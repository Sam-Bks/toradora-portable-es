#!/usr/bin/env python3
"""Build ISO v7: SOLO cambia el atlas sg_chaname (rótulos limpios Adobe Firefly)
sobre la base v6. Todo lo demás (275 títulos, 13 headers) idéntico a la v6.

- Parte de repack-full/resource-v6.dat y repack-full/first-v6.dat.
- Atlas: sg_chaname-v7-limpio.gim.gz (62,818 B) en 54,349,824; tamaño GPDA
  en 54,227,896; seekmap 74,937 -> 62,818 (mismo nº de dígitos: el texto
  descomprimido del seekmap NO cambia de longitud).
- Construye toradora-portable-ES-v7.iso (copia del ISO v6, reemplazando
  resource.dat y first.dat con pycdlib).
- Respalda el ISO v6 en repack-full/backup-iso-v6/ ANTES de tocar nada.
- NUNCA toca toradora-portable-ES-v6.iso (salvo leerlo) ni los .dat v6
  originales. NO usa repack_gpda.py. NO usa rebalancear.py.
"""
import gzip, hashlib, json, os, re, shutil, struct, datetime
from contextlib import ExitStack

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, "repack-full")
INV = os.path.join(BASE, "investigacion-texturas")
A7 = os.path.join(INV, "atlas-v7")
RES_V6 = os.path.join(WORK, "resource-v6.dat")
FIRST_V6 = os.path.join(WORK, "first-v6.dat")
ATLAS_GZ = os.path.join(A7, "sg_chaname-v7-limpio.gim.gz")
ATLAS_OLD_SIZE = 74937
ORIG_ISO = os.path.join(BASE, "toradora-portable-ES-v6.iso")
OUT_ISO = os.path.join(BASE, "toradora-portable-ES-v7.iso")
BACKUP_DIR = os.path.join(WORK, "backup-iso-v6")
REPORT_PATH = os.path.join(WORK, "build-v7-report.json")

ATLAS_OFF = 54349824
ATLAS_SIZE_FIELD = 54227896
SEEKM_OFF = 475136
SEEKM_SIZE_OFF = 88
SEEKM_GAP = 288768

def log(*a):
    print(*a, flush=True)

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def coincide_contenido(fp, esperado):
    if fp.length() != len(esperado):
        return False
    vista = memoryview(esperado)
    for inicio in range(0, len(vista), 1 << 20):
        bloque = vista[inicio:inicio + (1 << 20)]
        if fp.read(len(bloque)) != bloque:
            return False
    return True

def abrir_iso_nuevo(ruta, flags):
    return os.open(ruta, flags | os.O_CREAT | os.O_EXCL)

