# Reporte v7 FINAL — atlas limpio (Adobe Firefly) + ISO v7

**Fecha:** 19 nov 2026, ~16:13–16:50 UTC (10:13–10:50 a. m. CST)
**Veredicto: LA ISO v7 ESTÁ CONSTRUIDA Y VERIFICADA BINARIAMENTE AL 100%. El atlas quedó limpio como el original (0 motas). La prueba visual en PPSSPP confirma que el juego arranca, el título está en español y las plaquitas de nombre propio se ven perfectas — pero la plaquita TODOS no se llegó a ver en juego (ver §5).**

## ISO v7
- **Ruta:** `~/workspace/toradora/toradora-portable-ES-v7.iso`
- **md5:** `62a5416791fbe20e8896320a830bb90f` (1,708,947,456 B)
- **v6 intacta:** `88584bd0656046fa900463ab15e9fe48` (respaldo en `repack-full/backup-iso-v6/`)

## 1. Recogida — 29/29 rótulos Adobe Firefly
- Copiados de `~/workspace/browser_downloads/sess-2037473396/` a `atlas-v7/limpios-adobe/<CODIGO>.png` según el mapeo exacto (el archivo extra `-0-` NO se usó).
- **29/29 PNG RGBA válidos con canal alfa** (fondo transparente), todos con miles de píxeles opacos.
- **Verificación visual de las 29 etiquetas (hoja `verificar-limpios-hoja.png`, 3 partes):** textos completos y correctos; marcas pequeñas intactas — ¿ ¡ (C16, C21, C33, C35, C40, C41, C44, C50, C51, C56), ♂ (C12) y ♀ (C15) presentes; los 6 glifos fusionados de C44 (`¡¿YO?!`) intactos. Adobe no dañó ninguna etiqueta.

## 2. Composición — 29/29 en el atlas original
- Script `atlas-v7/componer-atlas-v7-limpio.py` (adaptado de `componer-atlas-v7.py`): borra primero la tinta original de cada celda, pega el rótulo limpio recortando el borde transparente, escala para caber (centrado, 2 px margen), cuantiza a la paleta original.
- **Píxeles distintos fuera de las 29 celdas: 0** (los 28 nombres propios quedan pixel-perfect).
- GIM: `sg_chaname-v7-limpio.gim` (197,840 B); **gzip 62,818 B en hueco de 75,776 B (margen 12,958 B)**.
- Decisiones de Sam aplicadas: C04/C05 `COMPAÑERO?`, C10 `COMPAÑERO`, C28 `JUNIOR`, C44 `¡¿YO?!` (texto v6 tal cual); C49 SEÑORA (tinta 54x20, 71.4% alto) y C51 ANFITRIÓN (53x16, 55.2% alto) quedan más chicos, como dijo Sam que no importa; C06 ESTUDIANTE recortado de C15.

## 3. Comparación — PUERTA: RUIDO DESAPARECIDO ✅
- Medición sobre el **GIM decodificado** (lo que dibuja el juego), por celda:
  - **Motas aisladas (componentes ≤4 px): 0 en las 29 celdas** (versión ruidosa anterior: 572; atlas original: 0).
  - Cada celda nueva es esencialmente un solo componente conexo (1; 2–3 solo en C02 y C15, donde ♂/♀ es un glifo separado — correcto).
  - Hoja visual `comparacion-celdas-v7-limpio.png` (original izq / v7 limpio der, zoom 3x) + `comparacion-celdas-v7-limpio.md` + `.json`: las 29 celdas se ven limpias, completas, centradas, sin motas ni invasión de vecinas.
- **Nota de medición:** la primera medición dentro del script de composición usaba alfa>0 sobre el PNG compuesto y contaba el halo de remuestreo LANCZOS como motas (falso positivo: 838). La medición válida es la del GIM decodificado, binario como el original: **0 motas**. El error fue mío al medir, no del atlas.

## 4. Build + verificación binaria — PERFECTA ✅
- Script `build-final-v7.py` (adaptado de `build-final-v6.py`, base v6): solo cambia el atlas (74,937 → 62,818 B); seekmap delta +0 B (mismo nº de dígitos); nivel 9, 288,015 B en hueco de 288,768 B.
- **Incidente:** `pycdlib` no estaba instalado en la VM (se perdió con un reemplazo); reinstalado con `pip3 install --break-system-packages pycdlib` (1.22.0). El primer intento de build falló solo por eso; el segundo pasó limpio.
- Verificador `investigacion-texturas/verificar-v7.py` (`verificar-v7-report.json`), **0 fallos**:
  - Escenas: **363/363 OK**; títulos: **450/450 OK**.
  - Atlas byte-idéntico al convertido limpio (62,818 B); headers **13/13 OK**.
  - **Solo cambió el atlas:** resource.dat v7 == v6 excepto la región del atlas + su campo de tamaño; first.dat v7 == v6 excepto el seekmap + su campo de tamaño. Seekmap atlas: 62,818 B.
  - ISO v5 y v6 intactas tras el build.

