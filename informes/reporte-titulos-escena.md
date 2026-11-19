# Títulos de escena + títulos de textura — ISO v6

**Fecha:** 19 nov 2026 (madrugada, trabajo nocturno autorizado por Sam).
**ISO v6:** `toradora-portable-ES-v6.iso` — **md5 `88584bd0656046fa900463ab15e9fe48`** (1,708,947,456 B).
**ISO v5 intacto:** `toradora-portable-ES.iso` — md5 `0993d95d4a1a687d32edce46777d753a` (NO se tocó).
**Alcance:** solo títulos de escena (275 únicos) + títulos de textura (atlas + 13 headers). Extras DROPPED por Sam — no se tocó nada de Extras. No se tocaron los .po de diálogo, STARTPOINT.po, utf16 ni las 4 listas de texto.

---

## 1. Censo de títulos de escena (v5)

Script: `censo-titulos-v5.py`. Recorrió los **363 .obj.gz** de `repack-full/resource-v5.dat` (offsets de `seekmap.txt`, tamaños actuales del campo GPDA en contenedor+24).

- **450 apariciones** de bloques 0x02BC, **275 títulos ÚNICOS** — no 254.
- **Reconciliación con la estimación de 254:** 191 únicos INICIALES (190 EN + el japonés 'スタートポイント' de STARTPOINT) + **84 únicos en bloques POSTERIORES** (no 64). La investigación previa solo muestreó 209 .obj del delta EN y encontró 64 posteriores; el recorrido completo de v5 encontró 20 más. 0 escenas sin título; 0 errores.
- Cruce con EN: **0 discrepancias** en los títulos iniciales vs `titulos-escena.json`.
- Escena con más títulos: `_a193ktm0` (8), `_b192min0` (7), `_b292ami0` (6).
- Tamaños de bloque: 64 B ×210, 80 B ×94, 48 B ×77, 32 B ×53, 96 B ×14, 112 B ×2. Sufijos: `000001000000` ×397, `000000000000` ×53. Relleno cero.
- **Límite por bloque** (unidades = (tamaño−16)/2): 32 B→8u; 48 B→16u; 64 B→24u; 80 B→32u; 96 B→40u; 112 B→48u. El título más largo EN: 'That Morning, in the Student Council Room' (41 caracteres, bloque 112 B, máx 48u).

Archivos: `titulos-escena-v5.json`, `titulos-unicos-v5.txt`, `titulos-para-traducir.json`.

### Decisiones ya tomadas para títulos ajustados
- STARTPOINT → **"Inicio"** (6 caracteres, cabe en 8u; agrandar el bloque exigiría más shifting: su .obj.gz ya mide 14,862 B, por encima del hueco original de 14,336 B).
- 'Sumire the Scout' → "Sumire la vigía" (16u). 'Pursuit of Taiga' → "Tras Taiga" (10u). 'Just One Feeling' → "Un sentimiento" (14u). 'Handle With Care' → "Con cuidado" (11u). "Bad Luck Can't Be Proven" → "Mala suerte sin pruebas" (24u). 'Homecoming' → **"Regreso a casa"** (14u).

---

## 2. Traducción (275 títulos, español neutro)

Script: `traducir-titulos.py` (valida que cada traducción quepa en su bloque MÍNIMO). Tabla JSON: `titulos-es.json`.

- **275/275 traducidos, 0 faltantes, 0 sobrantes.**
- Primera pasada: **40 traducciones NO cabían** en el bloque mínimo → se acortaron (decisión autónoma, siguiendo el precedente de Sam de "acortar lo mínimo" para las 11 escenas). Segunda pasada: 2 seguían sin caber → se acortaron de nuevo.
- **Resultado final: 0 traducciones fuera de límite.**

