# Traducción al español de Toradora! Portable (PSP)
## Documentación del proceso

*Fecha del documento: 19 de noviembre de 2026. Estado: traducción COMPLETA. Versión final: v7 (ISO `toradora-portable-ES-v7.iso`, md5 `62a5416791fbe20e8896320a830bb90f`), probada en juego.*

Este documento describe cómo se tradujo Toradora! Portable al español, qué herramientas se usaron, qué papel jugó la inteligencia artificial en el proceso y qué problemas aparecieron y cómo se resolvieron. Se publica junto con el parche para que cualquier persona pueda entender el método, reproducirlo y reportar errores.

## 1. Resumen del proyecto

Toradora! Portable es una novela visual para PSP, desarrollada por Guyzware y publicada por Bandai Namco el 30 de abril de 2009, solo en Japón. El jugador controla a Ryuuji Takasu en una historia original (despierta en el hospital con amnesia tras los sucesos del episodio de Navidad), con 21 finales y voces completas. No tuvo localización oficial en inglés ni en español. Su clasificación en Japón es CERO C (para mayores de 15 años); no contiene contenido para adultos.

La traducción al español parte de la ISO con el parche en inglés v1.10 ya aplicado (3 de agosto de 2014). No se encontró ninguna traducción completa al español: este proyecto es la primera.

Alcance: se tradujo todo el texto del juego, incluido lo que el parche en inglés dejó en japonés (por ejemplo, el archivo de datos ItemList.csv, que sigue en japonés en la versión 1.10; esos archivos se tradujeron directamente del japonés al español). El texto medido a partir de los archivos extraídos es:

- 363 escenas en total; 311 con texto y 52 vacías.
- 27,466 cadenas de texto.
- 183,040 palabras (1,325,176 caracteres).
- Duración estimada de una partida completa: entre 15 y 20 horas; unas 31 horas para ver todos los finales.

La variante de español es neutra, sin modismos de ningún país. Los personajes son estudiantes de preparatoria, así que el registro es natural y juvenil, pero sin regionalismos.

El proyecto se distribuye únicamente como parche: cada persona aplica el parche sobre su propia copia del juego. Nunca se distribuye la ISO.

![Pantalla de título en español: Nueva partida / Continuar / Opciones / Extra / Instalar](investigacion-texturas/atlas-v7/shots-ppsspp/title-final.png)

*Pantalla de título en español (v7, PPSSPP). El menú de título es texto del archivo `utf16.txt.gz`, no una textura.*

## 2. Qué se tradujo y qué quedó fuera

| Contenido | Estado en la v7 |
|---|---|
| Diálogo de las 310 escenas con texto (+ prólogo) | Español, 100 % |
| STARTPOINT: títulos de capítulo (275) y cadenas del sistema | Español, 100 % |
| Títulos de escena dentro de los .obj (450 apariciones, 275 únicos) | Español, 100 % |
| Texto del sistema `utf16.txt.gz` (315 líneas: título, opciones, guardar/cargar, Extra, mensajes, canciones) | Español, 100 % (versión A, canciones traducidas) |
| Listas de texto: ItemList.csv (58 objetos), charaname.txt (57), placename.txt (49), utf8.txt (7) | Español, 100 % |
| Atlas de nombres de hablante `sg_chaname.gim` (29 rótulos genéricos, incl. TODOS ×3) | Español, 100 % |
| Encabezados del menú del sistema `sg_title01–13` | Español, 100 % |
| Extras (minijuegos Rampage! Palmtop Tiger, Dress Up Breakout, juego de memoria, enciclopedia gráfica, globos del selector) | **No traducidos, por decisión expresa**: se dejan como están |
| Ayudas gráficas `Help0/Help1.gim`, pantallas de Game Over / Game Clear, logotipos de los minijuegos | No traducidos (son imágenes; el parche en inglés tampoco los tocó) |
| Manual físico del juego | No traducido: no existe escaneo digital y no está en la ISO |

Limitación conocida de los archivos Shift-JIS: `ItemList.csv`, `charaname.txt` y `placename.txt` llevan los acentos eliminados (á→a, ñ→n, ¿→?, ¡→!, etc.) porque Shift-JIS no puede representar á/é/í/ó/ú/ñ/¿/¡. La ＿ (guion bajo de ancho completo) y los símbolos ♂/♀ sí se conservaron, porque existen en Shift-JIS. Las versiones UTF-8 con acentos completos se guardan como referencia en `text-es/`.

Lo que queda en otro idioma dentro del juego es solo gráfico: los logotipos de los Extras, las ayudas dibujadas, la barra de vida de la batalla (que muestra «みのり» en kana japonés) y las letras impresas dentro de las ilustraciones de los objetos.

## 3. Cadena de trabajo (pipeline)

1. **Punto de partida.** Se parte de la ISO del juego con el parche en inglés v1.10 ya aplicado (cada quien aporta su propia copia).
2. **Conversión.** Si el archivo está en formato CHD, se convierte a ISO con chdman.
3. **Extracción de archivos.** Se extraen los archivos de datos del juego (resource.dat, first.dat y el guion script.dat) con tenoritool.
4. **Extracción del texto.** Los archivos de diálogo (.obj) se convierten a archivos .po (formato gettext), un archivo por escena, con la cadena en inglés como original y la traducción en español como destino.
5. **Conteo y planificación.** Se mide el texto real (palabras, cadenas, escenas) y se planifica el trabajo por lotes (80 lotes, 311 escenas).
6. **Glosario y guía de estilo.** Se fijan los nombres, los términos recurrentes y las reglas de formato antes de traducir.
7. **Traducción.** Gemini traduce cada lote de archivos .po siguiendo la guía de estilo y el glosario. Cuando se agotó la cuota de Gemini, Codex tradujo los últimos lotes (74, 76–80) y STARTPOINT, leyendo lotes ya traducidos y revisados como referencia de estilo.
8. **Revisión (primer filtro).** Gemini revisa la traducción en una llamada separada, con contexto limpio, comparando inglés y español, y corrige los .po directamente.
9. **Consolidación.** El coordinador del proyecto aplica las correcciones de la revisión y verifica el formato de los archivos .po.
10. **Revisión (segundo filtro).** Codex revisa el texto traducido como modelo independiente: congruencia entre lotes (misma voz por personaje, misma terminología, mismo tono, incluidos los lotes traducidos por modelos distintos), formato, sentido y fidelidad.
11. **Ajuste de saltos de línea.** Se recalculan los saltos de línea (＿) para el español, porque el español es más largo que el inglés y los cortes del inglés parten palabras y desbordan el cuadro de diálogo.
12. **Reempaquetado.** Los .po se convierten de nuevo a .obj y se reconstruyen los archivos de datos con el método in-place (ver sección 4). No se usa repack_gpda.py tal como está, porque rompe el juego (ver la advertencia en la sección 4).
13. **Prueba en PPSSPP.** Se juega la escena traducida en el emulador PPSSPP de escritorio.
14. **Control de calidad final.** El coordinador del proyecto juega las escenas traducidas y reporta problemas de texto, de formato y de visualización.
15. **Publicación y QA de la comunidad.** El parche se publica en foros. La comunidad juega y reporta errores; los reportes se corrigen en actualizaciones del parche. No hay una revisión humana completa línea por línea de todo el juego: la calidad se alcanza con la cadena de revisiones, la prueba en juego y los reportes de quienes juegan.