## 5. Prueba visual en PPSSPP (VM) — PARCIAL ⚠️
- **Tiempo total: 27 min (16:23–16:50 UTC), dentro del tope de 30 min.** PPSSPP detenido por PID al final (verificado: 0 procesos).
- Entorno: Xvfb :99 y PulseAudio seguían corriendo (PIDs 33521/33537); `AppDir/AppRun` (no AppImage).
- **Arranque: 10 min** (no 7): ~2 min logos + opening hasta el título. El opening no se salta con teclado.
- **Título en español verificado** (Nueva partida / Continuar / Opciones / Extra / Instalar).
- **Prólogo en español verificado:** batalla (`¡Turno de RYUUJI!`, `¡TAIGA usó un rayo mortal!`, `¡YURI compró un departamento!...`) + diálogo del hospital, todo en español, sin errores (solo los avisos benignos `E[SCEKERNEL]` habituales y `failed to open /font/zh_gb.pgf`).
- **Plaquitas de nombre propio PERFECTAS en juego:** RYUUJI, TAIGA y ??? se ven limpias, nítidas, con el mismo estilo del original, sin ruido ni invasión (capturas `shots-v7/t08`, `t10`, `t11`, `u05`, `u07`, `u09`, `u11`, etc.). Ojo: estas son celdas originales sin tocar, no las nuevas.
- **❌ La plaquita TODOS no se llegó a ver en juego.** El avance fue lento (los toques instantáneos de X no se registran a bajo FPS; solo funcionan holds de 0.5 s; el texto se teclea lento y muchos toques solo completan el tecleo en vez de avanzar: ~0.5 entradas por toque). Última captura (u12) en la entrada #55 del prólogo (`Ryuuji「..................Lo siento, no.」`); **TODOS es la #62** (`Todos「Y así es la historia.」`), **7 entradas más adelante**. La captura se detuvo por el tope de 30 min.
- **Lección para una corrida de seguimiento:** guardar la partida en el menú del sistema al llegar al hospital; así la siguiente corrida puede usar Continuar y llegar a #62 en ~2 min.

## Veredicto honesto
El atlas quedó limpio como el original por todas las mediciones (0 motas, comparación por celda, verificación binaria perfecta) y la ruta de renderizado en juego está probada por las plaquitas de nombre propio, que usan el mismo atlas y se ven perfectas. **La única verificación que falta es ver la plaquita TODOS dibujada en juego.** Recomendación: que Sam la confirme en su playtest de iPhone (llegar a #62 son ~2 min de diálogo desde el inicio del prólogo), o hacer una corrida VM de seguimiento con guardado previo. No recomiendo re-abrir la v7 por esto: el riesgo residual es mínimo (TODOS pasó por la misma pipeline que las demás celdas, verificadas 1 por 1).

## Archivos
- ISO v7: `toradora/toradora-portable-ES-v7.iso` (md5 `62a5416791fbe20e8896320a830bb90f`)
- Reporte de build: `repack-full/build-v7-report.json`; respaldo v6: `repack-full/backup-iso-v6/`
- Atlas limpio: `investigacion-texturas/atlas-v7/sg_chaname-v7-limpio.{png,gim,gim.gz}` + `sg_chaname-v7-limpio-decoded.png`
- Rótulos limpios: `investigacion-texturas/atlas-v7/limpios-adobe/C*.png` (29)
- Comparación: `investigacion-texturas/atlas-v7/comparacion-celdas-v7-limpio.{md,json,png}`; ruido: `ruido-v7-limpio.json`
- Scripts: `build-final-v7.py`, `investigacion-texturas/verificar-v7.py`, `investigacion-texturas/atlas-v7/componer-atlas-v7-limpio.py`
- Capturas PPSSPP: `investigacion-texturas/atlas-v7/shots-v7/` (título, batalla, diálogo; `t01–t18`, `u01–u12`, `hoja-t1/2/3.png`, `hoja-u1/2.png`; log `ppsspp-v7.log`)
- Verificación binaria: `investigacion-texturas/verificar-v7-report.json`