### Los 40 acortamientos (EN → primera propuesta → versión final que cabe)
| EN | Primera propuesta (no cabía) | Final |
|---|---|---|
| A Dog's Dream | El sueño de un perro (20>16u) | Sueño de perro |
| A Midwinter Ghost Story | Historia de fantasmas en invierno (33>32u) | Fantasmas en pleno invierno |
| All the Feels | Todos los sentimientos (22>16u) | Puro sentimiento |
| Battle of Taiga's Lair | La batalla en la guarida de Taiga (33>32u) | Batalla en la guarida de Taiga |
| Beyond the Chilly Night | Más allá de la noche fría (25>24u) | Tras la noche fría |
| Bonds 50cm Apart | Lazos a 50 cm de distancia (26>24u) | Lazos a 50 cm |
| Exploring Oohashi HS | Explorando el inst. Oohashi (27>24u) | Explorando Oohashi |
| Fading Misfortune | La desgracia se desvanece (25>24u) | La desgracia se va |
| Fractured Heart | Corazón fracturado (18>16u) | Corazón roto |
| Fried Rice Penance | Penitencia de arroz frito (25>24u) | Penitencia de arroz |
| Get a Big Bro! | ¡Consigue un hermano mayor! (27>16u) | ¡Hermano mayor! |
| How Many Coins? | ¿Cuántas monedas? (17>16u) | Cuántas monedas? (sin ¿ inicial, para caber) |
| Kitamura's Strategy | La estrategia de Kitamura (25>24u) | Estrategia de Kitamura |
| Midnight SOS | SOS de medianoche (17>16u) | SOS medianoche |
| Morning of Opening Ceremony | Mañana de la ceremonia de apertura (34>32u) | Mañana de la apertura |
| Near, Yet Far | Cerca, pero lejos (17>16u) | Cerca y lejos |
| RE:Legendary Showdown | RE:Enfrentamiento legendario (28>24u) | RE:Duelo legendario |
| Return March | Marcha de regreso (17>16u) | Marcha de vuelta |
| Road to Truth | Camino a la verdad (18>16u) | Hacia la verdad |
| Sensibly Unlucky | Sensatamente desafortunado (26>24u) | Desafortunado sensato |
| Showdown Morning | Mañana del enfrentamiento (25>24u) | Mañana del duelo |
| Spirit Capture Plan | Plan de caza de espíritus (25>24u) | Caza de espíritus |
| Strategy Meeting, Take Two | Reunión de estrategia, segunda toma (35>32u) | Estrategia, toma dos |
| Student Council Dog | Perro del consejo estudiantil (29>24u) | Perro del consejo |
| Taiga's Room...... | Habitación de Taiga...... (25>24u) | Cuarto de Taiga...... |
| Taiga's Wish | El deseo de Taiga (17>16u) | Deseo de Taiga |
| Testing Ami | Poner a prueba a Ami (20>16u) | Probando a Ami |
| Testing Haruta | Poner a prueba a Haruta (23>16u) | A prueba Haruta |
| Testing Haruta's Courage | Poner a prueba el valor de Haruta (33>32u) | Probando el valor de Haruta |
| Testing Minori | Poner a prueba a Minori (23>16u) | A prueba Minori |
| Testing My Courage! | ¡Poner a prueba mi valor! (25>24u) | ¡Probando mi valor! |
| The Armband's True Meaning | El verdadero significado del brazalete (38>32u) | El significado del brazalete |
| The Evil SC President | La malvada presidenta del consejo (33>32u) | La malvada presidenta |
| The New Semester Begins | Comienza el nuevo semestre (26>24u) | Comienza el semestre |
| True Nature | Verdadera naturaleza (20>16u) | Naturaleza real |
| Unnoticed Feelings | Sentimientos inadvertidos (25>24u) | Sentimientos ocultos |
| Visibly Unlucky | Visiblemente desafortunado (26>24u) | Mala suerte visible |
| We're the Same As Ever | Somos los mismos de siempre (27>24u) | Iguales que siempre |
| Where The Feelings Are | Donde están los sentimientos (28>24u) | Donde los sentimientos |
| Year-End Crisis | Crisis de fin de año (20>16u) | Crisis anual |

Notas: "MOTTAINAI! Food" → "¡Qué desperdicio! Comida". "Yuri-chan's Hint #N" → "Pista de Yuri-chan #N" (21 pistas). "Tiger" → "Tigre". Nombres como en EN. Elipsis conservadas.

