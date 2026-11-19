# Comparación por celda — atlas v7 limpio (Adobe Firefly) vs original

**Veredicto de ruido: DESAPARECIDO.** Medido sobre el GIM decodificado (lo que dibuja el juego):
- Motas aisladas (componentes ≤4 px) en las 29 celdas reemplazadas: **0** (versión ruidosa anterior: 572; atlas original: 0).
- Cada celda nueva es esencialmente un solo componente conexo (1; 2–3 solo en C02 y C15, donde el símbolo ♂/♀ es un glifo separado — correcto).
- Píxeles distintos fuera de las 29 celdas: **0** (los 28 nombres propios quedan pixel-perfect).
- Gzip del atlas: **62,818 B** en hueco de 75,776 B (margen 12,958 B).

Nota de medición: la primera medición dentro del script de composición usaba alfa>0 sobre el PNG compuesto y contaba el halo de remuestreo LANCZOS como motas (falso positivo: 838). La medición válida es la del GIM decodificado, binario como el original: 0 motas.

| Celda | Texto en celda | Escala | Tinta (px) | Motas nuevo / ruidoso / orig | Comp. nuevo |
|---|---|---|---|---|---|
| C01 | Altavoz | 0.429 | 91x27 (52.0%/93.1%) | 0 / 27 / 0 | 1 |
| C02 | Mamá de Kota | 0.397 | 143x27 (92.3%/93.1%) | 0 / 45 / 0 | 3 |
| C03 | Anciana | 0.422 | 95x27 (70.9%/93.1%) | 0 / 24 / 0 | 1 |
| C04 | ¿Compañero de clase? | 0.415 | 128x27 (97.7%/93.1%) | 0 / 0 / 0 | 1 |
| C05 | ¿Compañero de clase? | 0.415 | 125x27 (95.4%/93.1%) | 0 / 0 / 0 | 1 |
| C06 | Estudiante | 0.45 | 98x27 (75.4%/93.1%) | 0 / 17 / 0 | 1 |
| C09 | Reportero | 0.374 | 117x23 (98.3%/82.1%) | 0 / 24 / 0 | 1 |
| C10 | Compañero de equipo | 0.406 | 112x26 (94.1%/92.9%) | 0 / 0 / 0 | 1 |
| C12 | Estudiante ♂ | 0.39 | 112x24 (98.2%/82.8%) | 0 / 28 / 0 | 1 |
| C13 | Empleado | 0.419 | 98x26 (87.5%/92.9%) | 0 / 26 / 0 | 1 |
| C15 | Estudiante ♀ | 0.418 | 109x27 (98.2%/90.0%) | 0 / 44 / 0 | 2 |
| C16 | ¿Profesor? | 0.386 | 108x22 (98.2%/78.6%) | 0 / 30 / 0 | 1 |
| C17 | Todos | 0.433 | 73x26 (67.6%/92.9%) | 0 / 28 / 0 | 1 |
| C18 | Todos | 0.433 | 72x26 (66.7%/92.9%) | 0 / 21 / 0 | 1 |
| C19 | Todos | 0.433 | 68x26 (63.0%/92.9%) | 0 / 29 / 0 | 1 |
| C21 | ¡Profesor! | 0.385 | 102x23 (98.1%/82.1%) | 0 / 20 / 0 | 1 |
| C28 | Alumno menor | 0.426 | 83x25 (97.6%/89.3%) | 0 / 0 / 0 | 1 |
| C30 | Cliente | 0.421 | 83x25 (97.6%/89.3%) | 0 / 14 / 0 | 1 |
| C31 | Mujer | 0.449 | 83x26 (97.6%/89.7%) | 0 / 17 / 0 | 1 |
| C33 | ¿¿¿Yo??? | 0.389 | 82x23 (97.6%/82.1%) | 0 / 27 / 0 | 1 |
| C35 | ¿Tigre? | 0.412 | 80x25 (97.6%/89.3%) | 0 / 24 / 0 | 1 |
| C40 | ¿Pájaro? | 0.316 | 71x22 (97.3%/81.5%) | 0 / 25 / 0 | 1 |
| C41 | ¿Quién? | 0.38 | 65x27 (94.2%/93.1%) | 0 / 28 / 0 | 1 |
| C44 | ¡Yo!? | 0.407 | 59x24 (96.7%/85.7%) | 0 / 0 / 0 | 1 |
| C45 | Ambos | 0.387 | 58x24 (96.7%/88.9%) | 0 / 27 / 0 | 1 |
| C49 | Señora | 0.3 | 54x20 (96.4%/71.4%) | 0 / 15 / 0 | 1 |
| C50 | ¡¡Yo!! | 0.398 | 53x23 (96.4%/82.1%) | 0 / 10 / 0 | 1 |
| C51 | Anfitrión | 0.252 | 53x16 (96.4%/55.2%) | 0 / 8 / 0 | 1 |
| C56 | ¡Yo! | 0.433 | 43x26 (93.5%/92.9%) | 0 / 14 / 0 | 1 |

## Decisiones de Sam aplicadas (19 nov)
- C04/C05 quedan como **COMPAÑERO?**, C10 como **COMPAÑERO**, C28 como **JUNIOR**, C44 como **¡¿YO?!** (texto v6 tal cual, sin ronda ChatGPT).
- C49 SEÑORA (tinta 54x20, 71.4% alto) y C51 ANFITRIÓN (53x16, 55.2% alto) quedan como están, más chicos: Sam dijo que no importa.
- C06 ESTUDIANTE recortado de C15 (hueco real entre palabra y ♀).

Hoja visual: `comparacion-celdas-v7-limpio.png` (original izquierda / v7 limpio derecha, zoom 3x).