El trabajo se organizó con un orquestador automático que corría cada 15 minutos, mantenía hasta 7 sesiones de traducción en paralelo, lanzaba revisores al completarse cada lote, corregía automáticamente los lotes que fallaban la verificación (máximo 2 intentos de corrección por Gemini) y avisaba solo de avances o bloqueos. La regla de trabajo fue no parar: al topar con un límite, esperar a que se reiniciara y seguir.

## 4. Herramientas utilizadas

- **chdman** (herramienta de MAME). Convierte archivos CHD (formato comprimido de disco) a ISO. En este proyecto el CHD era de tipo DVD, por lo que se usó extractdvd (extractcd falló). También verifica la integridad del archivo (SHA1).
- **tenoritool.exe** (del proyecto TigerXDragon / DatWorker). Extrae los archivos .dat del juego (formato GPDA). Corre bajo mono en Linux; necesita el paquete libmono-i18n-cjk4.0-cil para leer Shift-JIS (codepage 932, japonés). Nota: DatWorker.exe no corre bajo mono (llama a componentes de Windows) y OBJEGUI.exe tampoco (necesita Windows Forms); por eso la extracción se hace directamente con tenoritool.
- **Scripts propios en Python.** Escritos para este proyecto:
  - extract_all.py: extracción recursiva de todos los .dat (las escenas contienen subarchivos .dat anidados).
  - extract_po.py: convierte cada .obj de diálogo a un archivo .po (un archivo por escena).
  - repack.py: convierte los .po traducidos de vuelta a .obj.
  - recalcular_guiones.py: recalcula los saltos de línea (＿) para el español.
  - rebalancear.py: mueve la cola de una frase al cuadro siguiente cuando la entrada siguiente es del mismo hablante y es corta, para no dejar el segundo cuadro casi vacío.
  - build-full-iso.py y familia (build-final-v4/v5/v6/v7.py, build-final-shift-iso*.py): construyen cada versión del ISO con el método in-place, con verificación round-trip por pycdlib.
  - gim_codec.py: codec GIM (parse, swizzle PSP 8-bit 16×8, conversión GIM↔PNG) para el trabajo de texturas.
  - **Advertencia: repack_gpda.py NO debe usarse tal como está.** Al reempaquetar, elimina las tablas de nombres de los archivos GPDA (escribe nameOffset=0 y no escribe la tabla). Eso encoge las cabeceras, mueve todos los archivos 6,144 bytes y deja obsoleto el índice seekmap.dat; el juego lee en la posición incorrecta y se cierra con error al pulsar New Game (Bad Execution Address, salto a c0ffeeee). El método correcto es el reemplazo in-place: se copian los archivos originales y solo se sustituyen los datos modificados en su posición exacta, actualizando únicamente los campos de tamaño y la línea correspondiente del seekmap. La lección es que extraer bien no equivale a jugar bien: la verificación por extracción no detecta este problema; solo lo detecta jugar.
- **pycdlib (1.22.0).** Biblioteca de Python para modificar imágenes ISO. Se usa su editor in-place para sustituir resource.dat y first.dat dentro de la ISO sin tocar el resto del disco.
- **translate-toolkit (txt2po / po2txt).** Herramientas estándar de gettext para convertir entre texto plano y .po. Se instaló como apoyo, pero en la práctica la generación y validación de los .po se hizo con Python propio (el validador msgfmt no estaba disponible; la validación se hace con un parser de Python que maneja los escapes de comillas).
- **PPSSPP v1.20.4** (versión portable para Windows). Emulador de PSP usado para probar el juego traducido. La prueba visual (que los caracteres ñ, ¿, ¡ se vean bien y que el texto quepa en el cuadro de diálogo) solo se puede hacer jugando; no hay forma fiable de automatizarla a distancia.
- **TigerXDragon** (licencia MIT, github.com/SH4FS0c13ty/TigerXDragon). Kit de herramientas creado para retraducir este juego a otro idioma a partir de la versión en inglés. Su flujo documentado es: extraer los .dat con DatWorker, extraer los .obj, traducir los .po, regenerar seekmap.dat y reconstruir la ISO. Ya se usó para la traducción al francés, lo que demuestra que el camino funciona. De este proyecto procede tenoritool, usado aquí para la extracción.

Formato de los archivos (resumen técnico):

- Los archivos de datos del juego usan el formato GPDA: cabecera (GPDA + tamaño total + número de entradas) + tabla de entradas (16 bytes por entrada: offset, tamaño y offset del nombre) + tabla de nombres. El juego localiza los archivos por nombre y usa seekmap.dat (un índice con nombre, offset y tamaño de cada archivo) para encontrarlos dentro de resource.dat.
- Los diálogos están en archivos .obj: un contador de bloques + cabecera de 0x2C + bloques (tamaño, tipo y datos). Los tipos de bloque con texto son 0x64/0x68 (diálogo), 0x67/0x69 (listas de opciones) y 0x12E/0x323. Las cadenas están en UTF-16LE. El formato de una línea es Nombre「texto」, y el salto de línea dentro del diálogo se marca con ＿ (guion bajo de ancho completo).
- Los títulos de escena viven en bloques 0x02BC dentro de cada .obj: longitud en unidades UTF-16, texto en UTF-16LE, sufijo fijo de 6 bytes y relleno cero hasta el tamaño del bloque (32/48/64/80/96/112 bytes, que admiten 8/16/24/32/40/48 unidades).
- Las texturas GIM de PSP usan formato INDEX8 con paleta RGBA8888 y píxeles en orden swizzled de PSP; el atlas de nombres mide 512×384 y sus celdas son de 108×28 píxeles.

## 5. Uso de inteligencia artificial

Este proyecto usa inteligencia artificial de forma explícita y con revisión humana. Ninguna parte del texto se publica sin pasar por la cadena de revisión y la prueba en juego.

- **Gemini (modelos Gemini 4 Hydrogen y Gemini 4 Argon en High, a través de Antigravity).** Hace tres trabajos distintos, en llamadas separadas con contexto limpio:
  - Traductor: traduce cada lote de archivos .po del inglés al español, siguiendo la guía de estilo y el glosario.
  - Revisor (primer filtro): revisa la traducción comparando inglés y español, buscando errores de sentido, de glosario, de registro de los personajes y de formato. En el piloto, esta revisión encontró 9 correcciones menores, todas aplicadas.
  - Corrector: cuando la verificación encuentra cadenas que no caben o tienen errores, ajusta esas cadenas y se relanza solo (máximo 2 intentos).
- **Codex (modelos gpt-6.1-sol y luego gpt-6.2-sol en High, a través del CLI de Codex en una PC con Windows).** Revisor independiente (segundo filtro): revisa congruencia entre lotes, formato, sentido, fidelidad, glosario y español neutro. En el piloto su veredicto fue: traducción natural, tono y glosario correctos, sin errores de naturalidad, de español neutro, de glosario ni de fidelidad; encontró solo 2 incidencias, ambas sobre la posición relativa de los saltos de línea (＿) en dos cadenas; ambas se corrigieron. En la revisión de los lotes, la primera ronda encontró 265 correcciones en 1,350 cadenas (244 de ellas errores de marcadores). Cuando se agotó la cuota semanal de Gemini, Codex asumió también la traducción de los lotes restantes (74, 76–80) y de STARTPOINT (directamente del japonés), leyendo lotes ya traducidos y revisados como referencia para mantener el mismo estilo.
- **ChatGPT (GPT-5, con edición de imágenes).** Redibujó las texturas: el atlas de nombres de hablante, los 13 encabezados del menú del sistema y el logotipo de la enciclopedia, en el mismo estilo del original. Lo que antes se estimaba en horas de trabajo por textura se resolvió en minutos.
- **Adobe Express (quitar fondo).** Limpió los 29 rótulos del atlas recortados de la imagen de ChatGPT, quitando el fondo y el ruido JPEG antes de componer el atlas final.
- **Muse (Bodoque, el asistente de este proyecto).** Coordina la cadena de trabajo: consolida las correcciones de las revisiones, verifica el formato de los .po, reempaqueta los archivos, verifica el resultado y organiza las pruebas. También mantiene la guía de estilo, el glosario y esta documentación.