### Tabla completa (275 títulos EN → ES, con escena de primera aparición)
| EN | ES | Primera escena |
|---|---|---|
| "Outsider" Buried in the Past | Forastero enterrado en el pasado | _b292ami0 |
| "That" Feeling | Ese sentimiento | _0013MIN0 |
| A Close Encounter | Un encuentro cercano | _0011AMI0 |
| A Date with Ami-chan | Una cita con Ami-chan | _b280ess0 |
| A Distant Promise | Una promesa lejana | _c054ktm0 |
| A Dog's Dream | Sueño de perro | _a040ess0 |
| A Midwinter Ghost Story | Fantasmas en pleno invierno | _b055ess0 |
| A Morning Unlike Any Other | Una mañana como ninguna otra | _b050ess0 |
| A New World | Un mundo nuevo | _b292ami0 |
| A Suspicious Look | Una mirada sospechosa | _a361ktm0 |
| Afternoon Free Time | Tiempo libre en la tarde | _b052ess0 |
| All the Feels | Puro sentimiento | _a162ess0 |
| Amazingly, The Gang's All Here! | ¡Increíble, están todos aquí! | _b051ami0 |
| Ami's Anger | La ira de Ami | _a361ami0 |
| Ami's Invitation | La invitación de Ami | _0031ami0 |
| And Inko-chan...... | E Inko-chan...... | _MP_INK5 |
| At Last, the Reunion | Por fin, el reencuentro | _a262ess0 |
| Bachelorette's Insurance | El seguro de soltera | _a192yur0 |
| Bad Luck Begins | Comienza la mala suerte | _d010ess0 |
| Bad Luck Can't Be Proven | Mala suerte sin pruebas | _d013ess0 |
| Battle Mode Tiger | Tigre en modo batalla | _c054ktm0 |
| Battle of Taiga's Lair | Batalla en la guarida de Taiga | _c065ktm0 |
| Before Showtime | Antes del espectáculo | _a161ami0 |
| Beyond the Chilly Night | Tras la noche fría | _c067ess0 |
| Biggest Shock Ever (I Think) | El mayor susto (creo) | _c057ess0 |
| Bishamontengoku | Bishamontengoku | _0022yas0 |
| Bonds 50cm Apart | Lazos a 50 cm | _c072ami0 |
| Boy's Desire, Girl's Ambition | Deseo de chico, ambición de chica | _c061sak0 |
| Bridge to Desire | Puente al deseo | _c065ktm0 |
| Bro Mode OK | Modo hermano OK | _c061har0 |
| Broken Buddies | Amigos rotos | _a193ktm0 |
| But Inko-chan...... | Pero Inko-chan...... | _MP_INK7 |
| Candy Generation | Generación de dulces | _c064ami0 |
| Chaos and Rebirth | Caos y renacimiento | _c044ess0 |
| Choosing Friendship | Elegir la amistad | _a051ami0 |
| Complicated | Complicado | _0035yas0 |
| Confession | Confesión | _a193ktm0 |
| Connection | Conexión | _c056yas0 |
| Conveying Happiness | Transmitir felicidad | _d021sak0 |
| Culture Festival Memories | Recuerdos del festival cultural | _0022not0 |
| Cupid is Born | Nace Cupido | _a052tig0 |
| Date with a Goddess | Cita con una diosa | _0032ed10 |
| Dearly Beloved | Queridísimos | _a050ess0 |
| Decision Before the Test | Decisión antes del examen | _b065ess0 |
| Did She Fall? | ¿Se cayó? | _b062tig0 |
| Did You Forget? | ¿Lo olvidaste? | _0022ami0 |
| Do You Believe in Ghosts? | ¿Crees en fantasmas? | _b055ess0 |
| Drowning | Ahogándose | _c051yur0 |
| EMERGENCY! | ¡EMERGENCIA! | _a162ess0 |
| Emotion Overload | Sobrecarga de emociones | _MP_TIG2 |
| Encounter at the New Year's Sale | Encuentro en las rebajas de Año Nuevo | _b041koh0 |
| Enemy of My Enemy | Enemigo de mi enemigo | _c042sak0 |
| Entrusting Happiness | Confiar la felicidad | _d021tig0 |
| Eve of Operation | Víspera de la operación | _a056ess0 |
| Exploring Oohashi HS | Explorando Oohashi | _0021ktm6 |
| Fading Misfortune | La desgracia se va | _d013ess0 |
| Family | Familia | _c051tig0 |
| Fancy That | Vaya | _0031not0 |
| Fated Encounter | Encuentro predestinado | _a362yur0 |
| Feelings Left Behind | Sentimientos abandonados | _b191tig0 |
| Finding Feelings | Encontrar sentimientos | _MP_MIN3 |
| For Inko-chan...... | Para Inko-chan...... | _MP_INK6 |
| For Whom the Bell Tolls | Por quién doblan las campanas | _a364ed10 |
| For Your Sake | Por ti | _a045ess0 |
| Forget the Shrine, Pray To Me | Olvida el santuario, reza a mí | _b041ktm0 |
| Forms of Happiness | Formas de felicidad | _c072min0 |
| Fortune Comes | Llega la fortuna | _a043not0 |
| Fractured Heart | Corazón roto | _a192ami0 |
| Fried Rice Penance | Penitencia de arroz | _b061tig0 |
| Friends | Amigos | _0013MIN0 |
| Game Set | Juego terminado | _c072min1 |
| Get a Big Bro! | ¡Hermano mayor! | _a055sum0 |
| Ghost Hunters | Cazafantasmas | _b170ed30 |
| God of Heartbreak, Hear Me Roar | Dios del desamor, escucha mi rugido | _c071ktm0 |
| Goddess of Love | Diosa del amor | _MP_AMI2 |
| Goodbye | Adiós | _b192min0 |
| Gunma, The Distant Land | Gunma, la tierra lejana | _c053har0 |
| Guy Gone Wild | Chico desatado | _a052tig4 |
| Handle With Care | Con cuidado | _c042not0 |
| Happily Married | Felizmente casados | _a364ed10 |
| Happy New... EMPTY!? | Feliz Año... ¡¿VACÍO?! | _b040ess0 |
| Haruta is Haruta | Haruta es Haruta | _0031har0 |
| Hatsumode For Two | Hatsumode para dos | _0024ess0 |
| Her 30th New Year | Su trigésimo Año Nuevo | _a041yur0 |
| Her Duty | Su deber | _a055sak0 |
| Her and Her | Ella y ella | _a190ess0 |
| Highest of Praise | El mayor elogio | _0011KTM0 |
| His Sudden Illness | Su repentina enfermedad | _a160ess0 |
| Homecoming | Regreso a casa | _0010ESS0 |
| How Many Coins? | Cuántas monedas? | _b293ed25 |
| How to Spend New Year's Single | Cómo pasar Año Nuevo soltero | _b051yur0 |
| Hurry Into Space | De prisa al espacio | _a292ed10 |
| If We're All Together | Si estamos todos juntos | _0033min0 |
| Incoming | Entrante | _c050ess0 |
| Incurable | Incurable | _c041har0 |
| Inko-chan AWOL | Inko-chan desaparecida | _a360ess0 |
| Inko-chan Has...... | Inko-chan tiene...... | _MP_INK8 |
| Inko-chan is...... | Inko-chan es...... | _MP_INK4 |
| Inko-chan's...... | De Inko-chan...... | _0037ess0 |
| It's Always Springtime | Siempre es primavera | _0011SAK0 |
| Just One Feeling | Un sentimiento | _b192min0 |
| Kanou Revealed | Kanou revelada | _a042ess0 |
| Kitamura and Venus! | ¡Kitamura y Venus! | _a054ktm0 |
| Kitamura the Nudist | Kitamura el nudista | _0031ktm0 |
| Kitamura's Strategy | Estrategia de Kitamura | _0021ktm0 |
| Kota and Operation Venus! | ¡Kota y la operación Venus! | _a054koh0 |
| Learning from the God of Heartbreak | Lecciones del dios del desamor | _b192ktm0 |
| Leftovers | Sobras | _0034ess0 |
| Let's Break a Morning Sweat | Sudemos en la mañana | _b052ess0 |
| Let's See It! | ¡Vamos a verlo! | _c044ess0 |
| Let's Talk | Hablemos | _MP_AMI3 |
| Lies and Truth | Mentiras y verdad | _b266ami0 |
| Lovable? | ¿Adorable? | _c042ami0 |
| Love All Over Again | El amor otra vez | _MP_SUM1 |
| Love Needs Communication | El amor necesita comunicación | _a052tig0 |
| Luck Runs Out | Se acaba la suerte | _a052not0 |
| MOTTAINAI! Food | ¡Qué desperdicio! Comida | _0030ess0 |
| Map | Mapa | _0011AAA0 |
| Meddling? | ¿Entrometido? | _a054yas0 |
| Memories of Christmas | Recuerdos de Navidad | _b062tig0 |
| Memories of Fried Rice | Recuerdos del arroz frito | _b041koh0 |
| Memory Fragments | Fragmentos de memoria | _b062koh0 |
| Midnight SOS | SOS medianoche | _0037ed10 |
| Midwinter Sunlight | Luz de sol en invierno | _c072min0 |
| Misfortune Again | Otra vez la desgracia | _d022ed10 |
| Misfortune Incarnate | La desgracia encarnada | _0011KOH0 |
| Missed Connection: Haruta Ver. | Conexión perdida: vers. Haruta | _a361har0 |
| Missed Connection: Noto Ver. | Conexión perdida: vers. Noto | _a361not0 |
| Mission Complete | Misión cumplida | _c067ess0 |
| Mission Failed | Misión fallida | _a264ess0 |
| Morning of Opening Ceremony | Mañana de la apertura | _a290ess0 |
| Morning of Unrest | Mañana de inquietud | _0020ess0 |
| Mother | Madre | _c064yas0 |
| Mystery of the Universe | Misterio del universo | _a054har0 |
| Near, Yet Far | Cerca y lejos | _c061ami0 |
| New Year's Foundation | Cimientos de Año Nuevo | _b044ami0 |
| No Turning Back | Sin vuelta atrás | _b045tig0 |
| Noto the Tactician? | ¿Noto el táctico? | _c053not0 |
| Noto's Surprisingly Rich | Noto, rico por sorpresa | _b045not0 |
| Of Love and Heartbreak | De amor y desamor | _a043ktm0 |
| Old-Fashioned | A la antigua | _c040ess0 |
| On My Mind...... | En mi mente...... | _b280ess0 |
| One Day at Dragon Diner | Un día en Dragon Diner | _a193ktm0 |
| Operation Venus! | ¡Operación Venus! | _a053ess0 |
| Past Person, Future Person | Persona del pasado, del futuro | _a192sum0 |
| Paused Game | Juego en pausa | _c072min0 |
| People Never Change | La gente nunca cambia | _b266ami0 |
| Pizza Tonight | Pizza esta noche | _0013MIN0 |
| Play Ball | A jugar | _c072min0 |
| Please Excuse Me | Disculpe | _0036ess1 |
| Praying For A Nightmare | Rezando por una pesadilla | _a193ktm0 |
| Prepared For Takeoff | Listos para despegar | _c043ess0 |
| Prologue | Prólogo | _0000ESS1 |
| Punishment From Taiga | Castigo de Taiga | _b192min0 |
| Pure Black | Negro puro | _c053ami0 |
| Pure White | Blanco puro | _c041ktm0 |
| Pursuit of Taiga | Tras Taiga | _0035min0 |
| RE:Legendary Showdown | RE:Duelo legendario | _a042ess0 |
| Remaking the Promise | Rehacer la promesa | _b041koh0 |
| Remnants of Amnesia | Restos de amnesia | _b280ess0 |
| Return March | Marcha de vuelta | _MP_MIN4 |
| Returning With An Extra | Volver con un extra | _b167ess0 |
| Reunion | Reencuentro | _0013MIN0 |
| Road to Truth | Hacia la verdad | _b170ed30 |
| Ryuuji's Decision | La decisión de Ryuuji | _b181ess0 |
| Sakura Before the Storm | Sakura antes de la tormenta | _a041sak0 |
| Same As Always | Como siempre | _b192min0 |
| Sausage Fest Hatsumode | Hatsumode de salchichas | _0032ess0 |
| Sensibly Unlucky | Desafortunado sensato | _d013ess0 |
| Sensing the Signs | Percibir las señales | _MP_MIN2 |
| Showdown Morning | Mañana del duelo | _c067ess0 |
| Slave to the Goddess | Esclavo de la diosa | _0032ed15 |
| Smile Again | Sonríe otra vez | _c073min0 |
| Spirit Capture Plan | Caza de espíritus | _a054not0 |
| Springtime at School | Primavera en la escuela | _a291sak0 |
| Springtime in January | Primavera en enero | _0033sak0 |
| Straight | Directo | _c064min0 |
| Strategy Meeting, Take Two | Estrategia, toma dos | _a052tig4 |
| Student Council Dog | Perro del consejo | _a292ed20 |
| Sumire the Scout | Sumire la vigía | _a292ed20 |
| Suspect In Custody | Sospechoso bajo custodia | _a192har0 |
| Swing Out | A balancearse | _c051min0 |
| Switcheroo | Intercambio | _a193ktm0 |
| Taiga in the Pool | Taiga en la piscina | _MP_TIG3 |
| Taiga's Disaster | El desastre de Taiga | _0034ess1 |
| Taiga's Misgivings | Las dudas de Taiga | _b192min0 |
| Taiga's Room...... | Cuarto de Taiga...... | _0022tig0 |
| Taiga's Wish | Deseo de Taiga | _0023ess0 |
| Telling the Truth | Decir la verdad | _c061har0 |
| Testing Ami | Probando a Ami | _b065ess0 |
| Testing Haruta | A prueba Haruta | _b065ess0 |
| Testing Haruta's Courage | Probando el valor de Haruta | _b064har0 |
| Testing Minori | A prueba Minori | _b065ess0 |
| Testing My Courage! | ¡Probando mi valor! | _b167ess0 |
| That Morning, in the Student Council Room | Esa mañana, en la sala del consejo | _a291sum0 |
| The Armband's True Meaning | El significado del brazalete | _a292ed10 |
| The Bear From That Memory | El oso de ese recuerdo | _0035tig0 |
| The Blushing Tiger | El tigre sonrojado | _c073min0 |
| The Christmas Eve Incident | El incidente de Nochebuena | _a192min0 |
| The Cost of Sunlight | El precio de la luz del sol | _c068ed10 |
| The Days Drag On | Los días se arrastran | _c068ed20 |
| The Dream Girl | La chica soñada | _a041har0 |
| The Evil SC President | La malvada presidenta | _0021ktm0 |
| The Final...... | El final...... | _b292ami0 |
| The Gang's at the Station Square! | ¡La pandilla en la plaza de la estación! | _b051not0 |
| The Independent Tiger | El tigre independiente | _MP_TIG4 |
| The Morning Without You | La mañana sin ti | _a190ess0 |
| The New Semester Begins | Comienza el semestre | _b181ess0 |
| The Night With No Handwarmer | La noche sin calentador de manos | _b064ami0 |
| The Password is OKINAWA | La contraseña es OKINAWA | _b192har0 |
| The Shocking Truth | La verdad impactante | _b060ess0 |
| The Shrewd One | La astuta | _b064ktm0 |
| The Silent Tiger | El tigre silencioso | _c073min0 |
| The Smiling Tiger | El tigre sonriente | _c073min0 |
| The Tiger of Rage | El tigre de la ira | _c057ess0 |
| The Tiger of Sorrow | El tigre de la tristeza | _c051tig0 |
| The Tiger's Revival | El renacer del tigre | _c040ess0 |
| The Tiger's Wrath | La ira del tigre | _0035tig1 |
| The Unwanted Present | El regalo no deseado | _0021har0 |
| The Wake Up Call | La llamada de atención | _b280ess0 |
| The Weeping Tiger | El tigre llorón | _c072tig0 |
| The Worst Possible Luck | La peor suerte posible | _d011ryu0 |
| This Excitement | Esta emoción | _0037ed15 |
| Three Guys' Italian | Italiano de tres chicos | _b366har0 |
| Three Guys, Late at Night...... | Tres chicos, de noche...... | _b366har0 |
| Tiger VS Chihuahua | Tigre contra Chihuahua | _0033ami0 |
| Tiger in the Labyrinth | Tigre en el laberinto | _c041min0 |
| Time Flies When You're Having Fun | El tiempo vuela divirtiéndose | _0034ess0 |
| To Grandma's House | A casa de la abuela | _0021min0 |
| To Inko-chan...... | A Inko-chan...... | _0025ess0 |
| True Nature | Naturaleza real | _0032ed15 |
| Two Guys, Late At Night...... | Dos chicos, de noche...... | _b366har0 |
| Two Guys, Late at Night...... +1 | Dos chicos, de noche...... +1 | _b366har0 |
| Unidentified Flying Object | Objeto volador no identificado | _c053koh0 |
| Unnoticed Feelings | Sentimientos ocultos | _b046ess0 |
| Unprepared | Sin preparación | _0011YUR0 |
| Useless Man | Hombre inútil | _a052tig0 |
| Visibly Unlucky | Mala suerte visible | _MP_SAK1 |
| We're the Same As Ever | Iguales que siempre | _0011HAR0 |
| What Worries Me...... | Lo que me preocupa...... | _0023ess4 |
| Where The Feelings Are | Donde los sentimientos | _b292ami0 |
| Wife? | ¿Esposa? | _a052yur0 |
| Wish. | Deseo. | _a163tig0 |
| With Inko-chan...... | Con Inko-chan...... | _0016ess0 |
| With a Wish | Con un deseo | _a043yas0 |
| Without Looking Back | Sin mirar atrás | _MP_AMI4 |
| Yacchan's Shocking | Lo impactante de Yacchan | _c065ktm0 |
| Year-End Crisis | Crisis anual | _0012TIG0 |
| Yep, Eternal Spring | Sí, eterna primavera | _a052sak0 |
| Yep, Mother and Son | Sí, madre e hijo | _0037ed15 |
| Yuri's Phone Call | La llamada de Yuri | _0021yur0 |
| Yuri's Wish | El deseo de Yuri | _0033yur0 |
| Yuri, Ryuuji, and the Bird | Yuri, Ryuuji y el pájaro | _a163yur0 |
| Yuri-chan's Hint #1 | Pista de Yuri-chan #1 | _0032ed15 |
| Yuri-chan's Hint #10 | Pista de Yuri-chan #10 | _b192min0 |
| Yuri-chan's Hint #11 | Pista de Yuri-chan #11 | _b192min0 |
| Yuri-chan's Hint #12 | Pista de Yuri-chan #12 | _b292ami0 |
| Yuri-chan's Hint #13 | Pista de Yuri-chan #13 | _b293ed25 |
| Yuri-chan's Hint #14 | Pista de Yuri-chan #14 | _b293ed20 |
| Yuri-chan's Hint #15 | Pista de Yuri-chan #15 | _b292ami0 |
| Yuri-chan's Hint #16 | Pista de Yuri-chan #16 | _b366har0 |
| Yuri-chan's Hint #17 | Pista de Yuri-chan #17 | _c073min0 |
| Yuri-chan's Hint #18 | Pista de Yuri-chan #18 | _c072min0 |
| Yuri-chan's Hint #19 | Pista de Yuri-chan #19 | _c068ed20 |
| Yuri-chan's Hint #2 | Pista de Yuri-chan #2 | _0037ed15 |
| Yuri-chan's Hint #20 | Pista de Yuri-chan #20 | _c068ed10 |
| Yuri-chan's Hint #21 | Pista de Yuri-chan #21 | _d022ed10 |
| Yuri-chan's Hint #3 | Pista de Yuri-chan #3 | _a193ktm0 |
| Yuri-chan's Hint #4 | Pista de Yuri-chan #4 | _a193ktm0 |
| Yuri-chan's Hint #5 | Pista de Yuri-chan #5 | _a193ktm0 |
| Yuri-chan's Hint #6 | Pista de Yuri-chan #6 | _a292ed10 |
| Yuri-chan's Hint #7 | Pista de Yuri-chan #7 | _a292ed20 |
| Yuri-chan's Hint #8 | Pista de Yuri-chan #8 | _a364ed10 |
| Yuri-chan's Hint #9 | Pista de Yuri-chan #9 | _b170ed30 |
| スタートポイント | Inicio | STARTPOINT |

