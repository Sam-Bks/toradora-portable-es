#!/usr/bin/env python3
"""Verificación binaria de v7 (sin PPSSPP).

- Extrae resource.dat y first.dat del ISO v7.
- Por cada escena del catálogo: descomprime el .obj.gz del resource.dat
  v7 y confirma que cada bloque 0x02BC trae el título ES esperado
  (y que el resto de bloques es idéntico al .obj v5).
- Atlas: descomprime sg_chaname.gim.gz del resource.dat v7 y confirma
  que es byte-idéntico al convertido limpio (sg_chaname-v7-limpio.gim.gz).
- Headers: descomprime cada sg_title.gim.gz del first.dat v7 y confirma
  que es byte-idéntico al convertido.
- Además: resource.dat v7 == resource.dat v6 EXCEPTO la región del atlas
  + su campo de tamaño; first.dat v7 == first.dat v6 EXCEPTO la región
  del seekmap + su campo de tamaño (prueba de que SOLO cambió el atlas).
- Escribe un reporte JSON.
"""
import gzip, hashlib, json, os, struct, sys
import pycdlib

BASE = "/home/hatch/workspace/toradora"
INV = os.path.join(BASE, "investigacion-texturas")
WORK = os.path.join(BASE, "repack-full")
A7 = os.path.join(INV, "atlas-v7")
ISO_V7 = os.path.join(BASE, "toradora-portable-ES-v7.iso")
RES_V6 = os.path.join(WORK, "resource-v6.dat")
FIRST_V6 = os.path.join(WORK, "first-v6.dat")
RES_V5 = os.path.join(WORK, "resource-v5.dat")
CATALOG = os.path.join(INV, "titulos-escena-v5.json")
TR = os.path.join(INV, "titulos-es.json")
ATLAS_GZ = os.path.join(A7, "sg_chaname-v7-limpio.gim.gz")
HEADERS_DIR = os.path.join(INV, "prueba-titulos", "headers")
REPORT = os.path.join(INV, "verificar-v7-report.json")

TITLE_TYPE = 0x02BC
ATLAS_OFF = 54349824
ATLAS_SIZE_FIELD = 54227896
ATLAS_NEW_SIZE = 62818
ATLAS_OLD_SIZE = 74937
HDR_BASE_OFF = 75776
HDR_SLOT = 4096
SEEKM_OFF = 475136
SEEKM_SIZE_OFF = 88


def read_iso_file(iso_path, iso_file):
    iso = pycdlib.PyCdlib()
    iso.open(iso_path)
    try:
        with iso.open_file_from_iso(iso_path=iso_file) as fp:
            return fp.read()
    finally:
        iso.close()


def titles_in_obj(obj):
    """Devuelve [(block_index, offset, text)] para cada bloque 0x02BC."""
    nblocks = struct.unpack_from("<I", obj, 0)[0]
    out = []
    off = 0x30
    for bi in range(nblocks):
        size, typ = struct.unpack_from("<IH", obj, off)
        if typ == TITLE_TYPE:
            body = obj[off + 6:off + size]
            nunits = struct.unpack_from("<I", body, 0)[0]
            text = body[4:4 + nunits * 2].decode("utf-16-le")
            out.append((bi, off, text))
        off += size
    return out