Qué significa esto en la práctica:

- La traducción es asistida por IA, no 100 % manual. El borrador lo genera la IA; la calidad depende de la cadena de revisiones y de la prueba en juego.
- La revisión final la hace una persona, jugando las escenas traducidas en PPSSPP y reportando lo que ve en pantalla.
- La comunidad también participa: al publicar el parche en foros, quienes jueguen pueden reportar errores de traducción, de formato o de visualización, y esos reportes se corrigen en actualizaciones del parche.
- Si encuentras un error, repórtalo indicando la escena o la frase (una captura ayuda mucho). No se promete una revisión humana completa línea por línea de las 27,466 cadenas; el modelo de calidad de este proyecto es: revisión por IA en dos filtros + consolidación + prueba en juego + reportes de la comunidad.

## 6. Reglas de estilo y calidad

- **Español neutro.** Sin modismos de ningún país (ni mexicanos ni de ninguna otra región). Registro natural y juvenil, acorde a que los personajes son estudiantes de preparatoria.
- **Nombres.** Se conservan exactamente como en el inglés, sin traducir ni adaptar: Ryuuji, Taiga, Minori, Ami, Yacchan, Yuri, Kitamura, Sumire, Sakura, Kota. El orden apellido + nombre se conserva como en el original ("Takasu Ryuuji").
- **"Tiger" → "Tigre".** Es el juego de palabras del original (Taiga suena como "tiger", tigre). Ryuuji llama "Tigre" a Taiga. Por eso, al principio del juego, cuando Ryuuji aún no sabe su nombre, el cuadro de diálogo muestra "Tigre?" y no "Taiga": es el comportamiento original del juego, no un error.
- **Marcadores de formato.** Se preservan tal cual, porque son parte del formato del juego:
  - 「」 delimitan el diálogo (Nombre「texto」).
  - （） (paréntesis de ancho completo) para acotaciones y pensamientos.
  - Puntos suspensivos: se conserva la misma cantidad de puntos que el inglés (...... es una pausa larga; no se reduce a ...).
  - Comillas: las mismas comillas dobles ASCII "..." del inglés (la fuente del juego podría no tener «»).
- **Menús.** "Play Main Story" → "Historia Principal"; "Play Bonus Story" → "Historia Extra". (La primera versión decía "Jugar historia principal" / "Jugar historia extra"; se cambió porque "jugar" es redundante en ese menú.)
- **Saltos de línea (＿).** El carácter ＿ marca el salto de línea dentro del juego. No se copia la posición del inglés: se recalcula para el español. El español es más largo que el inglés y las palabras caen distinto; copiar los cortes del inglés parte palabras a la mitad (se vio "tan/to" y "R/yuuji" en la prueba del piloto) y desborda el cuadro de diálogo. Reglas:
  - El corte cae entre palabras, nunca a mitad de palabra.
  - Cada línea tiene como máximo unos 40 caracteres (el cuadro aguanta unas 3 líneas). **El límite de 40 caracteres cuenta solo el diálogo dentro de 「」, sin el nombre del hablante ni los delimitadores.** Contar el nombre genera correcciones de formato falsas (ver sección 8).
  - Como máximo 3 líneas por diálogo.
  - La traducción se mantiene fiel: si una cadena no cabe en 3 líneas ni con buenos cortes, se marca para revisarla; no se acorta en silencio. No se crea una entrada nueva para el texto que sobra, porque el método in-place no puede insertar entradas sin cambiar los índices y romper el flujo de la escena; en esos casos puntuales se reestructura la traducción para que quepa.
  - Si el cuadro se llena y solo 1 o 2 palabras pasan al cuadro siguiente, se recorta un poco el primer cuadro para que más texto pase al segundo y no quede casi vacío (rebalanceo, solo entre entradas del mismo hablante).
- **Pausa de 72 puntos.** Cinco entradas (_b054ami0–4) tienen en el original un único grupo de 72 puntos suspensivos. Restaurarlo tal cual exigiría una línea de más de 40 caracteres, incompatible con la regla anterior; por eso se mantiene dividido en dos grupos de 36 puntos.
- **Tono.** El prólogo mezcla una secuencia onírica y absurda con una escena emotiva (Ryuuji despierta con amnesia en el hospital). La traducción mantiene la naturalidad del diálogo y el tono lírico del monólogo final ("Hay algo en este mundo que nadie ha visto jamás..."), que es el pasaje icónico de la serie.
- **Términos del glosario.** Christmas Eve → Nochebuena; the 28th → el 28; death ray → rayo mortal; red string → hilo rojo; condo → departamento; earthquake resistant → antisísmico; MOTTAINAI! → ¡QUÉ DESPERDICIO!; "cool" → "genial".

![Batalla del prólogo en español](repack-full/shots/v4-sysmenu-1.png)

*Batalla del prólogo en español (v4, PPSSPP): «¡YURI compró un departamento! ¡Pero no era antisísmico!». La barra de vida muestra «みのり» en kana japonés: es un gráfico, no texto traducible.*

## 7. Historial de versiones

### 7.1 Piloto (el prólogo, escena _0000ESS1: 69 cadenas, 455 palabras)