---

## 3. Títulos de textura (PRIORIDAD — Sam)

### Atlas de nombres (sg_chaname.gim) — CONVERTIDO Y CABE
- Script: `gim_codec.py` (parse, swizzle PSP 8-bit 16×8, GIM→PNG, PNG→GIM) + `convertir-atlas.py`.
- GIM verificado: header "MIG.00.1PSP", 512×384, INDEX8, paleta RGBA8888 (256 colores), píxeles swizzled. Decodificación del original = **0/196,608 píxeles de diferencia** vs la referencia.
- ChatGPT JPEG (1206×905, fondo blanco) → redimensionado a 512×384 (LANCZOS), blanco→transparente (umbral 242 → índice 189), cuantizado a la paleta ORIGINAL (66 entradas opacas), swizzled, paleta idéntica a la original.
- **gzip 74,937 B — CABE en el hueco de 75,776 B (margen 839 B).** GIM mismo tamaño (197,840 B). 92,817 píxeles transparentes (47.2%).
- **Verificado visualmente (decode):** TODOS ×3 en la fila 5 en (110,128), (218,128), (326,128); todas las etiquetas correctas (ALTAVOZ, MAMÁ DE KOTA, ANCIANA, AMI, COMPAÑERO?, ALUMNA, REPORTERO, RYUUJI-KUN, INKO-CHAN?, ESTUDIANTE ♂/♀, EMPLEADO, KITAMURA, TAIGA, PROFESOR?, PÁJARO?, AMI-CHAN, ¡PROFESOR!, NANAKO?, MINORIN, KIHARA?, YACCHAN, RYUUJI?, SUMIRE, JUNIOR, SAKURA, KASHII, CLIENTE, MUJER, YASUKO, ¿¿¿YO???, MINORI, ¿TIGRE?, HARUTA, ¿QUIÉN?, ¡¿YO?!, AMBOS, NOTO, KOTA, SEÑORA, ¡¡YO!!, ANFITRIÓN, YURI, ¡YO!, FAN). Nombres propios intactos. Bordes algo más duros que el original (umbral de alfa vs anti-aliasing suave) pero legible y correcto.
- Alineación: las etiquetas de ChatGPT NO están en exactamente la misma posición que el original (IoU global 0.753) — por eso el alfa se calculó desde la imagen de ChatGPT y NO se reutilizó la máscara original.
- Archivos: `prueba-todos/sg_chaname-todos.gim`, `.gim.gz`, `-decoded.png`.
- **En v6:** insertado en resource.dat image_main.dat, offset 54,349,824; tamaño GPDA actualizado (54,227,896 → 74,937); seekmap actualizado (74,384 → 74,937).

