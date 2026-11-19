# Recalcula los ＿ (saltos de línea) del prólogo para el español.
# Reglas (Sam, Nov 17): traducción FIEL (no se cambia ninguna palabra),
# solo se mueven los ＿. Corte ENTRE palabras, línea ≤40 car, ≤3 líneas.
# El ＿ del inglés se descarta; se recalcula desde cero para el español.
import re, math

MAX_LIN = 40      # máximo caracteres por línea (foto: 41 cabe, 42 se corta)
TARGET   = 38     # objetivo para dejar margen con caracteres anchos
MAX_LINEAS = 3

def leer_po(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def parsear(content):
    # Devuelve lista de (msgid_raw, msgstr_raw) preservando el formato crudo.
    # El patrón respeta los escapes: ((?:[^"\\]|\\.)*) captura el contenido
    # sin cortar en una comilla escapada \" (el bug que truncaba cadenas
    # con comillas y desalineaba todas las entradas siguientes).
    entries = []
    pat = re.compile(r'msgid "((?:[^"\\]|\\.)*)"\nmsgstr "((?:[^"\\]|\\.)*)"', re.DOTALL)
    for m in pat.finditer(content):
        entries.append((m.group(1), m.group(2)))
    return entries

def desescapar(s):
    # \" -> " y \\ -> \ ; otros escapes se dejan tal cual.
    return re.sub(r'\\(.)', lambda m: m.group(1) if m.group(1) in '"\\' else m.group(0), s)

def escapar(s):
    # Primero las barras, luego las comillas (el orden importa).
    return s.replace('\\', '\\\\').replace('"', '\\"')

def reenvolver(texto):
    """Recibe el texto dentro de 「」 (con o sin ＿) y devuelve el texto
    con los ＿ recalculados. No cambia palabras, solo los saltos."""
    # Quitar los ＿ existentes (reemplazar por espacio) y normalizar espacios
    limpio = texto.replace('＿', ' ')
    limpio = re.sub(r' +', ' ', limpio).strip()
    if not limpio:
        return texto
    palabras = limpio.split(' ')
    # Longitud total contando un espacio entre palabras
    total = sum(len(p) for p in palabras) + max(0, len(palabras) - 1)
    if total <= MAX_LIN:
        return limpio  # una sola línea, sin ＿
    n = math.ceil(total / TARGET)
    if n > MAX_LINEAS:
        n = MAX_LINEAS
    # Reparto equilibrado: objetivo por línea
    objetivo = total / n
    lineas = []
    actual = []
    long_actual = 0
    for i, pal in enumerate(palabras):
        # longitud si agregamos esta palabra
        nueva = long_actual + (1 if actual else 0) + len(pal)
        # ¿rompemos antes de esta palabra?
        # Romper si: la línea ya llegó al objetivo y aún quedan palabras,
        # y agregar la palabra superaría el máximo.
        if actual and nueva > MAX_LIN:
            lineas.append(' '.join(actual))
            actual = [pal]
            long_actual = len(pal)
        elif actual and long_actual >= objetivo and len(lineas) < n - 1:
            # Ya llegamos al objetivo y aún nos quedan líneas: romper aquí
            # para equilibrar (evita una última línea diminuta).
            lineas.append(' '.join(actual))
            actual = [pal]
            long_actual = len(pal)
        else:
            actual.append(pal)
            long_actual = nueva
    if actual:
        lineas.append(' '.join(actual))
    # Nov 17: si el reparto sale en más de 3 líneas, NO fusionar las últimas
    # dos: eso creaba líneas de 41-56 caracteres que luego fallaban la
    # verificación (los 17 fallos del 19:24). Se dejan las 4 líneas y el
    # llamador las reporta como problema; el flujo de fix las acorta.
    return '＿'.join(lineas)

def main():
    import sys
    in_path = sys.argv[1] if len(sys.argv) > 1 else 'po-es/_0000ESS1.po'
    out_path = sys.argv[2] if len(sys.argv) > 2 else in_path
    content = leer_po(in_path)
    entries = parsear(content)
    print(f"Entradas: {len(entries)}")
    cambios = []
    problemas = []
    nuevas = []
    for idx, (mid_raw, mstr_raw) in enumerate(entries):
        mid = desescapar(mid_raw)
        mstr = desescapar(mstr_raw)
        if idx == 0 and mid == '':
            nuevas.append((mid_raw, mstr_raw))
            continue
        m = re.search(r'^(.*?)「(.*?)」(.*)$', mstr, re.DOTALL)
        if not m:
            nuevas.append((mid_raw, mstr_raw))
            continue
        antes, texto, despues = m.group(1), m.group(2), m.group(3)
        nuevo_texto = reenvolver(texto)
        nuevo_mstr = f"{antes}「{nuevo_texto}」{despues}"
        # Verificar: líneas ≤40, ≤3 líneas, sin palabra partida
        lineas = nuevo_texto.split('＿')
        ok = True
        for lin in lineas:
            if len(lin) > MAX_LIN:
                ok = False
                problemas.append((idx, f"línea {len(lin)} car: {lin}"))
        if len(lineas) > MAX_LINEAS:
            ok = False
            problemas.append((idx, f"{len(lineas)} líneas"))
        if nuevo_mstr != mstr:
            cambios.append((idx, mstr, nuevo_mstr, lineas))
        nuevas.append((mid_raw, escapar(nuevo_mstr)))
    # Escribir el .po corregido
    out = []
    # Reconstruir preservando la estructura: el .po original es una secuencia
    # de bloques msgid/msgstr. Lo reescribimos en el mismo orden.
    for (mid_raw, mstr_raw) in nuevas:
        out.append(f'msgid "{mid_raw}"\nmsgstr "{mstr_raw}"\n')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(f"\nCadenas modificadas: {len(cambios)}")
    print(f"Problemas restantes: {len(problemas)}")
    for p in problemas:
        print("  ⚠", p)
    print("\n=== CAMBIOS (antes → después) ===")
    for idx, antes, despues, lineas in cambios:
        print(f"\n--- entrada {idx} ---")
        print(f"  ANTES: {antes}")
        print(f"  DESPUÉS: {despues}")
        for j, lin in enumerate(lineas):
            print(f"    L{j+1} [{len(lin)}]: {lin}")

if __name__ == '__main__':
    main()