| Versión | Fecha | Qué cambió | Resultado |
|---|---|---|---|
| Piloto v1 | 17 nov 2026 | Primera construcción con `repack_gpda.py` | **Rota.** Arranca y muestra el título, pero al pulsar New Game se cierra con error (Bad Execution Address, salto a c0ffeeee). Causa: `repack_gpda.py` elimina las tablas de nombres GPDA (ver sección 8.1). |
| Piloto v2 | 17 nov 2026 | Reconstrucción con el método in-place | **Jugable.** Arranca, pasa de New Game sin errores y muestra el prólogo en español, con ñ, ¿, ¡ y los puntos suspensivos correctos. Prueba en juego: palabras partidas a la mitad y texto que se salía por debajo del cuadro de diálogo (saltos de línea copiados del inglés). |
| Piloto v3 | 17 nov 2026 | Saltos de línea recalculados en 22 cadenas del prólogo | Mucho mejor, pero apareció una barra invertida `\` donde debería ir el nombre de un personaje: el parser de .po no era consciente de los escapes y corrompía las comillas. |
| Piloto v4 | 17 nov 2026 | Parser corregido (escape-aware); frases entrecomilladas reparadas; dos segundos cuadros casi vacíos («por ti.» y «ajeno.») reequilibrados | **Aprobada.** El prólogo quedó perfecto y se autorizó traducir el resto del juego con el mismo método. |

Pruebas de formato realizadas con el piloto (PPSSPP en la VM): una 4ª línea NO cabe — se dibuja fuera del cuadro de diálogo, cortada por el borde inferior, y solo se ve la mitad superior de las letras. Una línea de 42 caracteres sí cabe, pero al límite; el límite seguro sigue siendo ~40 caracteres por línea y 3 líneas como máximo. Las entradas largas deben acortarse para caber en 3 líneas, no llevarse a una 4ª.

### 7.2 Juego completo

| Versión | Fecha | Contenido | md5 del ISO |
|---|---|---|---|
| Full v1 | 18 nov 2026 | 300 de 310 escenas en español (método in-place). 10 escenas de diálogo + STARTPOINT no cabían en sus huecos y quedaron en inglés/japonés. 4 textos (ItemList, charaname, placename, utf8) en español, con CRLF corregido tras el fallo de pantalla blanca (ver sección 8.7). | `2db9e6eaf8000bf406292aa59acfb5a6` |
| Full v2 | 18 nov 2026 | Las 10 escenas de diálogo acortadas lo mínimo (184 acortes en 3 rondas) y ya en español. STARTPOINT seguía sin caber (faltaban 526 B). | `cc05dfd97690f36dffe62865a977c2d9` |
| Full v3 | 19 nov 2026 | STARTPOINT en español mediante desplazamiento de 526 B (ver sección 8.9): 310 escenas + títulos de capítulo + sistema, todo en español. El menú de título seguía en inglés. | `1965ef5f5f77c335d02fe706c4ce8d39` |
| Full v4 | 19 nov 2026 | Texto del sistema completo (`utf16.txt.gz`, versión A, 315 líneas): título, opciones, guardar/cargar, Extra, mensajes y canciones en español. Con la v4 el juego quedó 100 % en español en texto plano. | `eaabd086e4ec97f5c7de6d244c770966` |
| Full v5 | 19 nov 2026 | Las 94 correcciones de saltos de línea de la auditoría (ver sección 8.10) aplicadas. | `0993d95d4a1a687d32edce46777d753a` |
| Full v6 | 19 nov 2026 | Títulos de escena (275 únicos, 450 apariciones) + atlas de nombres con TODOS + 13 encabezados del menú del sistema, en español. Verificación binaria perfecta (363/363 escenas, 450/450 títulos, atlas y 13/13 encabezados). Prueba visual en juego: los encabezados y «Regreso a casa» se veían bien, pero las plaquitas de nombre salían mal cortadas y mezcladas con las vecinas (defecto de alineación del atlas redibujado). | `88584bd0656046fa900463ab15e9fe48` |
| **Full v7 (final)** | 19 nov 2026 | Atlas reconstruido celda por celda sobre el original (nombres propios intactos, 29 rótulos limpios con Adobe, 0 motas). Verificación binaria perfecta. Prueba en PPSSPP en la VM (parcial, 27 min) + **prueba en iPhone: va bien, plaquitas un poco más pixeladas pero aceptables, TODOS confirmado en juego**. | `62a5416791fbe20e8896320a830bb90f` |

Todos los ISO miden 1,708,947,456 bytes. Cada versión conserva un respaldo de la anterior antes de construir la siguiente.

### Las 11 escenas que no cabían (full v1 → v2)

El español es más largo que el inglés y los huecos in-place son fijos: 10 escenas de diálogo y STARTPOINT no cabían. La sobra total era de 1,569 B. Se resolvieron 10 con acortes mínimos (184 acortes en 146 entradas de diálogo, en 3 rondas, con el mismo criterio: quitar redundancias sin cambiar el sentido, recalcular los ＿, ≤40 caracteres por línea y ≤3 líneas). La ronda 1 aprobada no bastó: cada carácter eliminado ahorra solo ~0,5 B comprimidos, porque gzip comprime el .obj (UTF-16LE) con mucha eficiencia; hubo que ampliar los acortes con el mismo criterio en las rondas 2 y 3.

| Escena | Sobra original | .obj.gz final / hueco | Margen |
|---|---:|---:|---:|
| _b045not0 | 8 B | 4,095 / 4,096 | 1 B |
| _a043ktm0 | 22 B | 6,140 / 6,144 | 4 B |
| _a050ess0 | 34 B | 4,084 / 4,096 | 12 B |
| _b051yur0 | 45 B | 6,100 / 6,144 | 44 B |
| _0032ed15 | 102 B | 6,114 / 6,144 | 30 B |
| _b050ess0 | 105 B | 4,087 / 4,096 | 9 B |
| _MP_MIN2 | 133 B | 10,226 / 10,240 | 14 B |
| _a193ktm0 | 138 B | 20,480 / 20,480 | 0 B |
| _MP_TIG1 | 143 B | 10,234 / 10,240 | 6 B |
| _c042ami0 | 143 B | 10,238 / 10,240 | 2 B |
| STARTPOINT | 696 B | 14,862 / 14,336 | −526 B (no entraba) |

Lección: la estimación de ahorro debe medirse con un dry-run de recompresión, no estimarse a ojo. El listado completo de los 184 acortes está en `lotes/reporte-acortes-11-escenas.md`.

## 8. Problemas y decisiones

### 8.1 `repack_gpda.py` rompe el juego (piloto v1)

**Problema.** El ISO piloto v1 arrancaba y mostraba el título, pero al pulsar New Game se cerraba con pantalla azul de PPSSPP (Bad Execution Address, salto a c0ffeeee).

**Causa.** `repack_gpda.py` descarta los nombres al leer los GPDA y no escribe la tabla de nombres al reempaquetar (nameOffset=0). Eso encogió las cabeceras y movió todos los archivos 6,144 bytes, dejando obsoleto el seekmap.dat: el juego buscaba `_0000ESS1.dat` en el offset 59,379,712, pero el archivo estaba en 59,373,568, y leía basura.

**Solución.** Método in-place: copiar los archivos originales y sustituir solo los datos modificados en su posición exacta, actualizando únicamente los campos de tamaño y la línea correspondiente del seekmap. El piloto v2, construido así, funcionó. **Lección: extraer bien no equivale a jugar bien; la verificación por extracción no detecta este problema, solo lo detecta jugar.**

### 8.2 Formato .obj y UTF-16LE

**Problema.** Los diálogos viven en archivos .obj binarios con bloques tipados y cadenas en UTF-16LE, con un marcador de salto de línea propio (＿) y títulos de escena en bloques 0x02BC con tamaño fijo.

**Solución.** Se escribió un parser propio, con conversión .obj↔.po, recálculo de saltos y reempaquetado in-place. Los títulos de escena se sustituyen dentro de su bloque, conservando tamaño, sufijo de 6 bytes y relleno cero; si la traducción no cabe en el bloque mínimo, se acorta lo mínimo (40 títulos necesitaron acortamiento; ver anexo A).

### 8.3 El límite de 40 caracteres cuenta solo el diálogo dentro de 「」

**Problema.** En la revisión de los lotes 77/78/80 hubo que revertir 254 correcciones de formato falsas.

**Causa.** El revisor contaba el nombre del hablante y los delimitadores 「」 dentro del límite de 40 caracteres por línea. El juego mide solo el diálogo: en `Noto「Verás, el premio eran dos entradas＿...」` la primera línea mide 34 caracteres, no 39.

**Solución.** La regla quedó escrita en la plantilla del revisor con ese ejemplo, y las 254 correcciones se revirtieron. La verificación automática aplica el mismo criterio.

### 8.4 `rebalancear.py` deshacía correcciones de Codex

**Problema.** El script de rebalanceo movía colas de frase entre entradas vecinas y deshizo correcciones que Codex ya había aplicado: en la ronda 5 deshizo 21 de 22 pares corregidos (42 entradas); en la ronda 4, 13 pares (26 entradas); en las rondas 7 y 8 hubo que restaurar 38 y 2 entradas.

**Causa.** Su regla (entrada B corta + entrada A incompleta → mover la cola a B) contradecía la alineación con el inglés cuando el inglés también parte la frase ahí.

**Solución.** Se restauraron las entradas a la propuesta exacta de Codex y se corrigió el script: una entrada que termina en puntuación + `）` se lee como completa y ya no se le roba la cola. La verificación posterior confirmó 37/37 entradas intactas en los lotes 01–15 y 26/26 restauradas en los lotes 16–20.

### 8.5 Corrupción de comillas por un parser no consciente de los escapes (piloto v3)

**Problema.** En el piloto v3 apareció una barra invertida `\` en pantalla donde debería ir el nombre de un personaje.

**Causa.** El parser de .po no manejaba los escapes de comillas (`\"`): al leer y reescribir, dejaba la barra en el texto que llegaba al juego.