### Headers del SYSTEM MENU (sg_title01–13) — LOS 13 CONVERTIDOS Y CABEN
- Script: `convertir-headers.py`. Composite de ChatGPT (1206×870) dividido por detección de color (texto amarillo/rojo, bandas de fila y 3 grupos x). Fondo eliminado por distancia al gris oscuro (rampa de alfa 12–40). Cada recorte redimensionado a la altura del texto original, colocado en el offset original sobre un lienzo transparente del tamaño del GIM. Cuantizado a la paleta ORIGINAL de cada header (paleta idéntica); transparente → índice transparente de ese header.
- Originales extraídos de `repack-full/first-v5.dat` (offsets 75,776–124,928, slots de 4,096 B) en `headers-orig/`. Dimensiones: 256×40 (01, 04, 05, 06, 07, 09, 10, 12, 13) y 128×40 (02, 03, 08, 11).
- **Resultado: LOS 13 CABEN en sus slots de 4,096 B:** 01: 3,717 (margen 379), 02: 2,584 (1,512), 03: 2,344 (1,752), 04: 3,749 (347), 05: 3,233 (863), 06: 2,725 (1,371), 07: 3,408 (688), 08: 2,537 (1,559), 09: 2,423 (1,673), 10: 2,882 (1,214), 11: 2,343 (1,753), 12: 3,714 (382), 13: 2,652 (1,444).
- **Verificado visualmente (decode):** title01 "MENÚ DEL SISTEMA" y title13 "ENCICLOPEDIA" — texto correcto, estilo correcto, legible. (Los otros 11 PNG decodificados existen pero no se revisaron uno por uno a ojo.)
- Archivos: `prueba-titulos/headers/` (13 .gim + .gim.gz + -decoded.png).
- **En v6:** insertados en first.dat image_sharing.dat, offsets 75,776–124,928; tamaño GPDA de cada uno actualizado (2360 + (i−1)×16). Los headers NO están en el seekmap (0 coincidencias), así que no se tocó el seekmap por ellos.
- Nota: la 5ª fila del composite también trae sg_button.gim.gz y sg_logo.gim.gz — NO son headers y se ignoraron correctamente.