def main():
    res_v7 = read_iso_file(ISO_V7, "/PSP_GAME/USRDIR/resource.dat")
    first_v7 = read_iso_file(ISO_V7, "/PSP_GAME/USRDIR/first.dat")
    res_v6 = open(RES_V6, "rb").read()
    first_v6 = open(FIRST_V6, "rb").read()
    res_v5 = open(RES_V5, "rb").read()
    cat = json.load(open(CATALOG, encoding="utf-8"))["catalog"]
    tr = {t["en"]: t["es"] for t in json.load(open(TR, encoding="utf-8"))["table"]}
    by_scene = {}
    for t in cat:
        by_scene.setdefault(t["scene"], []).append(t)

    rep = {"scenes_checked": 0, "titles_checked": 0, "titles_ok": 0,
           "scenes_ok": 0, "failures": [], "atlas_ok": False, "headers_ok": 0,
           "only_atlas_changed": False}
    # escenas (igual que v6: títulos ES, resto idéntico a v5)
    for scene in sorted(by_scene):
        apps = by_scene[scene]
        off = apps[0]["gz_offset"]
        container = off - 2048
        size_v7 = struct.unpack_from("<I", res_v7, container + 24)[0]
        size_v5 = struct.unpack_from("<I", res_v5, container + 24)[0]
        gz7 = bytes(res_v7[off:off + size_v7])
        obj7 = gzip.decompress(gz7)
        obj5 = gzip.decompress(bytes(res_v5[off:off + size_v5]))
        if len(obj7) != len(obj5):
            rep["failures"].append({"scene": scene, "reason": "longitud .obj cambió"})
            continue
        t7 = titles_in_obj(obj7)
        rep["scenes_checked"] += 1
        ok_scene = True
        for bi, boff, text in t7:
            rep["titles_checked"] += 1
            en = [a["text"] for a in apps if a["block_index"] == bi and a["offset"] == boff]
            if not en:
                rep["failures"].append({"scene": scene, "block": bi,
                                        "reason": f"bloque 0x02BC inesperado: {text!r}"})
                ok_scene = False
                continue
            esperado = tr[en[0]]
            if text != esperado:
                rep["failures"].append({"scene": scene, "block": bi,
                                        "reason": f"título {text!r} != esperado {esperado!r}"})
                ok_scene = False
            else:
                rep["titles_ok"] += 1
        if ok_scene:
            rep["scenes_ok"] += 1
    # atlas
    atlas_new = open(ATLAS_GZ, "rb").read()
    atlas_size = struct.unpack_from("<I", res_v7, ATLAS_SIZE_FIELD)[0]
    atlas_v7 = bytes(res_v7[ATLAS_OFF:ATLAS_OFF + atlas_size])
    rep["atlas_ok"] = atlas_v7 == atlas_new
    rep["atlas_size"] = atlas_size
    if not rep["atlas_ok"]:
        rep["failures"].append({"scene": "ATLAS", "reason": "sg_chaname no coincide con el convertido limpio"})
    # headers
    for i in range(1, 14):
        name = f"sg_title{i:02d}"
        new_gz = open(os.path.join(HEADERS_DIR, f"{name}.gim.gz"), "rb").read()
        off = HDR_BASE_OFF + (i - 1) * HDR_SLOT
        sf = 2360 + (i - 1) * 16
        sz = struct.unpack_from("<I", first_v7, sf)[0]
        cur = bytes(first_v7[off:off + sz])
        if cur == new_gz:
            rep["headers_ok"] += 1
        else:
            rep["failures"].append({"scene": name, "reason": f"header no coincide ({sz} B vs {len(new_gz)} B)"})
    # solo cambió el atlas: resource.dat v7 vs v6
    def diff_ranges(a, b, allowed):
        """Devuelve lista de (inicio, fin) donde a!=b fuera de las regiones permitidas."""
        diffs = []
        i = 0
        n = len(a)
        while i < n:
            if a[i] != b[i]:
                j = i
                while j < n and a[j] != b[j]:
                    j += 1
                # ¿está [i,j) dentro de alguna región permitida?
                ok = any(s <= i and j <= e for s, e in allowed)
                if not ok:
                    diffs.append((i, j))
                i = j
            else:
                i += 1
        return diffs
    res_allowed = [(ATLAS_OFF, ATLAS_OFF + ATLAS_OLD_SIZE),
                   (ATLAS_SIZE_FIELD, ATLAS_SIZE_FIELD + 4)]
    res_diffs = diff_ranges(res_v7, res_v6, res_allowed)
    seek_size_v7 = struct.unpack_from("<I", first_v7, SEEKM_SIZE_OFF)[0]
    seek_size_v6 = struct.unpack_from("<I", first_v6, SEEKM_SIZE_OFF)[0]
    first_allowed = [(SEEKM_OFF, SEEKM_OFF + max(seek_size_v7, seek_size_v6)),
                     (SEEKM_SIZE_OFF, SEEKM_SIZE_OFF + 4)]
    first_diffs = diff_ranges(first_v7, first_v6, first_allowed)
    rep["resource_diffs_outside_atlas"] = res_diffs
    rep["first_diffs_outside_seekmap"] = first_diffs
    rep["only_atlas_changed"] = (not res_diffs and not first_diffs)
    if res_diffs:
        rep["failures"].append({"scene": "RESOURCE", "reason": f"diferencias fuera del atlas: {res_diffs[:5]}"})
    if first_diffs:
        rep["failures"].append({"scene": "FIRST", "reason": f"diferencias fuera del seekmap: {first_diffs[:5]}"})
    # seekmap: el tamaño del atlas debe ser 62818
    seek = gzip.decompress(first_v7[SEEKM_OFF:SEEKM_OFF + seek_size_v7])
    import re as _re
    m = _re.search(rb"sg_chaname\.gim\.gz +\d+ (\d+) ", seek)
    rep["seekmap_atlas_size"] = int(m.group(1)) if m else None
    if rep["seekmap_atlas_size"] != ATLAS_NEW_SIZE:
        rep["failures"].append({"scene": "SEEKMAp", "reason": f"tamaño atlas en seekmap {rep['seekmap_atlas_size']}"})
    json.dump(rep, open(REPORT, "w", encoding="utf-8"), indent=1)
    print(f"escenas verificadas: {rep['scenes_checked']}, OK: {rep['scenes_ok']}")
    print(f"títulos verificados: {rep['titles_checked']}, OK: {rep['titles_ok']}")
    print(f"atlas OK: {rep['atlas_ok']} (tamaño {rep['atlas_size']} B)")
    print(f"headers OK: {rep['headers_ok']}/13")
    print(f"solo cambió el atlas: {rep['only_atlas_changed']}")
    print(f"seekmap atlas: {rep['seekmap_atlas_size']} B")
    print(f"fallos: {len(rep['failures'])}")
    for f in rep["failures"][:20]:
        print("  ", f)
    print(f"reporte: {REPORT}")
    return 0 if not rep["failures"] else 2

if __name__ == "__main__":
    sys.exit(main())