**Solución.** Parser consciente de los escapes y validación con Python propio. El piloto v4, con el parser corregido, quedó aprobado.

### 8.6 La decisión de los 72 puntos (divididos 36+36)

**Problema.** Cinco entradas (_b054ami0–4) tienen en el original un único grupo de 72 puntos suspensivos. Conservarlo como un solo grupo exigiría una línea de más de 40 caracteres; dividirlo parecía romper el original.

**Decisión.** Se mantiene dividido en dos grupos de 36 puntos: las dos reglas (conservar el grupo y limitar la línea a 40 caracteres) son incompatibles en este original, y no se reduce la pausa sin autorización. Es una excepción documentada, no un error.

### 8.7 CRLF frente a LF: pantalla blanca (full v1)

**Problema.** El primer ISO completo arrancaba en pantalla blanca con ~100 errores `Bad memory access` en el log de PPSSPP, mientras el ISO en inglés arrancaba bien.

**Causa (por bisección).** Los textos eran el problema: los originales usan CRLF (`\r\n`) en `utf8.txt`, `ItemList.csv` y `placename.txt` (charaname.txt usa solo LF). Las traducciones usaban solo LF (`\n`) en los 4 archivos, y el parser del juego espera CRLF en esos tres y al no encontrarlo lee mal el archivo.

**Solución.** Reemplazo por bytes `\n` → `\r\n` en los tres archivos (seguro porque `0x0A` nunca es byte de continuación en Shift-JIS ni UTF-8). `charaname.txt` no se tocó (su original es LF). Tras la corrección, el ISO arrancó sin errores. **Lección: al traducir archivos de texto del juego, preservar los finales de línea exactos del original (CRLF frente a LF, por archivo).** La misma regla se aplica a `utf16.txt.gz`: texto UTF-16LE sin BOM, con CRLF y sin CRLF final.

### 8.8 Seekmap y gzip nivel 9

**Problema.** El seekmap recomprimido debe caber en su hueco de 288,768 B en `first.dat`. El nivel 9 de gzip no siempre es el que más comprime.

**Causa.** Para el seekmap original con las 3 sustituciones de STARTPOINT, el nivel 9 producía 289,884 B (1,116 B por encima del hueco) y el nivel 8 producía 282,648 B (cabe). En cambio, para el seekmap de la v2 el nivel 9 daba 288,006 B y sí cabía.

**Solución.** Medir y usar el primer nivel (9, 8, 7, 6…) que quepa, escribiendo el tamaño realmente obtenido en el campo GPDA. No asumir que el nivel 9 siempre comprime mejor. gzip es determinista (nivel 9, mtime=0), así que los tamaños son reproducibles y el build verifica cada escena con `assert len(ogz) <= gap`.

### 8.9 El menú de título: de "probable textura" a `utf16.txt.gz`

**Problema.** Tras aplicar el cambio «Historia Principal» / «Historia Extra» en `_0000ESS1.po`, la pantalla de título seguía mostrando «New Game / Continue / Options / Extra / Install» en inglés. Esas cadenas no son el menú principal.

**Búsqueda.** No estaba en ningún .po, ni en EBOOT.BIN ni BOOT.BIN, ni en first.dat ni en resource.dat como texto plano (ASCII, UTF-16LE ni Shift-JIS). La hipótesis era que fuera una textura.

**Hallazgo.** Codex lo encontró: las cinco opciones viven en `/PSP_GAME/USRDIR/first.dat → text.dat → utf16.txt.gz`, texto UTF-16LE sin BOM, con CRLF, comprimido en un miembro gzip (se genera al construir el parche en inglés). Las líneas 16–20 son New Game / Continue / Options / Extra / Install → Nueva partida / Continuar / Opciones / Extra / Instalar. El gzip en español mide 3,015 B y cabe en el hueco de 4,096 B.

**Consecuencia.** Al revisar ese archivo completo (315 líneas) se descubrió que en la v3 todo el texto del sistema seguía en inglés, no solo el título: opciones, guardar/cargar, instalación de datos, reproductor, galería, menú rápido y títulos de canciones (225 de 315 líneas necesitaban traducción; el resto son dígitos, duraciones y copyright). Se tradujo todo (versión A, canciones incluidas: 16,734 B descomprimidos → gzip 3,155 B, cabe con 941 B libres) y se aplicó en la v4. Con la v4 el juego quedó 100 % en español en texto plano. Detalle crítico de ese archivo: el `_` ASCII (80 en total) es sustituto de espacio dentro de un segmento, mientras que el `＿` fullwidth (34 en total) es el salto de línea y el separador de botones (`Sí＿No`, `Ventana＿Pantalla completa`); no deben confundirse.

### 8.10 STARTPOINT: 526 B de más y el desplazamiento

**Problema.** STARTPOINT (1,359 cadenas: títulos de capítulo y cadenas del sistema, traducidas directamente del japonés) generaba un .obj.gz de 14,862 B frente a un hueco de 14,336 B: faltaban 526 B y el hueco no se podía ampliar.

**Opciones descartadas.** Acortar los títulos: truncar los 338 títulos a ≤28 caracteres solo ahorraba 159 B; cerrar los 526 B exigiría eliminar ~890 caracteres únicos más (~150–250 acortes), deformando visiblemente los títulos, y el coordinador del proyecto rechazó deformarlos. Dejar los títulos más largos en inglés: imposible, porque el parche en inglés nunca tradujo los títulos de capítulo (están en japonés en la versión 1.10); no existen títulos en inglés que dejar. Acortar el mensaje repetido VG_ATTAINMENT_END ahorraba 0 B: gzip lo comprime por back-references.

**Solución (investigación con Codex).** Desplazar 526 B hacia adelante las entradas 1 (`.dat`, 2,048 B, un GPDA vacío válido) y 2 (`.dat.gz`, 40 B) del contenedor GPDA de STARTPOINT, actualizando sus offsets en la tabla GPDA y las 3 líneas correspondientes del seekmap. Quedaban 1,482 B libres antes de la entrada 3. **Riesgo crítico:** los 28,219 registros del seekmap tienen offset múltiplo de 2,048 y los destinos nuevos tienen residuo 526 (no alineados); si el lector del juego truncara offsets a sectores, el plan fallaría.

**Verificación.** Se construyó un ISO de prueba con el desplazamiento (con el .obj.gz español real, 56/56 comprobaciones OK) y se probó en PPSSPP: arranque limpio, logos → título → New Game → cinemática → batalla → diálogo, sin crasheo ni corrupción. **El riesgo de alineación quedó dirimido: el lector del juego acepta los offsets desalineados.** El desplazamiento se aplicó entonces al ISO final (v3). Un error real encontrado en la validación del script: la comprobación de la "palabra alta" del tamaño leía el puntero al nombre en lugar de la palabra alta; Codex devolvió el script corregido antes de construir.