---

## 4. Aplicación de los títulos de escena (preparación)

Script: `aplicar-titulos.py`. Por cada escena: extrae el .obj.gz de resource-v5.dat, descomprime, reemplaza cada bloque 0x02BC con el título ES (mismo tamaño de bloque, mismo sufijo de 6 bytes, relleno cero), reensambla el .obj (los demás bloques byte-idénticos), recomprime con gzip −9 y verifica que cabe en su hueco (de `lotes/scene-map.json` para las 311 escenas; calculado del seekmap para las 52 `_aaa0`).

- **363/363 escenas procesadas. 363/363 caben. 0 no caben.**
- Dos casos que requirieron ajuste:
  - **STARTPOINT:** el hueco del scene-map (14,336 B) era el PRE-shift. El hueco real post-shift es **14,862 B** (la entrada 1 se movió +526). El .obj.gz nuevo mide 14,853 B → **cabe (margen 9 B)**. Se corrigió el hueco en el script.
  - **_b045not0:** el .obj.gz nuevo medía 4,100 B vs hueco 4,096 B (4 B de más). Niveles gzip 1–9 no ayudaron (el 9 era el menor, 4,100 B). Se acortó el único título de la escena: "Noto's Surprisingly Rich" → **"Noto, rico por sorpresa"** (23 caracteres, conserva la sorpresa) → gzip 4,093 B → **cabe (margen 3 B)**.
