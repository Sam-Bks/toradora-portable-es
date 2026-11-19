#!/usr/bin/env python3
"""Verificación SOLO LECTURA: ¿siguen intactas en los .po actuales las
correcciones de texto desplazado que Codex propuso en las rondas 1-3
(lotes 01-15)?

No modifica ningún .po. Compara, por entrada, el msgstr actual contra la
propuesta exacta de Codex del reporte, normalizando ＿ -> ' ' (igual que
los scripts restaurar-codex-ronda*.py), para no marcar como diferencia
los re-saltos de la auditoría de saltos de línea.

Salida: lotes/verificar-desplazados-rondas1-3.json
"""
import re, sys, os, json

BASE = '/home/hatch/workspace/toradora'
REPORTS = [
    os.path.join(BASE, 'lotes', 'revision-codex-lote-01-02-04-05-06.md'),
    os.path.join(BASE, 'lotes', 'revision-codex-lote-03-07-09-10-11.md'),
    os.path.join(BASE, 'lotes', 'revision-codex-lote-08-12-13-14-15.md'),
]
sys.path.insert(0, BASE)
from recalcular_guiones import parsear, desescapar

# Cabecera de problema, dos variantes de formato.
pat_head = re.compile(
    r'^(\d+)\. \*\*(?:Archivo: `po-es-(.+?)\.po` — cadena (\d+)|`po-es-(.+?)\.po`, cadena (\d+))',
    re.MULTILINE)
fence = re.compile(r'```text[ \t]*\r?\n(.*?)\r?\n[ \t]*```', re.DOTALL)
pat_problema = re.compile(r'\*\*Problema:\*\*\s*(.*?)(?=\n\s*\n|\n\s*\*\*)', re.DOTALL)

def norm(s):
    return ' '.join(desescapar(s).replace('＿', ' ').split())

resultados = []
for rep_path in REPORTS:
    texto = open(rep_path, encoding='utf-8').read()
    heads = list(pat_head.finditer(texto))
    for i, h in enumerate(heads):
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(texto)
        seg = texto[h.start():fin]
        esc = h.group(2) or h.group(4)
        cad = int(h.group(3) or h.group(5))
        m_prob = pat_problema.search(seg)
        prob = m_prob.group(1).strip() if m_prob else ''
        if 'desplazado' not in prob.lower():
            continue
        # Propuesta: el fence después de "Corrección propuesta exacta".
        idx = seg.find('Corrección propuesta exacta')
        if idx < 0:
            resultados.append({'reporte': os.path.basename(rep_path), 'escena': esc,
                               'cadena': cad, 'problema': prob[:120],
                               'estado': 'SIN_PROPUESTA'})
            continue
        f = fence.findall(seg[idx:])
        if not f:
            resultados.append({'reporte': os.path.basename(rep_path), 'escena': esc,
                               'cadena': cad, 'problema': prob[:120],
                               'estado': 'SIN_PROPUESTA'})
            continue
        propuesta = f[0].strip()
        po_path = os.path.join(BASE, 'po-es', esc + '.po')
        try:
            entradas = parsear(open(po_path, encoding='utf-8').read())
        except FileNotFoundError:
            resultados.append({'reporte': os.path.basename(rep_path), 'escena': esc,
                               'cadena': cad, 'problema': prob[:120],
                               'estado': 'SIN_PO'})
            continue
        if cad >= len(entradas):
            resultados.append({'reporte': os.path.basename(rep_path), 'escena': esc,
                               'cadena': cad, 'problema': prob[:120],
                               'estado': 'CADENA_FUERA_DE_RANGO'})
            continue
        actual = desescapar(entradas[cad][1])
        if norm(actual) == norm(propuesta):
            estado = 'INTACTA'
        else:
            estado = 'DIFIERE'
        resultados.append({'reporte': os.path.basename(rep_path), 'escena': esc,
                           'cadena': cad, 'problema': prob[:160], 'estado': estado,
                           'actual': actual[:200], 'propuesta': propuesta[:200]})

intactas = [r for r in resultados if r['estado'] == 'INTACTA']
difieren = [r for r in resultados if r['estado'] == 'DIFIERE']
otros = [r for r in resultados if r['estado'] not in ('INTACTA', 'DIFIERE')]
print(f"Problemas con 'desplazado' en rondas 1-3: {len(resultados)}")
print(f"  Intactas (coinciden con la propuesta de Codex): {len(intactas)}")
print(f"  Difieren (posible deshecho por rebalancear.py): {len(difieren)}")
print(f"  Otros (sin propuesta/PO/rango): {len(otros)}")
for r in difieren:
    print(f"  DIFIERE {r['escena']}:{r['cadena']} — {r['problema'][:100]}")
    print(f"    actual:    {r['actual'][:150]}")
    print(f"    propuesta: {r['propuesta'][:150]}")
for r in otros:
    print(f"  {r['estado']} {r['escena']}:{r['cadena']}")

out = os.path.join(BASE, 'lotes', 'verificar-desplazados-rondas1-3.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump({'resultados': resultados,
               'resumen': {'total': len(resultados), 'intactas': len(intactas),
                           'difieren': len(difieren), 'otros': len(otros)}}, f,
              ensure_ascii=False, indent=1)
print(f"Reporte en: {out}")