### 8.11 La 4ª línea y la auditoría de saltos (94 correcciones)

**Problema.** En la prueba en iPhone de la v3 aparecía una 4ª línea fuera del cuadro de diálogo, con palabras partidas por la mitad («verdad» → «ver»/«ad», «grande» → «gran»/«de», «resulta» → «result»/«a»). Era crítico.

**Diagnóstico.** El texto cabía; el problema era la colocación de los saltos: tramos de más de 40 caracteres que el juego parte al llegar al límite, dejando un fragmento huérfano en su propia línea y empujando el texto a 4 líneas. No eran `＿` puestos a mitad de palabra (los 3,133 separadores explícitos estaban todos fuera de las palabras).

**Solución.** Auditoría completa con 4 sesiones de Codex en paralelo (lotes 01–20, 21–40, 41–60, 61–80): **22,930 entradas auditadas, 94 fallaban (0,41 %)** — 92 solo necesitaban mover los `＿` sin cambiar ni una palabra, y 2 necesitaron acortamientos mínimos documentados (`_MP_SAK1:293`: «así que» → «conque»; `_a042ess0:205`: «consejo estudiantil» → «consejo»). Ninguna necesitaba la segunda ventana de texto. Las 94 correcciones se aplicaron y verificaron (msgid intactos, ≤40 caracteres, ≤3 líneas) y se construyó la v5. Las 3 entradas de las capturas quedaron cubiertas y corregidas.

### 8.12 Texturas: EVERYONE, títulos de escena y Extras

**Problema.** En la prueba en iPhone de la v5 quedaba texto en inglés en imágenes: la etiqueta de hablante «EVERYONE» (cuyo texto «Todos» ya existía traducido en los archivos), títulos de escena como «Homecoming» y las pantallas de Extras.

**Investigación (Codex).** EVERYONE está dibujado 3 veces en el atlas `sg_chaname.gim` (512×384, celdas de 108×28); SYSTEM MENU y otros 12 encabezados son texturas `sg_title01–13.gim.gz` en `first.dat`; los títulos de escena son texto en bloques 0x02BC. El censo completo recorrió los 363 .obj.gz: **450 apariciones, 275 títulos únicos** (no 254: la primera estimación solo muestreó 209 archivos y encontró 64 títulos posteriores; el recorrido completo encontró 84). No quedaba ningún otro texto plano en inglés fuera de los bloques 0x02BC y los conjuntos ya traducidos. La enciclopedia sí lee el `ItemList.csv` ya traducido (solo su logotipo y su miniatura seguían en japonés).

**Aplicación (v6).** Los 275 títulos se tradujeron a español neutro (40 se acortaron lo mínimo para caber en su bloque; ver anexo A); 363/363 escenas procesadas y todas caben. El atlas se redibujó completo con ChatGPT (gzip 74,937 B en hueco de 75,776 B) y los 13 encabezados se convirtieron con la paleta original (todos caben en sus slots de 4,096 B). Verificación binaria perfecta: 363/363 escenas, 450/450 títulos, atlas byte-idéntico, 13/13 encabezados, 0 fallos.

**El fallo de la v6 y su arreglo (v7).** En el juego, las plaquitas de nombre salían mal cortadas y mezcladas con las etiquetas vecinas («TODOS» traía un «?» pegado, «YACCHAN» doble). Causa: el redibujo completo del atlas en ChatGPT no quedó alineado con las celdas fijas de 108×28 que recorta el juego; cada plaquita agarraba pedazos de la etiqueta vecina. La verificación de la v6 solo había revisado la imagen completa decodificada, no los recortes por celda como los dibuja el juego: ese era el hueco de verificación.

![Fallo de la v6: TODOS con un «?» pegado de la etiqueta vecina (captura de iPhone, v6)](documentacion-pdf/.src/media/todos-v6-fallo.jpg)

*Fallo de la v6 en juego (iPhone): la plaquita «TODOS» trae un «?» pegado de la etiqueta vecina. Es la v6 rota, no la v7.*

**Solución (v7).** Rehacer el atlas celda por celda sobre el atlas original: los 28 nombres propios quedan pixel-perfect y solo se reemplazan las 29 etiquetas genéricas, recortadas de la imagen de ChatGPT y limpiadas una por una con Adobe Express (quitar fondo), para eliminar el ruido JPEG. Comparación por celda como puerta obligatoria antes de construir: **0 motas aisladas en las 29 celdas** (la versión ruidosa tenía 572; el original, 0), 0 píxeles distintos fuera de las 29 celdas, gzip 62,818 B en hueco de 75,776 B (margen 12,958 B). Decisiones aplicadas: C04/C05 quedan como «COMPAÑERO?», C10 como «COMPAÑERO», C28 como «JUNIOR» y C44 como «¡¿YO?!» (texto de la v6 tal cual, sin otra ronda de ChatGPT); C49 SEÑORA y C51 ANFITRIÓN quedan más pequeños que sus vecinos, como se aceptó.

![Atlas v7 limpio, decodificado: TODOS ×3 en la fila 5](documentacion-pdf/.src/media/atlas-v7.png)

*Atlas de nombres v7 decodificado (lo que dibuja el juego): TODOS ×3 en la quinta fila, y los 28 nombres propios intactos.*

![Plaquita RYUUJI en juego, v7 (PPSSPP)](documentacion-pdf/.src/media/plaquita-ryuuji.png)

*Plaquita «RYUUJI» limpia en juego (v7, PPSSPP, prólogo del hospital, 12/28). Las plaquitas de nombre propio se ven perfectas en juego.*

### 8.13 Extras descartados

**Decisión.** Toda la parte de Extras se dejó como está, por decisión expresa: no se toca nada de Extras en la ISO final — ni los minijuegos (Rampage! Palmtop Tiger, Dress Up Breakout, juego de memoria), ni los globos del selector («¡Date prisa en desbloquearlo, FLOJO!!» y «Aquí no hay nada», que ChatGPT ya había devuelto traducidos en una hoja de contacto), ni el logotipo ni la miniatura de la enciclopedia. El trabajo estimado para los Extras era de 26–48 horas de edición y validación, con ayudas completas, tablas de controles, 16 frases de Taiga en el ejecutable y arte de 58 objetos; no entraba en el alcance. La lista interactiva de la enciclopedia sí está en español, porque lee el `ItemList.csv` traducido; solo su imagen de vista previa sigue en japonés.

### 8.14 Las pruebas de ChatGPT (texturas)

Sam probó directamente la edición de imágenes con ChatGPT: el atlas de nombres (EVERYONE → TODOS y ~25 rótulos genéricos), los 13 encabezados del menú del sistema (SYSTEM MENU, SAVE, LOAD, etc.) y el logotipo de la enciclopedia salieron correctos y en el mismo estilo. Redibujar una textura llevó minutos, no las horas estimadas antes, así que el trabajo de texturas dejó de ser el cuello de botella. La segunda hoja de contacto (con un prompt en inglés más específico: mayúsculas obligatorias, letra angosta y angulosa) también salió usable, pero la decisión final fue recortar los rótulos de la primera imagen de ChatGPT (la de la v6, la más cercana al estilo original) y limpiarlos con Adobe, en lugar de usar la segunda hoja.