- Salida: `titulos-v6/` (363 .obj.gz nuevos). Reporte: `aplicar-titulos-report.json`.

---

## 5. ISO v6 — construcción

Script: `build-final-v6.py` (basado en el flujo v5: `build-final-shift-iso-v5.py`). Parte de `repack-full/resource-v5.dat` y `repack-full/first-v5.dat`.

- **363 .obj.gz** escritos en resource.dat + tamaño GPDA (contenedor+24) actualizado en cada uno.
- **Atlas** escrito en 54,349,824 + tamaño GPDA (54,227,896 → 74,937).
- **13 headers** escritos en first.dat (75,776 + (i−1)×4,096) + tamaño GPDA (2360 + (i−1)×16) actualizado en cada uno.
- **Seekmap** (en first.dat, offset 475,136, hueco 288,768 B): 364 sustituciones (363 escenas + atlas). Solo `_b047ess0` cambia de dígitos (1002 → 999), así que el texto descomprimido queda **1 byte más corto** (1,375,861 B; se registra, no afecta el parseo por líneas). Recomprimido con gzip nivel 9: **288,015 B — CABE** (hueco 288,768 B).
- ISO construido con pycdlib (copia del ISO v5, reemplazando resource.dat y first.dat). Round-trip verificado para ambos archivos.
- **ISO v6: `toradora-portable-ES-v6.iso`, 1,708,947,456 B, md5 `88584bd0656046fa900463ab15e9fe48`.**
- Reporte de build: `repack-full/build-v6-report.json` (todos los checks OK).
- **El ISO v5 NO se tocó** (md5 verificado `0993d95d4a1a687d32edce46777d753a` tras la copia).

---

## 6. Verificación binaria (completa)

Script: `verificar-v6.py`. Extrae resource.dat y first.dat del ISO v6 y verifica cada archivo.

- **Escenas: 363/363 OK.** **Títulos: 450/450 apariciones OK** (275 únicos, cada uno en su bloque 0x02BC correcto con el texto ES esperado). El resto de cada .obj es idéntico al v5.
- **Atlas: OK** — el sg_chaname.gim.gz del ISO v6 es byte-idéntico al convertido (74,937 B).
- **Headers: 13/13 OK** — cada sg_title.gim.gz del ISO v6 es byte-idéntico al convertido.
- **Fallos: 0.** Reporte: `verificar-v6-report.json`.

---

## 7. Verificación visual en PPSSPP (VM) — NO COMPLETADA (entorno)

**Cap de prueba: 30 minutos totales. Se intentó; no se pudo completar por fallos del entorno de la VM, NO del ISO.**