def main():
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    report = {"ts": ts, "checks": []}
    def check(name, ok, detail=""):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": str(detail)})
        log(f"  [{'OK' if ok else 'FALLO'}] {name} {detail}")
        if not ok:
            raise SystemExit(f"CHECK FALLIDO: {name} {detail}")

    log("== 0. Respaldo v6 + entradas ==")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_iso = os.path.join(BACKUP_DIR, "toradora-portable-ES-v6.iso")
    if not os.path.exists(backup_iso):
        shutil.copy2(ORIG_ISO, backup_iso)
        log(f"  respaldo v6: {backup_iso}")
    check("respaldo v6 existe y coincide con el original",
          md5(backup_iso) == md5(ORIG_ISO), md5(backup_iso))
    for path in (RES_V6, FIRST_V6, ATLAS_GZ, ORIG_ISO):
        check(f"entrada disponible: {path}", os.path.isfile(path))
    check(f"salida nueva: {OUT_ISO}", not os.path.lexists(OUT_ISO))
    check(f"reporte nuevo: {REPORT_PATH}", not os.path.lexists(REPORT_PATH))
    res_v6 = open(RES_V6, "rb").read()
    first_v6 = open(FIRST_V6, "rb").read()
    check("resource-v6.dat mide 426012672 B", len(res_v6) == 426012672, len(res_v6))
    check("first-v6.dat mide 1499136 B", len(first_v6) == 1499136, len(first_v6))
    report["v6_resource_md5"] = hashlib.md5(res_v6).hexdigest()
    report["v6_first_md5"] = hashlib.md5(first_v6).hexdigest()
    report["v6_iso_md5"] = md5(ORIG_ISO)
    check("ISO v6 md5 esperado 88584bd0656046fa900463ab15e9fe48",
          report["v6_iso_md5"] == "88584bd0656046fa900463ab15e9fe48", report["v6_iso_md5"])

    # ---- 1. Atlas en resource.dat ----
    log("== 1. Atlas sg_chaname limpio en resource.dat ==")
    res = bytearray(res_v6)
    atlas_gz = open(ATLAS_GZ, "rb").read()
    check("atlas limpio .gim.gz mide 62818 B", len(atlas_gz) == 62818, len(atlas_gz))
    cur = struct.unpack_from("<I", res, ATLAS_SIZE_FIELD)[0]
    check("tamaño GPDA atlas actual 74937 B", cur == ATLAS_OLD_SIZE, cur)
    cur2 = bytes(res[ATLAS_OFF:ATLAS_OFF + ATLAS_OLD_SIZE])
    check("atlas v6 actual descomprime a 197840 B",
          len(gzip.decompress(cur2)) == 197840)
    res[ATLAS_OFF:ATLAS_OFF + len(atlas_gz)] = atlas_gz
    struct.pack_into("<I", res, ATLAS_SIZE_FIELD, len(atlas_gz))
    check("atlas escrito + tamaño GPDA 62818 B",
          struct.unpack_from("<I", res, ATLAS_SIZE_FIELD)[0] == 62818)
    check("atlas nuevo descomprime a 197840 B",
          len(gzip.decompress(bytes(res[ATLAS_OFF:ATLAS_OFF + len(atlas_gz)]))) == 197840)
    report["resource_v7_md5"] = hashlib.md5(res).hexdigest()

    # ---- 2. Seekmap en first.dat (solo la línea del atlas) ----
    log("== 2. Seekmap (solo atlas) ==")
    first = bytearray(first_v6)
    seek_size = struct.unpack_from("<I", first, SEEKM_SIZE_OFF)[0]
    check("límites del seekmap v6",
          struct.unpack_from("<4sIII", first) == (b"GPDA", len(first_v6), 0, 8)
          and struct.unpack_from("<II", first, SEEKM_SIZE_OFF - 8) == (SEEKM_OFF, 0)
          and struct.unpack_from("<I", first, SEEKM_SIZE_OFF + 8)[0] == SEEKM_OFF + SEEKM_GAP
          and 0 < seek_size <= SEEKM_GAP, seek_size)
    seek = gzip.decompress(first[SEEKM_OFF:SEEKM_OFF + seek_size])
    log(f"  seekmap v6: comprimido {seek_size} B, descomprimido {len(seek)} B")
    lineas = seek.split(b"\r\n")
    idx_by_name = {}
    for li, L in enumerate(lineas):
        m = re.match(rb"\t+(sg_chaname\.gim\.gz) +", L)
        if m:
            idx_by_name[m.group(1).decode()] = li
    li = idx_by_name.get("sg_chaname.gim.gz")
    check("seekmap: línea única para sg_chaname.gim.gz", li is not None, li)
    L = lineas[li]
    m = re.match(rb"(\t+sg_chaname\.gim\.gz +\d+ )(\d+)( \d+ )", L)
    check("seekmap: formato de línea atlas", m is not None, L[:80])
    check("seekmap: tamaño actual atlas = 74937", int(m.group(2)) == ATLAS_OLD_SIZE, m.group(2))
    lineas[li] = m.group(1) + str(len(atlas_gz)).encode() + m.group(3)
    new_seek = b"\r\n".join(lineas)
    delta = len(new_seek) - len(seek)
    log(f"  seekmap nuevo: descomprimido {len(new_seek)} B (delta {delta:+d} B; mismo nº de dígitos)")
    check("seekmap: longitud descomprimida sin cambio", delta == 0, delta)
    report["seekmap_delta_bytes"] = delta
    chosen = None
    for lvl in (9, 8, 7, 6):
        gz = gzip.compress(new_seek, compresslevel=lvl, mtime=0)
        log(f"  seekmap nivel {lvl}: {len(gz)} B (hueco {SEEKM_GAP}) {'CABE' if len(gz) <= SEEKM_GAP else 'NO CABE'}")
        if len(gz) <= SEEKM_GAP:
            chosen = (lvl, gz)
            break
    check("algún nivel de seekmap cabe en el hueco", chosen is not None)
    lvl, new_seek_gz = chosen
    seek_end = SEEKM_OFF + len(new_seek_gz)
    first[SEEKM_OFF:seek_end] = new_seek_gz
    struct.pack_into("<I", first, SEEKM_SIZE_OFF, len(new_seek_gz))
    check("seekmap insertado descomprime a lo esperado",
          gzip.decompress(first[SEEKM_OFF:SEEKM_OFF + struct.unpack_from("<I", first, SEEKM_SIZE_OFF)[0]]) == new_seek)
    check("tamaño total first.dat intacto", len(first) == len(first_v6))
    report["seekmap_level"] = lvl
    report["seekmap_gz_len"] = len(new_seek_gz)
    report["first_v7_md5"] = hashlib.md5(first).hexdigest()

    # ---- 3. ISO v7 ----
    log("== 3. ISO v7 ==")
    import pycdlib
    iso_size = os.path.getsize(ORIG_ISO)
    report["v6_iso_size"] = iso_size
    res_path = os.path.join(WORK, "resource-v7.dat")
    first_path = os.path.join(WORK, "first-v7.dat")
    archivos = (
        (res_path, "/PSP_GAME/USRDIR/resource.dat", res_v6, bytes(res)),
        (first_path, "/PSP_GAME/USRDIR/first.dat", first_v6, bytes(first)),
    )
    with ExitStack() as limpiar:
        for local, _, _, parcheado in archivos:
            with open(local, "xb") as salida:
                limpiar.callback(os.unlink, local)
                salida.write(parcheado)
            log(f"{os.path.basename(local)}: {len(parcheado)} B")
        with open(ORIG_ISO, "rb") as origen, open(OUT_ISO, "r+b", opener=abrir_iso_nuevo) as copia:
            limpiar.callback(os.unlink, OUT_ISO)
            shutil.copyfileobj(origen, copia, length=1 << 20)
            copia.seek(0)
            iso = pycdlib.PyCdlib()
            iso.open_fp(copia)
            try:
                for _, iso_p, base, _ in archivos:
                    with iso.open_file_from_iso(iso_path=iso_p) as fp:
                        check(f"tamaño y contenido de {iso_p} coinciden con la base v6",
                              coincide_contenido(fp, base), f"{len(base)} B esperados")
                for local, iso_p, _, parcheado in archivos:
                    with open(local, "rb") as fp:
                        iso.modify_file_in_place(fp, len(parcheado), iso_path=iso_p)
            finally:
                iso.close()
        check("ISO v7 conserva el tamaño del ISO v6", os.path.getsize(OUT_ISO) == iso_size, iso_size)
        iso2 = pycdlib.PyCdlib()
        iso2.open(OUT_ISO)
        try:
            for _, iso_p, _, parcheado in archivos:
                with iso2.open_file_from_iso(iso_path=iso_p) as fp:
                    check(f"round-trip {iso_p}: tamaño y contenido idénticos",
                          coincide_contenido(fp, parcheado), f"{len(parcheado)} B esperados")
        finally:
            iso2.close()
        report["v7_iso_md5"] = md5(OUT_ISO)
        log(f"ISO v7: {OUT_ISO} ({iso_size} B)")
        log(f"  md5 ISO v7: {report['v7_iso_md5']}")
        check("ISO v6 intacto tras la copia", md5(ORIG_ISO) == report["v6_iso_md5"])
        check("resource-v6.dat intacto", hashlib.md5(open(RES_V6,'rb').read()).hexdigest() == report["v6_resource_md5"])
        check("first-v6.dat intacto", hashlib.md5(open(FIRST_V6,'rb').read()).hexdigest() == report["v6_first_md5"])
        with open(REPORT_PATH, "x", encoding="utf-8") as salida:
            limpiar.callback(os.unlink, REPORT_PATH)
            json.dump(report, salida, indent=1)
        limpiar.pop_all()
    log("DONE — reporte en repack-full/build-v7-report.json")

if __name__ == "__main__":
    main()