### 8.15 Reparación de PPSSPP en la VM

**Problema.** La prueba visual de la v6 no pudo completarse en la VM: PPSSPP no arrancaba — «Unable to initialize SDL: Could not setup connection to PulseAudio» (no había demonio PulseAudio instalado), no existía `/dev/fuse` (el AppImage no montaba) y el binario directo hacía segfault.

**Solución.** PulseAudio ya estaba instalado tras un `apt update` (el «sin candidato» anterior era por listas de paquetes desactualizadas). `/dev/fuse` sigue sin existir, así que se usa el AppImage extraído (`AppDir/AppRun`), no el AppImage montado. Receta tras un reemplazo de VM: `sudo apt update && sudo apt install -y pulseaudio xvfb xdotool imagemagick`, extraer el AppImage con `--appimage-extract`, arrancar Xvfb :99 y PulseAudio, y lanzar PPSSPP con `LIBGL_ALWAYS_SOFTWARE=1`. Los paquetes de la VM no sobreviven a un reemplazo: hay que reinstalarlos. Limitaciones conocidas: el arranque es lento (~2 min hasta los logos y ~4–5 min de opening, ~7 min hasta el título, en render por software) y el opening no se salta con teclado en esa sesión.

### 8.16 Tope de 30 minutos de pruebas

**Decisión.** Las pruebas no deben pasar de 30 minutos en total. Una prueba anterior de PPSSPP duró 2 h 40 min, muchísimo. Consecuencias: en la v6 la prueba se detuvo a los ~25 minutos sin completar la verificación visual (quedó para el playtest en iPhone); en la v7 la prueba duró 27 minutos y llegó hasta la entrada #55 del prólogo, sin alcanzar la #62 donde aparece TODOS (quedó para el playtest en iPhone, que lo confirmó). En PPSSPP no se puede cargar o saltar a una escena concreta, así que el método acordado es verificación binaria de todos los títulos más vistazos visuales a unas pocas escenas clave.

### 8.17 Formato del parche: xdelta3

**Decisión.** El parche se distribuye como **xdelta3 dentro de un zip**, aplicado sobre la ISO del juego **con el parche en inglés v1.10 ya aplicado** (no sobre la ISO japonesa original), porque esa es la ISO de la que parte la traducción en español. Solo se distribuye el parche, nunca la ISO. El parche irá acompañado de un README con las instrucciones para aplicarlo.

### 8.18 Publicación: sin mención a los autores del parche en inglés

**Decisión.** Los autores del parche en inglés pidieron expresamente no ser mencionados ni asociados a este proyecto, y así se hace: no se les acredita ni se enlaza su trabajo en ningún sitio. El parche solo indica que se parte de la ISO con el parche en inglés v1.10 ya aplicado. Las comunidades previstas son Romhack Plaza y Romhack.ing para alojar el parche, el Discord de Toradora, Fuwanovel, r/Toradora, r/visualnovels, r/PSP, r/romhacking, GBAtemp, ClanDLAN y ElOtroLado, además de registrarlo en VNDB.

### 8.19 Manual del juego

El juego traía un manual físico de papel (inserto del UMD), que no está en la ISO. No se encontró ningún escaneo digital público del manual original japonés; traducirlo exigiría comprar una copia física desde Japón (unos 6–25 USD más envío), y se decidió no comprarlo. El tema queda aparcado: se retomará solo si aparece una copia digital.

## 9. Verificación y pruebas