- **Intento 1 (06:26):** PPSSPP AppImage no arrancó — "Unable to initialize SDL: Could not setup connection to PulseAudio". Captura en blanco (202 B).
- **Intento 2 (06:30, con SDL_AUDIODRIVER=dummy):** mismo error SDL/PulseAudio. La VM **no tiene el demonio pulseaudio instalado** (`pulseaudio: command not found`; `apt-get install pulseaudio` → "no installation candidate"). Las librerías libpulse SÍ están, pero no hay servidor.
- **Diagnóstico:** `/dev/fuse` no existe en la VM → el AppImage falla con "failed to utilize FUSE during startup!". Se extrajo el AppImage (`squashfs-root/`, extracción OK) para evitar FUSE.
- **Intento 3 (binario extraído vía AppRun):** mismo error SDL/PulseAudio (la variable SDL_AUDIODRIVER=dummy no evita que el SDL empaquetado intente PulseAudio).
- **Intento 4 (binario directo PPSSPPSDL):** Segmentation fault (el AppRun/sharun configura las librerías; sin él el binario no arranca).
- Se detuvo la prueba de PPSSPP a los ~25 minutos para respetar el cap de 30 min. Procesos limpiados (0 restantes).

**Qué quedó verificado visualmente y qué no:**
- Verificado visualmente (fuera del juego, por decodificación): el atlas TODOS ×3 y los headers "MENÚ DEL SISTEMA" y "ENCICLOPEDIA" (sección 3). Los 450 títulos están verificados a nivel binario (sección 6).
- **NO verificado visualmente en el juego:** que el título "Regreso a casa" se vea en pantalla al empezar _0010ESS0, que "TODOS" se vea en un diálogo, ni que los headers se vean en el System Menu. La verificación binaria es completa y el método de construcción es el mismo que pasó PPSSPP en v5, pero el render en pantalla de v6 queda pendiente.
- **Recomendación:** que Sam lo pruebe en su iPhone/PC (su playtest es la validación autoritativa, como en v5). Si el juego arranca y el prólogo muestra los títulos en español, v6 está bien.

---

## 8. Archivos

| Archivo | Descripción |
|---|---|
| `investigacion-texturas/censo-titulos-v5.py` | Censo (363 .obj.gz → 450 apariciones, 275 únicos) |
| `investigacion-texturas/titulos-escena-v5.json` | Catálogo (escena + bloque + offset + texto) |
| `investigacion-texturas/titulos-unicos-v5.txt` | Lista de 275 títulos únicos |
| `investigacion-texturas/titulos-para-traducir.json` | 275 títulos con su límite de unidades |
| `investigacion-texturas/traducir-titulos.py` | Tabla de traducción + validación de ajuste |
| `investigacion-texturas/titulos-es.json` | Tabla EN→ES (275) |
| `investigacion-texturas/gim_codec.py` | Codec GIM (parse, swizzle, GIM↔PNG) |
| `investigacion-texturas/convertir-atlas.py` | Conversión del atlas (TODOS) |
| `investigacion-texturas/prueba-todos/sg_chaname-todos.gim` (+ `.gim.gz`, `-decoded.png`) | Atlas convertido |
| `investigacion-texturas/convertir-headers.py` | Conversión de los 13 headers |
| `investigacion-texturas/prueba-titulos/headers/` | 13 headers convertidos (.gim + .gim.gz + -decoded.png) |
| `investigacion-texturas/headers-orig/` | 13 headers originales extraídos |
| `investigacion-texturas/aplicar-titulos.py` | Aplica los títulos a los .obj (363 .obj.gz nuevos) |
| `investigacion-texturas/titulos-v6/` | 363 .obj.gz nuevos con títulos ES |
| `investigacion-texturas/aplicar-titulos-report.json` | Reporte de aplicación (363 caben, 0 no caben) |
| `build-final-v6.py` | Build del ISO v6 |
| `repack-full/build-v6-report.json` | Reporte de build (checks OK) |
| `repack-full/resource-v6.dat`, `repack-full/first-v6.dat` | resource.dat y first.dat de v6 |
| `toradora-portable-ES-v6.iso` | **ISO v6** (md5 `88584bd0656046fa900463ab15e9fe48`) |
| `investigacion-texturas/verificar-v6.py` | Verificación binaria de v6 |
| `investigacion-texturas/verificar-v6-report.json` | Reporte de verificación (450/450, atlas OK, 13/13, 0 fallos) |
| `repack-full/launch-v6.sh`, `repack-full/test-v6.log`, `test-v6b.log`, `test-v6c.log` | Intentos de prueba PPSSPP (fallidos por entorno) |
| `repack-full/shots/v6-boot-1.png` | Captura en blanco del intento PPSSPP |

## 9. Pendientes

- **Playtest visual de v6 por Sam** (iPhone/PC): confirmar que "Regreso a casa" se ve al empezar la escena, que "TODOS" aparece en diálogos y que los headers del System Menu se ven en español.
- **Issue de GitHub a los autores EN:** respondido el 19 nov 2026 — se negaron y pidieron no ser mencionados ni asociados al proyecto. En consecuencia, el repo no acredita ni enlaza su trabajo; solo indica que se parte de la ISO con el parche en inglés v1.10. El cambio de avatar de esa cuenta quedó diferido ("lo hago luego", Sam).
- **Manual impreso:** PARKED (no comprar; solo si aparece un escaneo digital).
- **Documentación final** (`documentacion-proceso.md`): cerrar con historial de versiones al final del proyecto (incluir los 40 acortamientos de títulos y el acortamiento de _b045not0 en el reporte de recortes).