| Versión | Verificación binaria | Prueba en PPSSPP (VM) | Prueba en iPhone |
|---|---|---|---|
| Piloto v2 | .obj válido (246 bloques, 69 cadenas, caracteres españoles) | Arranca, prólogo en español | — |
| Piloto v4 | — | — | Aprobada: prólogo perfecto |
| Full v1 | Round-trip pycdlib; 11 escenas omitidas verificadas byte-idénticas al original (22/22 blobs) | Arranque limpio, batalla y diálogo en español; título en inglés (esperado) | — |
| Full v3 (shift) | 56/56 comprobaciones del script de desplazamiento | Arranque limpio, prólogo completo en español, 0 errores reales | Prueba: 4ª línea fuera del cuadro (ver 8.11); problema de I/O en el primer arranque (ver 10) |
| Full v4 | 20/20 comprobaciones | Título, menú del sistema, opciones, guardado, confirmaciones y batalla en español | — |
| Full v5 | 310/310 escenas caben (dry-run); STARTPOINT desplazado | Arranque limpio; entrada #67 («resulta») verificada en 3 líneas limpias | Prueba: mucho mejor; quedaba texto en inglés en texturas y títulos (ver 8.12) |
| Full v6 | 363/363 escenas, 450/450 títulos, atlas byte-idéntico, 13/13 encabezados, 0 fallos | No completada por el entorno (sin PulseAudio, sin /dev/fuse, segfault) | Encabezados y «Regreso a casa» bien; plaquitas mal cortadas (ver 8.12) |
| **Full v7** | 363/363 escenas, 450/450 títulos, atlas byte-idéntico al limpio, 13/13 encabezados, 0 fallos; solo cambió el atlas respecto a la v6 | Parcial (27 min): título y prólogo en español; plaquitas RYUUJI/TAIGA/??? perfectas; TODOS (#62) no se alcanzó (se llegó a #55) | **Va bien; plaquitas un poco más pixeladas pero aceptables; TODOS confirmado en juego** |

![Menú del sistema en español en iPhone (v6): «MENÚ DEL SISTEMA» y «Regreso a casa»](documentacion-pdf/.src/media/menu-sistema-iphone.jpg)

*Menú del sistema en español en iPhone (v6): encabezado «MENÚ DEL SISTEMA», «Guardar / Cargar / Guardado rápido / Carga rápida / Opciones / Salir» y título de escena «Regreso a casa», con lugar y BGM en español.*

Pendientes menores conocidos (no bloquean la v7): en Opciones, las etiquetas largas en español («Velocidad de mensaje», «Transparencia de la caja», «Marcar elecciones pasadas») quedan parcialmente tapadas por la barra verde de valores; es cosmético y se entiende. La pantalla de Cargar no se verificó directamente en la VM (la de Guardar y la entrada «Cargar» sí, y usan las mismas cadenas de ranura).

## 10. Cómo jugar

**Requisitos.** Tu propia copia del juego con el parche en inglés v1.10 ya aplicado, y el parche en español (xdelta3 en zip) aplicado sobre ella. El parche no incluye el juego ni sus archivos.

**Recomendación para jugar en PPSSPP (iOS).** En iPhone, el primer arranque del juego puede cerrarse solo justo después del aviso de la Memory Stick si el método de sincronización de E/S está en "Rápido". Es un problema de temporización de lectura del emulador en el primer arranque, no del parche: la ISO estaba completa y la compilación verificada, y el juego arranca bien en PPSSPP de PC.

- **Antes del primer arranque:** en PPSSPP, Ajustes → Sistema → "Método de sincronización de E/S" → **"Simular retraso del UMD"**.
- **Después de que el juego haya arrancado bien una vez**, se puede volver a poner en "Rápido" y sigue cargando sin problema.

Observado con la versión v5 en iPhone 16 Pro (PPSSPP de App Store).

**«Install» (opción del título).** Es la función de instalación de datos de PSP: copia parte de los datos del juego al Memory Stick™ para que las cargas sean más rápidas. Necesita 407 MB libres (+ 2.272 KB para guardados) y tarda unos 4 minutos. No es obligatorio para jugar.

## 11. Cómo reportar errores

Si juegas el parche y encuentras un error (de traducción, de formato o de visualización), repórtalo con la escena o la frase exacta y, si puedes, una captura de pantalla. Indica también la versión del parche que estás usando.

## 12. Notas legales

- Este proyecto distribuye únicamente el parche en español (los archivos .po traducidos y las instrucciones para aplicarlo). Nunca se distribuye la ISO del juego, ni la original ni la ya parcheada.
- Para jugar con el parche en español necesitas tu propia copia del juego (idealmente, volcada de tu propio UMD). El parche no incluye el juego ni sus archivos.
- Toradora! Portable es un juego comercial de Bandai Namco (2009, solo Japón), sin localización oficial en inglés ni en español.
- La traducción al español parte de la ISO con el parche en inglés v1.10 ya aplicado. Este proyecto distribuye solo el trabajo nuevo en español (sin incluir texto en inglés ni recursos del juego). Los autores del parche en inglés pidieron no ser mencionados ni asociados a este proyecto, y así se hace.
- Es un proyecto de fans, sin fines comerciales.
- Este documento no es asesoría legal; resume la práctica habitual en la escena de fan translations.

## 13. Créditos

- Kit de retraducción TigerXDragon: SH4FS0c13ty (licencia MIT).
- Emulador PPSSPP: equipo de PPSSPP.
- Traducción al español, coordinación y control de calidad: @Sam-Bks, con ayuda de Muse (Bodoque).

*Documento elaborado el 19 de noviembre de 2026. El contenido describe el método y las herramientas del proyecto; no incluye el juego ni sus archivos.*

## Anexo A. Los 40 acortamientos de títulos de escena

Primera pasada de traducción: 40 títulos no cabían en su bloque mínimo y se acortaron lo mínimo (segunda pasada: 2 seguían sin caber y se acortaron de nuevo). Resultado final: 0 fuera de límite.

| Título en inglés | Primera propuesta (no cabía) | Versión final |
|---|---|---|
| A Dog's Dream | El sueño de un perro | Sueño de perro |
| A Midwinter Ghost Story | Historia de fantasmas en invierno | Fantasmas en pleno invierno |
| All the Feels | Todos los sentimientos | Puro sentimiento |
| Battle of Taiga's Lair | La batalla en la guarida de Taiga | Batalla en la guarida de Taiga |
| Beyond the Chilly Night | Más allá de la noche fría | Tras la noche fría |
| Bonds 50cm Apart | Lazos a 50 cm de distancia | Lazos a 50 cm |
| Exploring Oohashi HS | Explorando el inst. Oohashi | Explorando Oohashi |
| Fading Misfortune | La desgracia se desvanece | La desgracia se va |
| Fractured Heart | Corazón fracturado | Corazón roto |
| Fried Rice Penance | Penitencia de arroz frito | Penitencia de arroz |
| Get a Big Bro! | ¡Consigue un hermano mayor! | ¡Hermano mayor! |
| How Many Coins? | ¿Cuántas monedas? | Cuántas monedas? (sin ¿ inicial, para caber) |
| Kitamura's Strategy | La estrategia de Kitamura | Estrategia de Kitamura |
| Midnight SOS | SOS de medianoche | SOS medianoche |
| Morning of Opening Ceremony | Mañana de la ceremonia de apertura | Mañana de la apertura |
| Near, Yet Far | Cerca, pero lejos | Cerca y lejos |
| RE:Legendary Showdown | RE:Enfrentamiento legendario | RE:Duelo legendario |
| Return March | Marcha de regreso | Marcha de vuelta |
| Road to Truth | Camino a la verdad | Hacia la verdad |
| Sensibly Unlucky | Sensatamente desafortunado | Desafortunado sensato |
| Showdown Morning | Mañana del enfrentamiento | Mañana del duelo |
| Spirit Capture Plan | Plan de caza de espíritus | Caza de espíritus |
| Strategy Meeting, Take Two | Reunión de estrategia, segunda toma | Estrategia, toma dos |
| Student Council Dog | Perro del consejo estudiantil | Perro del consejo |
| Taiga's Room...... | Habitación de Taiga...... | Cuarto de Taiga...... |
| Taiga's Wish | El deseo de Taiga | Deseo de Taiga |
| Testing Ami | Poner a prueba a Ami | Probando a Ami |
| Testing Haruta | Poner a prueba a Haruta | A prueba Haruta |
| Testing Haruta's Courage | Poner a prueba el valor de Haruta | Probando el valor de Haruta |
| Testing Minori | Poner a prueba a Minori | A prueba Minori |
| Testing My Courage! | ¡Poner a prueba mi valor! | ¡Probando mi valor! |
| The Armband's True Meaning | El verdadero significado del brazalete | El significado del brazalete |
| The Evil SC President | La malvada presidenta del consejo | La malvada presidenta |
| The New Semester Begins | Comienza el nuevo semestre | Comienza el semestre |
| True Nature | Verdadera naturaleza | Naturaleza real |
| Unnoticed Feelings | Sentimientos inadvertidos | Sentimientos ocultos |
| Visibly Unlucky | Visiblemente desafortunado | Mala suerte visible |
| We're the Same As Ever | Somos los mismos de siempre | Iguales que siempre |
| Where The Feelings Are | Donde están los sentimientos | Donde los sentimientos |
| Year-End Crisis | Crisis de fin de año | Crisis anual |

Decisiones puntuales: «Homecoming» → «Regreso a casa»; «Sumire the Scout» → «Sumire la vigía»; «Pursuit of Taiga» → «Tras Taiga»; «Just One Feeling» → «Un sentimiento»; «Handle With Care» → «Con cuidado»; «Bad Luck Can't Be Proven» → «Mala suerte sin pruebas»; STARTPOINT → «Inicio». La tabla completa de los 275 títulos (inglés → español, con escena de primera aparición) está en `investigacion-texturas/titulos-es.json` y en `investigacion-texturas/reporte-titulos-escena.md`.

## Anexo B. Los 13 encabezados del menú del sistema

| Archivo | Texto original | Tamaño gzip / hueco |
|---|---|---:|
| sg_title01 | SYSTEM MENU | 3,717 / 4,096 B |
| sg_title02 | SAVE | 2,584 / 4,096 B |
| sg_title03 | LOAD | 2,344 / 4,096 B |
| sg_title04 | QUICK SAVE | 3,749 / 4,096 B |
| sg_title05 | QUICK LOAD | 3,233 / 4,096 B |
| sg_title06 | OPTIONS | 2,725 / 4,096 B |
| sg_title07 | ITEM LIST | 3,408 / 4,096 B |
| sg_title08 | CG ALBUM | 2,537 / 4,096 B |
| sg_title09 | MUSIC | 2,423 / 4,096 B |
| sg_title10 | BACKLOG | 2,882 / 4,096 B |
| sg_title11 | EXTRA | 2,343 / 4,096 B |
| sg_title12 | DATA INSTALL | 3,714 / 4,096 B |
| sg_title13 | ENCYCLOPEDIA | 2,652 / 4,096 B |

Los 13 encabezados se redibujaron en español con ChatGPT y se convirtieron cuantizando a la paleta original de cada uno; «MENÚ DEL SISTEMA» (sg_title01) y «ENCICLOPEDIA» (sg_title13) se verificaron visualmente por decodificación, y los 13 se vieron en juego en la prueba de iPhone de la v6 (el encabezado «MENÚ DEL SISTEMA» se ve en la captura de la sección 9).
