# Acortes de las 11 escenas — Toradora! Portable en español

**Fecha:** 18 nov 2026 (noche). **Aprobación:** Sam eligió "Acortar lo mínimo las 11 escenas" y pidió ver el plan por escena antes de aplicar (presentado 17:26, aprobado 17:30).
**ISO nuevo:** `toradora-portable-ES.iso` — 1,708,947,456 B, md5 `cc05dfd97690f36dffe62865a977c2d9` (antes: `2db9e6eaf8000bf406292aa59acfb5a6`).
**Resultado: 10 de 11 escenas entraron** (las 10 de diálogo). **STARTPOINT NO entró** (ver § STARTPOINT).
**Backups:** `lotes/backup-pre-acortes-11/` (los 11 .po originales). Scripts: `aplicar-acortes-11.py` (ronda 1), `aplicar-acortes-ronda2.py`, `aplicar-acortes-ronda3.py`, `acortar-startpoint.py`. Logs JSON: `lotes/acortes-11-aplicados.json`, `acortes-ronda2.json`, `acortes-ronda3.json`, `acortes-startpoint.json`.

## Hallazgo clave: la ronda 1 aprobada no bastó

Los acortes aprobados por Sam (ronda 1, 29 reemplazos) ahorraron solo **12–36 B** por escena, pero las sobras eran de **8–143 B**. Causa: gzip comprime el .obj (UTF-16LE) con mucha eficiencia — cada carácter eliminado ahorra solo **~0.4–1.0 B** comprimidos (medido: ~0.5 B/car de media). Por eso hicieron falta **rondas 2 y 3 con el mismo criterio** (quitar redundancias, sin cambiar el sentido, recalcular ＿, ≤40 car/línea, ≤3 líneas). Total: **184 acortes** en 146 entradas de diálogo + 32 reemplazos en STARTPOINT (59 entradas). Todas las entradas modificadas se verificaron (líneas ≤40 car, ≤3 líneas) y los msgid quedaron intactos (verificado contra el backup).

## Resumen por escena

| Escena | Sobra orig. | .obj.gz nuevo | Hueco | Margen | .dat.gz | Estado |
|---|---|---|---|---|---|---|
| _b045not0 | 8 B | 4095 | 4096 | 1 B | 1464/2048 | ✅ ENTRA |
| _a043ktm0 | 22 B | 6140 | 6144 | 4 B | 2135/4096 | ✅ ENTRA |
| _a050ess0 | 34 B | 4084 | 4096 | 12 B | 1620/2048 | ✅ ENTRA |
| _b051yur0 | 45 B | 6100 | 6144 | 44 B | 2291/4096 | ✅ ENTRA |
| _0032ed15 | 102 B | 6114 | 6144 | 30 B | 2311/4096 | ✅ ENTRA |
| _b050ess0 | 105 B | 4087 | 4096 | 9 B | 1545/2048 | ✅ ENTRA |
| _MP_MIN2 | 133 B | 10226 | 10240 | 14 B | 3599/4096 | ✅ ENTRA |
| _a193ktm0 | 138 B | 20480 | 20480 | 0 B | 8567/10240 | ✅ ENTRA |
| _MP_TIG1 | 143 B | 10234 | 10240 | 6 B | 3607/4096 | ✅ ENTRA |
| _c042ami0 | 143 B | 10238 | 10240 | 2 B | 4474/6144 | ✅ ENTRA |
| STARTPOINT | 696 B | 14862 | 14336 | -526 B | 40/2048 | ❌ NO ENTRA |

Márgenes ajustados en varias escenas (_a193ktm0: 0 B, _b045not0: 1 B, _c042ami0: 2 B, _a043ktm0: 4 B). gzip es determinista (nivel 9, mtime=0), así que el tamaño es reproducible; el build verificó cada escena con `assert len(ogz) <= gap`.

## _b045not0 (sobra original 8 B → .obj.gz 4095/4096, margen 1 B)

- [R1] **#71** (−16 car): «Mi papá me dio unas entradas gratis para Luxure. Las aguas termales y el gimnasio son gratis.» → «Mi papá me dio entradas gratis para Luxure. Aguas termales y gimnasio gratis.»

## _a043ktm0 (sobra original 22 B → .obj.gz 6140/6144, margen 4 B)

- [R1] **#6** (−10 car): «Al ver su cara seria tan despreciable, mi orgullo se interpuso...... Así que no fue distinto a la última vez.» → «Al ver su cara tan despreciable, mi orgullo se interpuso...... Así que fue igual que la última vez.»
- [R1] **#58** (−6 car): «¿Quizá me engaña para que diga lo que ella no puede?» → «¿Me engaña para que diga lo que ella no puede?»
- [R2] **#58** (−7 car): «Qué mala ① Bueno, Ami-chan es tan amable que te lo dirá.» → «Qué mala ① Ami-chan es tan amable que te lo dirá.»
- [R2] **#24** (−5 car): «Claro que tenía que portarme bien frente a los padres de Yuusaku.» → «Claro que tenía que portarme bien con los padres de Yuusaku.»
- [R2] **#60** (−4 car): «se declaró frente a toda la escuela y fue rechazado con honor.» → «se declaró ante toda la escuela y fue rechazado con honor.»
- [R2] **#54** (−6 car): «Pero fue un rechazo rotundo frente a todos nosotros.» → «Pero fue un rechazo rotundo frente a nosotros.»

## _a050ess0 (sobra original 34 B → .obj.gz 4084/4096, margen 12 B)

- [R1] **#67** (−18 car): «¿O sea que Yasuko es mi madre? ¡¿Esta cara de niña, que no se parece en nada a mí, es mi madre?!» → «¿Yasuko es mi madre? ¡¿Esta cara de niña, que no se parece a mí, es mi madre?!»
- [R1] **#69** (−3 car): «Oyeee, Ryuu-chan debería hacerse este peinado～ Y una camisa con el cuello abiertooo, y una cadena de orooo.» → «Oyeee, Ryuu-chan debería hacerse este peinado～ Una camisa con el cuello abiertooo y una cadena de orooo.»
- [R2] **#8** (−10 car): «¡Espera, lo pongo a cocinar en la olla de barro enseguida!» → «¡Espera, lo pongo en la olla de barro enseguida!»
- [R2] **#31** (−9 car): «Perdón, me dejaste sin palabras...... Y bueno, ¿dónde está mi padre?» → «Perdón, me dejaste sin palabras...... ¿Dónde está mi padre?»
- [R2] **#61** (−13 car): «Las tortillas enrolladas quedaron esponjosas y brillantes, la sopa de miso es casera» → «Las tortillas enrolladas quedaron esponjosas, la sopa de miso es casera»
- [R2] **#37** (−9 car): «Seguro hay razones por las que mi padre ya no está» → «Seguro hay razones por las que ya no está»

## _b051yur0 (sobra original 45 B → .obj.gz 6100/6144, margen 44 B)

- [R1] **#109** (−12 car): «En mi caso, mis amigas dicen» → «Mis amigas dicen»
- [R1] **#113** (−12 car): «Agradezco tanto poder llevar una vida normal de preparatoria» → «Agradezco llevar una vida normal de preparatoria»
- [R2] **#81** (−18 car): «Si es solo para el salón, parece que dan ropa de cambio. Está bien mientras no sea nada poco profesional, ¿no?» → «Si es solo para el salón, dan ropa de cambio. Está bien si no es nada poco profesional, ¿no?»
- [R2] **#94** (−7 car): «Sé que en el pasado me gustaba Kushieda» → «Sé que antes me gustaba Kushieda»
- [R2] **#52** (−13 car): «Solo pasaba de camino a la plaza de la estación. Y sobre las entradas, aún tengo algunas, así que vamos todos.» → «Solo pasaba camino a la plaza de la estación. Sobre las entradas, aún tengo algunas, vamos todos.»
- [R2] **#111** (−5 car): «¡Pero verás, Kushieda-san!» → «¡Verás, Kushieda-san!»
- [R2] **#85** (−4 car): «Bien, vamos hacia la plaza de la estación.» → «Bien, vamos a la plaza de la estación.»
- [R2] **#34** (−5 car): «¿Serán compañeras mías?» → «¿Serán compañeras?»
- [R3] **#113** (−7 car): «sonriendo y hablando con gente normal, pese a mi» → «sonriendo y hablando con gente, pese a mi»
- [R3] **#109** (−13 car): «¡Me voy al extranjero con mi novio!» → «¡Me voy al extranjero!»
- [R3] **#52** (−15 car): «Solo pasaba camino a la plaza de la estación.» → «Solo pasaba camino a la plaza.»
- [R3] **#111** (−7 car): «la lista de amigas con las que salir es más corta» → «la lista de amigas para salir es más corta»
- [R3] **#94** (−7 car): «así que ¿cómo es que puedo hablar con ella tan naturalmente?» → «así que ¿cómo puedo hablar con ella tan naturalmente?»
- [R3] **#85** (−15 car): «Bien, vamos a la plaza de la estación.» → «Bien, vamos a la plaza.»
- [R3] **#81** (−5 car): «Está bien si no es nada poco profesional, ¿no?» → «Está bien si no es poco profesional, ¿no?»
- [R3] **#17** (−14 car): «Todas están tan ocupadas con sus vidas que nunca puedo hacer planes con ellas» → «Todas están tan ocupadas que nunca puedo hacer planes con ellas»
- [R3] **#34** (−4 car): «Pero esa me llamó "Takasu-kun".» → «Pero me llamó "Takasu-kun".»
- [R3] **#60** (−6 car): «siempre andaban pegadas a Kawashima» → «siempre andaban con Kawashima»
- [R3] **#98** (−7 car): «Bueno, la verdad...... no sabía quiénes eran Kihara y Kashii» → «La verdad...... no sabía quiénes eran Kihara y Kashii»
- [R3] **#39** (−5 car): «Seguro que nadar un rato sin prisas se va a sentir genial.» → «Seguro que nadar un rato sin prisas se siente genial.»
- [R3] **#76** (−12 car): «No es exactamente la única que viene sin pagar aquí.» → «No es la única que viene sin pagar aquí.»
- [R3] **#20** (−6 car): «Escúcheme. No debe decir cosas tan negativas.» → «Escúcheme. No diga cosas tan negativas.»
- [R3] **#80** (−10 car): «O sea, de verdad debería abstenerme.» → «O sea, debería abstenerme.»

## _0032ed15 (sobra original 102 B → .obj.gz 6114/6144, margen 30 B)

- [R1] **#96** (−19 car): «Para saber más, deberías intentar hablar con los amigos con los que pasaste tiempo en el Festival Cultural.» → «Para saber más, habla con los amigos con los que pasaste tiempo en el Festival Cultural.»
- [R1] **#87** (−12 car): «reflexionar juntos al respecto.» → «reflexionar juntos.»
- [R1] **#92** (−9 car): «Mientras tú estés de acuerdo, puede que sea una forma de felicidad» → «Si estás de acuerdo, puede que sea una forma de felicidad»
- [R1] **#49** (−2 car): «Jajajajaja» → «Jajajaja»
- [R2] **#110** (−21 car): «Quiero que reflexiones sobre las decisiones que tomaste esta vez y las tengas en cuenta para la próxima.» → «Quiero que reflexiones sobre tus decisiones y las tengas en cuenta para la próxima.»
- [R2] **#97** (−12 car): «Si calificara este final, supongo que le daría 60 puntos.» → «Si calificara este final, le daría 60 puntos.»
- [R2] **#18** (−15 car): «Aparte de eso, Ryuuji, ¡¿qué tan tonto eres?!» → «Ryuuji, ¡¿qué tan tonto eres?!»
- [R2] **#28** (−7 car): «Creo que TÚ eres la que está jugando con él.» → «Creo que TÚ eres la que juega con él.»
- [R2] **#26** (−5 car): «Basta, Ryuuji. A mí no me importa que me insulten.» → «Basta, Ryuuji. No me importa que me insulten.»
- [R2] **#105** (−6 car): «solo finges ser mala ahora......» → «solo finges ser mala......»
- [R2] **#101** (−9 car): «¿Y por qué sigues diciéndole "chihuahua tonta"» → «¿Y por qué le dices "chihuahua tonta"»
- [R2] **#49** (−12 car): «Jajajaja...... Aah, en serio, tu cara de bobo es buenísima» → «Jajaja...... Aah, tu cara de bobo es buenísima»
- [R2] **#92** (−13 car): «puede que sea una forma de felicidad, pero......» → «puede que sea felicidad, pero......»
- [R2] **#96** (−29 car): «Para saber más, habla con los amigos con los que pasaste tiempo en el Festival Cultural.» → «Para saber más, habla con tus amigos del Festival Cultural.»
- [R2] **#87** (−13 car): «hablar sobre la ruta que elegiste. Pensé que podríamos reflexionar juntos.» → «hablar sobre tu ruta. Pensé que podríamos reflexionar juntos.»
- [R2] **#45** (−7 car): «Ya logré mi objetivo, así que terminé contigo, Takasu-kun. Bueno, adiós» → «Ya logré mi objetivo, así que terminé contigo, Takasu-kun. Adiós»
- [R2] **#63** (−8 car): «Luego también te compraré tu revista favorita.» → «Luego te compraré tu revista favorita.»
- [R2] **#107** (−8 car): «Ah, sí. A partir de mañana, ¿les prepararías también a Maya y a Nanako?» → «Ah, sí. A partir de mañana, ¿les prepararías a Maya y a Nanako?»
- [R2] **#73** (−14 car): «Entonces hazlo a partir de mañana. Ah, y ojalá este té helado mejor estuviera, o sea, caliente» → «Entonces hazlo a partir de mañana. Ah, y ojalá este té helado estuviera caliente»
- [R2] **#95** (−4 car): «Además, parece que hay muchas cosas que aún no recuerdas.» → «Además, parece que hay muchas cosas que no recuerdas.»
- [R2] **#51** (−6 car): «¿Perdiste el sentido común y el vocabulario junto con tu memoria? Qué lástima das.» → «¿Perdiste el sentido común y el vocabulario con tu memoria? Qué lástima das.»

## _b050ess0 (sobra original 105 B → .obj.gz 4087/4096, margen 9 B)

- [R1] **#42** (−21 car): «Ya me preocuparé por mi metabolismo después. Dejando eso de lado, responde mi pregunta. ¿Qué está pasando?» → «Ya me preocuparé por mi metabolismo después. Responde mi pregunta. ¿Qué está pasando?»
- [R1] **#59** (−10 car): «debo meter la comida de Taiga en el refrigerador por ahora......» → «debo meter la comida de Taiga en el refrigerador......»
- [R1] **#71** (−7 car): «¡QUÉ DESPERDICIO!...... Bueno, podría cenarlo hoy......» → «¡QUÉ DESPERDICIO!...... Podría cenarlo hoy......»
- [R1] **#53** (−6 car): «Ah, y traje el bolso con tu traje de baño.» → «Traje el bolso con tu traje de baño.»
- [R2] **#2** (−9 car): «Bien, con esto basta para el almuerzo de Yasuko.» → «Bien, basta para el almuerzo de Yasuko.»
- [R2] **#48** (−5 car): «Es solo que, sin ti por ahí, Yasuko se ha estado sintiendo sola.» → «Es que, sin ti por ahí, Yasuko se ha estado sintiendo sola.»
- [R2] **#11** (−6 car): «Yacchan quisiera poder irrr.» → «Yacchan quisiera irrr.»
- [R2] **#53** (−11 car): «¿Ya estamos listos?» → «¿Listos?»
- [R2] **#14** (−7 car): «Yacchan está agotada, gansu...... A la cama, giza......» → «Yacchan está agotada...... A la cama, giza......»
- [R2] **#71** (−3 car): «Hasta me reté a cocinarlo al estilo Kansai.» → «Hasta me reté a cocinarlo estilo Kansai.»
- [R2] **#13** (−11 car): «Yacchan es más feliz cuando Ryuu-chan se divierteee» → «Yacchan es más feliz cuando te diviertes»
- [R2] **#59** (−3 car): «debo meter la comida de Taiga en el refrigerador» → «debo meter la comida de Taiga al refrigerador»
- [R2] **#69** (−5 car): «mientras pensaba en cómo apoyarlos a ti y a Minorin» → «mientras pensaba en apoyarlos a ti y a Minorin»
- [R2] **#33** (−10 car): «¡Hagámoslo otra vez algún día!» → «¡Hagámoslo otra vez!»
- [R2] **#10** (−13 car): «Si no llega en los próximos 10 minutos, iré a buscarla.» → «Si no llega en 10 minutos, iré a buscarla.»
- [R2] **#65** (−9 car): «no ver la cara de Taiga-chan hace que Yacchan se sienta» → «no ver a Taiga-chan hace que Yacchan se sienta»
- [R2] **#67** (−3 car): «No apareciste a comer ni anoche NI esta mañana.» → «No viniste a comer ni anoche ni esta mañana.»
- [R2] **#46** (−12 car): «así que simplemente pasó.» → «así que pasó.»
- [R2] **#8** (−12 car): «La otra porción es el desayuno de Taiga.» → «La otra porción es de Taiga.»
- [R2] **#16** (−12 car): «¿Qué es exactamente Yasuko para mí?» → «¿Qué es Yasuko para mí?»
- [R2] **#32** (−6 car): «no se compara con el arroz frito de Takasu-kun.» → «no se compara con el arroz de Takasu-kun.»
- [R2] **#12** (−6 car): «¿Quieres que pregunte si puedes ir?» → «¿Quieres que pregunte si vas?»

## _MP_MIN2 (sobra original 133 B → .obj.gz 10226/10240, margen 14 B)

- [R1] **#116** (−13 car): «¡Las bromas de Amin están hechas para tu disfrute! ¡Disfrútalo!» → «¡Las bromas de Amin están hechas para tu disfrute!»
- [R1] **#146** (−13 car): «Literalmente todo el mundo se nos está quedando mirando.» → «Todo el mundo se nos está quedando mirando.»
- [R1] **#278** (−10 car): «¡Deberías unirte al equipo de chicos!» → «¡Únete al equipo de chicos!»
- [R2] **#280** (−10 car): «¡En ese caso, deberías ver el próximo partido de Kitamura-kun!» → «¡En ese caso, ve el próximo partido de Kitamura-kun!»
- [R2] **#34** (−4 car): «¡Eres como un francotirador de élite rango A y yo soy el blanco!» → «¡Eres como un francotirador de élite rango A y yo el blanco!»
- [R2] **#154** (−12 car): «¡Estamos eternamente agradecidos! ¡Ja!» → «¡Estamos agradecidos! ¡Ja!»
- [R2] **#185** (−6 car): «no soy tan cobarde como para afligirme por tales nimiedades!» → «no soy tan cobarde como para afligirme por nimiedades!»
- [R2] **#276** (−8 car): «¡No te sonrojes también!» → «¡No te sonrojes!»
- [R2] **#199** (−9 car): «Pero en cuanto decidimos adoptarlo, debíamos prepararnos» → «Pero al decidir adoptarlo, debíamos prepararnos»
- [R2] **#116** (−9 car): «¡Las bromas de Amin están hechas para tu disfrute!» → «¡Las bromas de Amin son para tu disfrute!»
- [R2] **#278** (−10 car): «¡Únete al equipo de chicos! A Kitamura-kun le encantaría contar» → «¡Únete al equipo! A Kitamura-kun le encantaría contar»
- [R2] **#169** (−7 car): «Bueno, mientras sea feliz relajándose a gusto, no es gran cosa, ¿no?» → «Mientras sea feliz relajándose a gusto, no es gran cosa, ¿no?»
- [R2] **#149** (−6 car): «pienso: "¡Yo podría hacerlo mejor!"» → «pienso: "¡Yo lo haría mejor!"»
- [R2] **#146** (−10 car): «Pero ¿podrías bajar la voz, por favor?» → «Pero baja la voz, por favor.»
- [R2] **#161** (−10 car): «que te divirtieras nadando sin tener que preocuparte por ella?» → «que te divirtieras nadando sin preocuparte por ella?»
- [R2] **#282** (−14 car): «Verlos en persona te hace sentir más conectado» → «Verlos en persona te conecta más»
- [R2] **#284** (−12 car): «Lo de antes sobre Amin, ehm......» → «Lo de Amin, ehm......»
- [R2] **#286** (−12 car): «Amin y las demás dijeron que iban al salón del quinto piso.» → «Amin y las demás iban al salón del quinto piso.»
- [R2] **#110** (−9 car): «te habría invitado a uno de los partidos de Kitamura-kun.» → «te habría invitado a un partido de Kitamura-kun.»
- [R2] **#128** (−20 car): «¡¡Amin en traje de baño... en traje de baño...!!» → «¡¡Amin en traje de baño...!!»
- [R2] **#126** (−4 car): «¿que ver a Amin en traje de baño te da malos pensamientos, verdad?» → «¿ver a Amin en traje de baño te da malos pensamientos, verdad?»
- [R2] **#130** (−7 car): «no puedo creer que seamos de la misma especie» → «no creo que seamos de la misma especie»
- [R2] **#145** (−5 car): «es la MEJOR forma de disfrutar nuestra juventud!» → «es la MEJOR forma de disfrutar la juventud!»

## _a193ktm0 (sobra original 138 B → .obj.gz 20480/20480, margen 0 B)

- [R1] **#354** (−18 car): «vendrá a mi casa a comer en menos de lo que canta un gallo.» → «vendrá a mi casa a comer en un santiamén.»
- [R1] **#475** (−17 car): «Remodelé el primer piso de mi edificio de departamentos, y» → «Remodelé el primer piso de mi edificio, y»
- [R1] **#127** (−10 car): «Con tu fuerza de voluntad y perseverancia» → «Con tu voluntad y perseverancia»
- [R2] **#409** (−6 car): «ajusté el agarre para tranquilizarme una y otra» → «ajusté el agarre para calmarme una y otra»
- [R2] **#415** (−18 car): «Quería preguntarle a Aisaka si estaría dispuesta a ayudar a preparar» → «Quería preguntarle a Aisaka si ayudaría a preparar»
- [R2] **#457** (−15 car): «creo que siempre estás en la mente de Aisaka-san, incluso ahora.» → «creo que siempre estás en la mente de Aisaka-san.»
- [R2] **#184** (−7 car): «y un rostro dormido sin preocupación alguna.» → «y un rostro dormido sin preocupación.»
- [R2] **#401** (−6 car): «Lo que diré podría traicionar tu confianza en mí.» → «Lo que diré podría traicionar tu confianza.»
- [R2] **#465** (−12 car): «y luego oímos el rumor de que Kanou-senpai nos envió su» → «y luego oímos que Kanou-senpai nos envió su»
- [R2] **#459** (−6 car): «Escucha con cuidado y luego respóndele.» → «Escucha con cuidado y respóndele.»
- [R2] **#463** (−2 car): «Me enamoré de la Presidenta por su valor, su audacia para ser más varonil» → «Me enamoré de la Presidenta por su valor y audacia para ser más varonil»
- [R2] **#477** (−10 car): «Por mi mirada "malvada" y afilada, no» → «Por mi mirada "malvada", no»
- [R2] **#487** (−9 car): «Eres el mismo perro simple e inútil de siempre.» → «Eres el mismo perro inútil de siempre.»
- [R2] **#419** (−7 car): «Bueno, Yasuko me dijo que hiciera todos tus platos favoritos» → «Yasuko me dijo que hiciera todos tus platos favoritos»
- [R2] **#467** (−5 car): «Es solo cuestión de» → «Es cuestión de»
- [R2] **#481** (−8 car): «podemos darle consejos fáciles de guarniciones que dejarían asombrada» → «podemos darle consejos de guarniciones que dejarían asombrada»
- [R2] **#425** (−6 car): «y vivir en una vieja casita para perros» → «y vivir en una casita para perros»
- [R2] **#439** (−9 car): «Supongo que debería dejar de hacer esto.» → «Supongo que debería dejar esto.»
- [R2] **#190** (−25 car): «hablar sobre la ruta que elegiste. Pensé que podríamos reflexionar al respecto juntos.» → «hablar sobre tu ruta. Pensé que podríamos reflexionar juntos.»
- [R2] **#291** (−25 car): «hablar sobre la ruta que elegiste. Pensé que podríamos reflexionar al respecto juntos.» → «hablar sobre tu ruta. Pensé que podríamos reflexionar juntos.»
- [R2] **#390** (−25 car): «hablar sobre la ruta que elegiste. Pensé que podríamos reflexionar al respecto juntos.» → «hablar sobre tu ruta. Pensé que podríamos reflexionar juntos.»
- [R2] **#172** (−15 car): «y entonces estaremos todos en igualdad de condiciones.» → «y estaremos en igualdad de condiciones.»
- [R2] **#333** (−4 car): «pero puedo enamorarme de ti como hombre, ¿verdad?» → «pero puedo enamorarme de ti como hombre, ¿no?»
- [R2] **#354** (−9 car): «Esa chica volverá a ser la de siempre en un segundo» → «Esa chica volverá a ser ella en un segundo»
- [R2] **#475** (−3 car): «Ahora soy el dueño de un lugar llamado» → «Ahora soy dueño de un lugar llamado»
- [R2] **#127** (−12 car): «¡seguro tendremos una fiesta increíble! ¿Verdad, Presidenta?» → «¡seguro tendremos una fiesta increíble! ¿Verdad?»

## _MP_TIG1 (sobra original 143 B → .obj.gz 10234/10240, margen 6 B)

- [R1] **#148** (−13 car): «querer estar en esa "bandada" para empezar.» → «querer estar en esa "bandada".»
- [R1] **#151** (−15 car): «¡y no he dejado de llenarlo de amor desde entonces!» → «¡y no he dejado de llenarlo de amor!»
- [R1] **#62** (−7 car): «Bueno, si no hago que vuelvas rápido a la normalidad» → «Si no hago que vuelvas rápido a la normalidad»
- [R1] **#311** (−7 car): «Bueno, aún debemos comprar recuerdos para Yacchan.» → «Aún debemos comprar recuerdos para Yacchan.»
- [R2] **#72** (−12 car): «¡¿O me trataría como un bulto?! ¡¡Vete al diablo!!» → «¡¿O como un bulto?! ¡¡Vete al diablo!!»
- [R2] **#311** (−7 car): «Mini bizcochos, castañas dulces y caramelo de albaricoque» → «Mini bizcochos, castañas y caramelo de albaricoque»
- [R2] **#141** (−7 car): «Bueno, no creo que ninguno sea mala persona.» → «No creo que ninguno sea mala persona.»
- [R2] **#201** (−12 car): «Y no venden eso con este frío del demonio.» → «Y no venden eso con este frío.»
- [R2] **#146** (−7 car): «Bueno, tú mismo eres MUY bonachón, ¿sabes?» → «Tú mismo eres MUY bonachón, ¿sabes?»
- [R2] **#62** (−5 car): «Si no hago que vuelvas rápido a la normalidad» → «Si no te devuelvo rápido a la normalidad»
- [R2] **#148** (−16 car): «ni siquiera estoy segura de querer estar en esa "bandada".» → «ni siquiera quiero estar en esa "bandada".»
- [R2] **#175** (−16 car): «¡Basta de tus caprichos utópicos, impulsivos y despreocupados!» → «¡Basta de tus caprichos utópicos e impulsivos!»
- [R2] **#305** (−9 car): «y justo cuando creí que mejoraba, tuve que empezar de cero!» → «y justo cuando mejoraba, tuve que empezar de cero!»
- [R2] **#40** (−13 car): «¡¡No se te ocurra tramar nada raro!!» → «¡¡No trames nada raro!!»
- [R2] **#170** (−12 car): «¡Usa un poco más ese cerebro podrido y descúbrelo!!» → «¡Usa ese cerebro podrido y descúbrelo!!»
- [R2] **#186** (−13 car): «y por lo tanto no sería Inko-chan.» → «y no sería Inko-chan.»
- [R2] **#151** (−8 car): «¡y no he dejado de llenarlo de amor!» → «¡y no he dejado de quererlo!»
- [R2] **#164** (−12 car): «Qué bueno que puedas ser objetivo al respecto, pero no deberías decir algo así.» → «Qué bueno que puedas ser objetivo, pero no deberías decir algo así.»
- [R2] **#59** (−8 car): «¿No tienes idea de cuántos problemas me has estado causando desde que te dieron el alta?» → «¿No tienes idea de cuántos problemas me has causado desde que te dieron el alta?»
- [R2] **#38** (−4 car): «¡No te creas tan importante, monigote!» → «¡No te creas importante, monigote!»
- [R2] **#307** (−6 car): «Aunque fue-- fue un poco» → «Aunque fue un poco»
- [R2] **#87** (−13 car): «Cuando te eché un vistazo, seguías rogando y suplicando.» → «Cuando te vi, seguías rogando y suplicando.»
- [R2] **#95** (−9 car): «No, sigo haciéndolo, supongo.» → «No, sigo haciéndolo.»
- [R2] **#88** (−4 car): «¿te refieres a cuando pedía por lo del moho?» → «¿te refieres a cuando pedía por el moho?»
- [R3] **#311** (−5 car): «Mini bizcochos, castañas y caramelo de albaricoque» → «Bizcochos, castañas y caramelo de albaricoque»
- [R3] **#141** (−8 car): «No creo que ninguno sea mala persona.» → «No creo que ninguno sea malo.»
- [R3] **#62** (−7 car): «Si no te devuelvo rápido a la normalidad» → «Si no te devuelvo a la normalidad»
- [R3] **#146** (−4 car): «los pájaros del mismo plumaje vuelan en bandada.» → «los pájaros del mismo plumaje vuelan juntos.»
- [R3] **#72** (−10 car): «¡¡Vete al diablo!!» → «¡¡Vete!!»
- [R3] **#201** (−3 car): «No es un festival de verano.» → «No es festival de verano.»
- [R3] **#305** (−10 car): «y justo cuando mejoraba, tuve que empezar de cero!» → «y justo cuando mejoraba, empecé de cero!»
- [R3] **#148** (−9 car): «ni siquiera quiero estar en esa "bandada".» → «no quiero estar en esa "bandada".»

## _c042ami0 (sobra original 143 B → .obj.gz 10238/10240, margen 2 B)

- [R1] **#97** (−8 car): «No le des importancia...... En fin, como dijeron Kihara y Kashii» → «No le des importancia...... Como dijeron Kihara y Kashii»
- [R1] **#224** (−10 car): «Bueno, la verdad quizá no tengas» → «Bueno, quizá no tengas»
- [R1] **#178** (−7 car): «Bueno, me daría pena dejar que esas dos jueguen» → «Me daría pena dejar que esas dos jueguen»
- [R1] **#218** (−7 car): «Bueno, parece que no tengo ninguna foto clara de mí mismo» → «Parece que no tengo ninguna foto clara de mí mismo»
- [R2] **#216** (−14 car): «Seguro Yasuko se alegrará cuando se la mostremos» → «Seguro Yasuko se alegrará al verla»
- [R2] **#202** (−10 car): «En serio, pensé que ya estabas acostumbrada a los seres humanos» → «Pensé que ya estabas acostumbrada a los seres humanos»
- [R2] **#222** (−18 car): «Bueno, yo fui quien sugirió que se lo pusiera.» → «Yo sugerí que se lo pusiera.»
- [R2] **#90** (−9 car): «jamás le habría entrado en la cabeza a StuChi» → «jamás se le habría ocurrido a StuChi»
- [R2] **#165** (−16 car): «¿Veo visiones, o estás pálida como un fantasma?» → «¿Estás pálida como un fantasma?»
- [R2] **#97** (−5 car): «creo que es buena idea probárselos solo una vez.» → «creo que es buena idea probárselos una vez.»
- [R2] **#168** (−25 car): «No puedo. No es lo mío. Además...... En el remoto, REMOTÍSIMO caso» → «No puedo. No es lo mío. En el remoto caso»
- [R2] **#178** (−3 car): «así que tomemos unas fotos ya. Vamos.» → «así que tomemos unas fotos. Vamos.»
- [R2] **#218** (−8 car): «Parece que no tengo ninguna foto clara de mí mismo» → «Parece que no tengo foto clara de mí mismo»
- [R2] **#131** (−4 car): «así que démonos prisa y tomemos las fotos.» → «así que démonos prisa y tomemos fotos.»
- [R2] **#210** (−6 car): «¡No pasa nada! Probémonoslos antes.» → «¡No pasa nada! Probémonoslos.»
- [R2] **#224** (−7 car): «En cuanto a Taiga...... Bueno, quizá no tengas» → «En cuanto a Taiga...... Quizá no tengas»
- [R2] **#98** (−9 car): «así que probémonoslos rapidito.» → «así que probémonoslos.»
- [R2] **#139** (−7 car): «Bueno, es un poco tarde para...... Espera,» → «Es un poco tarde para...... Espera,»
- [R2] **#220** (−14 car): «siente una pequeñííísima sensación de derrota, así que» → «siente una sensación de derrota, así que»
- [R2] **#174** (−11 car): «O-Oye, Kawashima, deberías salir en la foto también, si quieres.» → «O-Oye, Kawashima, sal en la foto también, si quieres.»
- [R2] **#212** (−10 car): «De hecho, yo soy a quien molestan todo el tiempo» → «Yo soy a quien molestan todo el tiempo»
- [R2] **#119** (−6 car): «Tendremos otra oportunidad de reírnos de la torpeza de la Chihuahua sucia.» → «Tendremos otra oportunidad de reírnos de la torpeza de la Chihuahua.»
- [R2] **#26** (−6 car): «Seguro estás libre ahora mismo, así que ven un momento» → «Seguro estás libre ahora, así que ven un momento»
- [R2] **#214** (−17 car): «te dio un CD al volver de tu suspensión.» → «te dio un CD al volver.»

## STARTPOINT (sobra original 696 B → .obj.gz 14,862/14,336, **faltan 526 B, NO ENTRA**)

Ronda 1 aplicada (32 reemplazos, 59 entradas, ahorro 287 car únicos):

- ×23 (−18 car c/u): «VG_ATTAINMENT_END　23 o más＿Este valor no es posible durante una partida normal.＿Se restablecerá VG_ATTAINMENT_END　22.» → «VG_ATTAINMENT_END　23 o más＿Valor imposible en partida normal.＿Se restablecerá VG_ATTAINMENT_END　22.»
- ×1 (−4 car c/u): «Una lluvia de pétalos de cerezo antes de la tormenta» → «Lluvia de pétalos de cerezo antes de la tormenta»
- ×1 (−10 car c/u): «El malvado presidente estudiantil・Hace su aparición» → «El malvado presidente estudiantil aparece»
- ×1 (−4 car c/u): «Una noche en que no basta un calentador de bolsillo» → «Noche en que no basta un calentador de bolsillo»
- ×1 (−5 car c/u): «Mejor una gran deidad cerca que un santuario lejos» → «Mejor una deidad cerca que un santuario lejos»
- ×1 (−8 car c/u): «Primera visita del año al santuario entre hombres» → «Primera visita al santuario entre hombres»
- ×1 (−9 car c/u): «Dos personas que no se entienden・Parte de Haruta» → «Dos personas que no se entienden・Haruta»
- ×1 (−8 car c/u): «A quién encontré en las primeras rebajas del año» → «A quién encontré en las primeras rebajas»
- ×1 (−8 car c/u): «El deseo de los chicos y el anhelo de las chicas» → «El deseo de chicos y el anhelo de chicas»
- ×1 (−13 car c/u): «Un vínculo a cincuenta centímetros de distancia» → «Un vínculo a cincuenta centímetros»
- ×1 (−9 car c/u): «Dos personas que no se entienden・Parte de Noto» → «Dos personas que no se entienden・Noto»
- ×1 (−7 car c/u): «Una persona del pasado,una persona del futuro» → «Una persona del pasado, una del futuro»
- ×1 (−10 car c/u): «La mañana de la ceremonia de inicio de clases» → «La mañana de la ceremonia de inicio»
- ×1 (−11 car c/u): «Esa mañana,en la sala del consejo estudiantil» → «Esa mañana, en la sala del consejo»
- ×1 (−9 car c/u): «El mejor tinte para volver al cabello negro para hombres!» → «Tinte para volver al cabello negro para hombres!»
- ×1 (−5 car c/u): «Las enseñanzas de la gran deidad del desamor» → «Las enseñanzas de la deidad del desamor»
- ×5 (−8 car c/u): «Primera visita del año al santuario a solas» → «Primera visita al santuario a solas»
- ×1 (−6 car c/u): «Una historia de fantasmas en pleno invierno» → «Una historia de fantasmas en invierno»
- ×1 (−9 car c/u): «Foto del festival cultural・Ryuuji en una carrera reñida» → «Foto del festival・Ryuuji en una carrera reñida»
- ×1 (−16 car c/u): «ＤＶＤ de 『Crónica real・Japón el archipiélago del terror』» → «ＤＶＤ de 『Crónica real・Japón del terror』»
- ×1 (−8 car c/u): «El saludo de Año Nuevo es la base del año» → «El saludo de Año Nuevo es la base»
- ×1 (−5 car c/u): «Como siempre hay que tratarlo con cuidado» → «Siempre hay que tratarlo con cuidado»
- ×1 (−7 car c/u): «También es primavera el día de Año Nuevo» → «También es primavera en Año Nuevo»
- ×1 (−8 car c/u): «El enemigo natural de mi enemigo natural» → «El enemigo de mi enemigo natural»
- ×1 (−12 car c/u): «La mala suerte que no se puede demostrar» → «La mala suerte indemostrable»
- ×2 (−12 car c/u): «Final del perro del consejo estudiantil» → «Final del perro del consejo»
- ×1 (−4 car c/u): «Todos reunidos de una forma inesperada!» → «Todos reunidos de forma inesperada!»
- ×1 (−16 car c/u): «Dos hombres,a altas horas de la noche……» → «Dos hombres, de noche……»
- ×1 (−3 car c/u): «No desperdiciar la comida de Año Nuevo» → «No desperdiciar comida de Año Nuevo»
- ×1 (−10 car c/u): «Año Nuevo de una mujer de treinta años» → «Año Nuevo de una treintañera»
- ×1 (−10 car c/u): «El verdadero significado del brazalete» → «El significado del brazalete»
- ×1 (−15 car c/u): «Sentimientos que quedaron en el pasado» → «Sentimientos del pasado»

**Por qué no entra:** tras la ronda 1, el .obj.gz quedó en 14,862 B (antes 15,032 B; solo se ahorraron 170 B). La compresión es muy eficiente (~0.59 B por carácter único) y STARTPOINT tiene 1,359 cadenas de sistema: cerrar los 526 B restantes exigiría eliminar ~890 caracteres únicos más (~150–250 acortes adicionales en títulos de capítulo y mensajes de sistema), lo que degradaría visiblemente los títulos. Se decidió NO forzarlo (el hueco no se puede ampliar: el siguiente archivo, STARTPOINT .dat.gz, empieza 2,048 B después del fin del hueco y pertenece a otra entrada GPDA). **El menú/título queda en inglés**, como en el parche EN base. Los acortes de la ronda 1 quedan guardados en `po-es/STARTPOINT.po` (documentados arriba) por si se retoma más adelante.

## Repack e ISO

- `build-full-iso.py` (sin cambios): parcheó **310 escenas** (las 300 que ya cabían + las 10 acortadas), omitió solo STARTPOINT. `seekmap.gz` 288,368 → 288,005 B (620 sustituciones). Textos 4/4 reutilizados con CRLF corregido (utf8 111 B, ItemList 2,199 B, charaname 630 B, placename 684 B). Round-trip pycdlib OK (resource.dat 426,012,672 B, first.dat 1,499,136 B).
- `lotes/dryrun-repack.json` actualizado (fusión de la medición de las 11 escenas con el dry-run completo de 311).

## Prueba en PPSSPP (VM, 18 nov ~11:42 p.m.–12:05 a.m.)

PPSSPP 1.20.4 AppImage, Xvfb :99, `LIBGL_ALWAYS_SOFTWARE=1`. Lanzador `repack-full/test-iso-v2.sh`; capturas en `repack-full/shots/` (prefijo `v2-`). El arranque es lento en software (~2 min hasta el título), por lo que la secuencia se completó a mano tras el script (las pulsaciones X iniciales cayeron durante los logos).

- **Arranque limpio, 0 errores `Bad memory access`.** (Las únicas líneas `E[` del log son benignas: Vulkan no disponible —sin GPU, usa software— y falta `/font/zh_gb.pgf`, fuente china que el juego no usa.)
- Logos: Bandai Namco → Guyzware → CRIWARE → Motion Portrait / Silicon Studio.
- Título: menú en inglés (esperado, STARTPOINT no entró). New Game → cinemática de nieve → **batalla del prólogo en español**: «¡TAIGA usó un rayo mortal! BIBIBIBIBIBI...... ¡pero no afecta a MINORIN!» (3 líneas, cabe), «¡Turno de YURI!» (parcial en captura), «¡YURI compró un departamento! ¡Pero no era antisísmico!» (2 líneas), «¡RYUUJI no puede moverse! ¡RYUUJI no puede moverse! RYUUJI no puede......» (3 líneas).
- **Diálogo normal en español**: «RYUUJI (¡Maldi...» (inicio de pensamiento). Acentos, ¿, ¡ correctos; máximo 3 líneas, sin desborde.
- Las 10 escenas acortadas son de mitad/final del juego y no se alcanzan en una prueba rápida; su ajuste quedó verificado por dry-run (tamaño .obj.gz ≤ hueco) y por la verificación de formato (≤40 car, ≤3 líneas) al aplicar cada acorte. Quedan para la prueba final de Sam.
- Menú de objetos / nombres en sus pantallas propias: no verificado visualmente (requiere navegar a esos menús); los archivos están empaquetados y el juego arranca sin errores con ellos.

## Para el reporte final (documentacion-proceso.md)

- Método in-place con huecos fijos: el español es más largo que el inglés y 11 escenas no cabían; se resolvieron 10 con acortes mínimos (184 acortes, 3 rondas) y 1 (STARTPOINT, sistema) quedó en inglés por falta de 526 B.
- Lección de compresión: cada carácter eliminado ahorra solo ~0.5 B comprimidos; los acortes "mínimos" iniciales no bastaron y hubo que ampliarlos con el mismo criterio. Documentar que la estimación de ahorro debe medirse con dry-run, no estimarse a ojo.
- Lección de prueba: el arranque en software es lento (~2 min); las pulsaciones durante los logos se pierden y la secuencia de prueba debe esperar al título antes de pulsar.
---

## Cambio de menú + prueba (18 nov, ~6:09–6:15 p.m.)

**Cambio aplicado (Sam explícito):** en `po-es/_0000ESS1.po`, «Jugar historia principal» → **«Historia Principal»** y «Jugar historia extra» → **«Historia Extra»** (entradas 1–2, msgid «Play Main Story» / «Play Bonus Story»). Backup en `lotes/backup-pre-cambio-menu/`. Verificado: 70 entradas, msgid intacto. ISO de prueba `toradora-portable-ES-test-menu.iso` (md5 `70255ae6601a1de2f2da9c284416e804`; nuevo .obj 13,392 B, .obj.gz 3,586 B vs hueco 4,096, .dat.gz 1,230 B vs hueco 2,048; round-trip OK).

**Resultado en PPSSPP — EL MENÚ DE TÍTULO NO VIENE DE _0000ESS1.** La pantalla de título muestra (captura `repack-full/shots/menu-t3.png`): **«New Game / Continue / Options / Extra / Install»** en inglés. NO aparece «Historia Principal» ni «Historia Extra». Por tanto, las cadenas «Play Main Story» / «Play Bonus Story» de _0000ESS1.po NO son el menú principal: deben usarse en otro contexto (submenú al elegir New Game, sección Extra, o selección de historia), no en la pantalla de título.

**Búsqueda de «New Game» (dónde vive el menú de título):** NO está en ningún archivo .po (311 escenas + STARTPOINT), NO en EBOOT.BIN (2,487,188 B) ni BOOT.BIN, NO en first.dat (1,499,136 B), NO en resource.dat como texto plano (UTF-16LE ni ASCII), NO en ningún .obj.gz de escenas descomprimido. Ubicación aún no identificada: probablemente otro contenedor GPDA de resource.dat (datos no-script) o textura. Queda como investigación pendiente; el cambio a «Historia Principal» en _0000ESS1 queda aplicado en el .po (harmless, se verá donde se use esa cadena), pero NO traduce el menú de título.

## STARTPOINT — Medición (18 nov, ~6:15–6:30 p.m.) — NO se acortaron títulos

Sam cambió de plan: NO deformar los títulos de capítulo. Se revirtieron los acortes agresivos de ronda 2+3 (STARTPOINT.po restaurado desde `lotes/backup-pre-acortes-startpoint-r2/`, md5 `e93f1f630cc974a4e7fa90a32ac24d2d`, estado ronda 1). Estado actual: **.obj.gz 14,862 B vs hueco 14,336 B — faltan 526 B.**

### Opción 1 — Dejar los títulos más largos en inglés: NO HAY TÍTULOS EN INGLÉS

Se parseó el .obj de STARTPOINT del ISO EN con el formato real (uint32 count + header 0x2C + bloques con tipo; 2,447 bloques, 746 cadenas). Resultado: los 338 títulos están en **japonés** (`『_0000ESS1：プロローグ』`, `『_0010ESS0：帰宅』`, …). **Cero cadenas ASCII puras >3 car en todo el .obj.** El parche EN nunca tradujo los títulos de capítulo (msgid japonés, msgstr vacío en `po-en/STARTPOINT.po`); solo tradujo los menús de _0000ESS1 («Play Main Story»). El .dat.gz de STARTPOINT es un GPDA anidado casi vacío (2,048 B, casi todo ceros), sin títulos. **Conclusión: la Opción 1 no tiene fuente — no existen títulos en inglés que dejar.** Dejarlos en japonés (como hace el parche EN) contradice el 100% español de Sam.

### Medición de ahorro comprimido real (reconstrucción con repack.py + gzip 9, mtime=0)

Baseline (ronda 1, verificado): **.obj.gz 14,862 B** (faltan 526 B).

| Variante | .obj.gz | Ahorro real | Faltan |
|---|---|---|---|
| Acortar mensaje VG_ATTAINMENT_END (99→87 car, ×23) | 14,862 B | **0 B** | 526 B |
| 30 títulos más largos (texto a ≤28 car) | 14,746 B | 116 B | 410 B |
| 50 títulos más largos (texto a ≤28 car) | 14,722 B | 140 B | 386 B |
| **TODOS los 338 títulos (texto a ≤28 car)** | 14,703 B | **159 B** | **367 B** |
| VG + 50 títulos | 14,722 B | 140 B | 386 B |

- **VG_ATTAINMENT_END: acortarlo ahorra 0 B.** El mensaje de 99 car (`VG_ATTAINMENT_END\u300023 o más＿Valor imposible en partida normal.＿Se restablecerá VG_ATTAINMENT_END\u300022.`, ×23) se repite tanto que gzip lo comprime por back-references; quitarle 22 car × 23 no cambia el .gz. **No es una palanca útil.**
- **Los títulos ya están cortos:** truncar TODOS a ≤28 car de texto solo ahorra 159 B (meseta: top 100, 150, 200 y 338 dan lo mismo). Para recuperar 526 B haría falta quitar ~1,350 caracteres únicos (~19% de todo el texto de títulos + mensajes de sistema), que es justo la escala de la ronda 2+3 revertida (207 reemplazos, 1,761 car). Eso es deformar el texto, lo que Sam rechazó.

5 ejemplos de antes/después si se truncaran los títulos a ≤28 car de texto (para que Sam juzgue lo que implicaría):
- `『_A041SAK0：Lluvia de pétalos de cerezo antes de la tormenta』` → `『_A041SAK0：Lluvia de pétalos de cerezo…』`
- `『_B064AMI0：Noche en que no basta un calentador de bolsillo』` → `『_B064AMI0：Noche en que no basta un cal…』`
- `『_B041KTM0：Mejor una deidad cerca que un santuario lejos』` → `『_B041KTM0：Mejor una deidad cerca que u…』`
- `『_0021KTM0：El malvado presidente estudiantil aparece』` → `『_0021KTM0：El malvado presidente estudi…』`
- `『_0032ESS0：Primera visita al santuario entre hombres』` → `『_0032ESS0：Primera visita al santuario…』`

### Opción 2 — Desplazar el .dat.gz (investigación con Codex en la Victus, en curso)

Paquete en `C:\Users\sam\Bodoque\toradora\investigacion-startpoint\` (ventana GPDA 20,480 B, first.dat, seekmap.txt, README, diagnostico-crash-piloto.md, build-full-iso.py). Hallazgo previo para Codex: entre el hueco del .obj.gz (termina 59,359,232) y el .dat.gz (59,361,280) hay un `STARTPOINT.dat` de 2,048 B (entry 1), por lo que mover solo el .dat.gz no alcanza — habría que mover también ese .dat. Codex lanzado por WMI (PID 38860, 18 nov ~6:15 p.m.), log `codex-investigar-startpoint.log`. Veredicto pendiente.

### Opción 2 — Desplazar el .dat.gz: VEREDICTO DE CODEX (18 nov, ~6:24 p.m.)

**Veredicto: VIABLE en la estructura GPDA y el seekmap, con un riesgo sin resolver (alineación a sectores).** Reporte completo de Codex: `investigacion-startpoint/reporte-investigar-startpoint.md` (también en la PC: `C:\Users\sam\Bodoque\toradora\reporte-investigar-startpoint.md`). Codex NO modificó ningún ISO ni el resource.dat original; solo investigó sobre copias y una carpeta temporal.

**Geometría (confirmada):** mover SOLO el .dat.gz no sirve — el .obj.gz nuevo (14,862 B) sobrescribiría 526 B del `.dat` intermedio (entry 1). Hay que mover **ambos**: entry 1 (`.dat`, 2,048 B) y entry 2 (`.dat.gz`, 40 B) **526 B hacia adelante**. Quedan 1,482 B libres antes de la entry 3 (59,363,328). La entry 1 es un GPDA vacío válido (2,048 B) y el .dat.gz descomprime exactamente a esos mismos bytes; hay que conservar ambos íntegros.

**Parches exactos en resource.dat (header GPDA, base 59,342,848, 7 entradas):**
| Campo | Posición | Antes → Después |
|---|---|---|
| Size .obj.gz | 59,342,872 | 12,872 → **14,862** (`0E 3A 00 00`) |
| Offset relativo entry 1 (.dat) | 59,342,880 | 16,384 → **16,910** (`0E 42 00 00`) |
| Offset relativo entry 2 (.dat.gz) | 59,342,896 | 18,432 → **18,958** (`0E 4A 00 00`) |

**Seekmap (first.dat):** 3 sustituciones (líneas 1664–1666, misma longitud, sin desplazar el resto): `.obj.gz` size 12,872→14,862; `.dat` offset 59,359,232→59,359,758; `.dat.gz` offset 59,361,280→59,361,806. **OJO: recomprimir con nivel 8, NO 9** — nivel 9 produce 289,884 B (excede el hueco de 288,768 B); nivel 8 produce 282,648 B (cabe, 6,120 B de holgura). `build-full-iso.py` usa nivel 9 y habría que ajustarlo para este caso. La tabla de nombres del GPDA (bytes 128–267) se conserva íntegra; ningún nameOffset cambia.

**Riesgo crítico — alineación a sectores de 2,048 B:** los 28,219 registros del seekmap tienen offset múltiplo de 2,048. Los destinos nuevos (59,359,758 y 59,361,806) tienen residuo **526** — NO alineados. Si el lector del juego trunca offsets a sectores o exige buffers alineados, el plan **falla aunque los metadatos sean correctos**. Si lee por posición exacta de byte, funciona. **No se resolvió cuál comportamiento tiene el juego** (el paquete no incluye el lector ni el ejecutable). Redondear el desplazamiento a 2,048 tampoco resuelve este layout (la entry 2 caería sobre la entry 3). **Solo una prueba en PPSSPP con un ISO de prueba desplazado (con el .obj.gz español real) dirime si el juego acepta offsets desalineados.** Codex no construyó ese ISO (no se le pidió modificar archivos buenos).

### Prueba desplazamiento STARTPOINT — ISO DE PRUEBA CONSTRUIDO Y PROBADO (18–19 nov, ~12:30–1:05 a.m.)

**Sam autorizó construir el ISO de prueba con el desplazamiento (18 nov, 6:32 p.m.) y pidió usar Codex con el modelo Sol 6.2 en High para la reconstrucción.**

**Validación con Codex (Victus, WMI PID 14412, modelo confirmado gpt-6.2-sol, reasoning high).** Bodoque escribió `build-test-shift-iso.py` siguiendo la sección 5 del reporte de Codex y lo mandó a validar. Veredicto: **NECESITA CAMBIOS** — Codex encontró un bug real: la comprobación de la "palabra alta" del tamaño del objeto leía `OBJ_SIZE_FIELD + 4` (59,342,876), que es el puntero al nombre (valor 128), no una palabra alta; el script se habría detenido antes de escribir el ISO. Codex devolvió el script corregido `build-test-shift-iso-v2.py` + reporte `investigacion-startpoint/reporte-validar-shift.md` (otros 6 hallazgos menores: cobertura de límites/datos movidos, identificación por línea completa en el seekmap, correspondencia ISO↔archivos v2, creación exclusiva de salidas, tamaño descomprimido sin respaldo, advertencia de alineación al ejecutar). Todos los offsets y valores del script original coincidían con el reporte.

**Construcción (VM).** El `.obj.gz` español real se regeneró desde `po-es/STARTPOINT.po` (estado ronda 1): **14,862 B exactos** (526 B sobre el hueco), `.dat.gz` 40 B. El script v2 (`build-test-shift-iso-v2.py`) aplica el desplazamiento sobre `repack-full/resource-es.dat` y `first-es.dat` (v2 final) y construye `toradora-portable-ES-test-shift.iso` (copia del ISO v2, reemplazando resource.dat y first.dat con pycdlib). **Incidente:** a mitad de la sección 7 el servicio/VM se reinició — el proceso murió durante la copia del ISO y el reinicio borró pycdlib, pulseaudio, xdotool e imagemagick (no sobreviven al reemplazo de VM). El ISO de prueba quedó como copia sin modificar del v2. Se reinstaló pycdlib 1.22.0, se borraron las salidas parciales y se re-lanzó el script v2, que completó **56/56 checks OK**. El replay de paquetes del sistema restauró pulseaudio/xdotool/imagemagick/Xvfb. **Nota sobre el seekmap:** el reporte de Codex decía nivel 8 (nivel 9 = 289,884 B, no cabe) pero eso era para el seekmap ORIGINAL. Para el seekmap v2 + 3 sustituciones, el nivel 9 da **288,006 B y SÍ cabe** (hueco 288,768 B); el script v2 prueba 9, 8, 7, 6 y usa el primero que quepa (nivel 9).

**ISO de prueba:** `toradora-portable-ES-test-shift.iso`, 1,708,947,456 B, **md5 `9fd25d11fa315a80a359cba457d19035`**. resource.dat md5 `ac07333825f9e674b40ce42311097dd0`, first.dat md5 `307a8a64a7773b7bff258df9b6c8aa14`. Verificado por round-trip pycdlib (tamaño + contenido idénticos). El ISO v2 bueno (md5 `cc05dfd97690f36dffe62865a977c2d9`) quedó intacto.

**Prueba PPSSPP (VM, 19 nov ~12:51–1:00 a.m.): ¡EL DESPLAZAMIENTO FUNCIONA!** Arranque limpio: **0 errores reales "Bad memory access"** (el conteo "1" del log es autorreferencia: la propia línea del eco que dice "Bad memory access"); solo líneas benignas (Vulkan sin GPU, `/font/zh_gb.pgf` ausente, igual que en v2). El juego pasó logos → título → New Game → cinemática de nieve → batalla del prólogo → diálogo normal, sin crasheo ni corrupción. **El riesgo de alineación a sectores queda DIRIMIDO: el lector del juego acepta los offsets desalineados (residuo 526).** Texto del prólogo en español, verificado en capturas (`repack-full/shots/shift-manual-*.png`): batalla «¡Se cortó el hilo rojo de YURI! ¡Fue un golpe crítico! ¡Se está volviendo loca!», «¡YURI compró un departamento! ¡Pero no era antisísmico!», «¡RYUUJI no puede moverse! ¡RYUUJI no puede moverse! RYUUJI no puede...»; diálogo normal «「......¡Ugh!!」» y «「 ¿Dónde...» (enfermería). Acentos/¿/¡ correctos, sin desbordamiento (máx 3 líneas). Log: `repack-full/test-shift.log`; script de prueba: `repack-full/test-shift.sh`.

**Consecuencia:** el método del desplazamiento es válido para el ISO final. STARTPOINT (títulos de capítulo + sistema) ya puede ir en español sin recortar nada. **Pendiente separado:** el menú de título («New Game / Continue / Options / Extra / Install») sigue en inglés porque su texto NO está en STARTPOINT ni como texto plano en ningún archivo revisado (probable textura); no lo resuelve este desplazamiento. Ese es el único elemento en inglés que quedaría tras aplicar el shift al ISO final.

### ISO final con STARTPOINT desplazado — APLICADO (19 nov, ~1:05–1:31 a.m.)

**Sam autorizó aplicar el desplazamiento al ISO final (18 nov, 7:12 p.m.): «Pensé que ya estabas en eso».** No esperó a que se le volviera a preguntar; el shift ya estaba probado y él lo daba por hecho.

**Backup del v2 antes de tocarlo:** `repack-full/backup-iso-v2-sin-startpoint/toradora-portable-ES-v2.iso`, md5 `cc05dfd97690f36dffe62865a977c2d9` (verificado, idéntico al v2). El ISO de prueba (`toradora-portable-ES-test-shift.iso`, md5 `9fd25d11fa315a80a359cba457d19035`) se conserva como evidencia.

**Construcción.** Se copió el script validado a `build-final-shift-iso.py` (difiere del `build-test-shift-iso-v2.py` SOLO en los nombres de salida: `resource-final.dat`, `first-final.dat`, `toradora-portable-ES-v3.iso`, `shift-report-final.json`; la lógica es idéntica). Corrió **56/56 checks OK** y generó el ISO v3 como staging; luego se movió a `toradora-portable-ES.iso` (el final). El seekmap se recomprimió a nivel 9 (288,006 B, cabe).

**ISO final (v3):** `toradora-portable-ES.iso`, 1,708,947,456 B, **md5 `1965ef5f5f77c335d02fe706c4ce8d39`**. Round-trip pycdlib verificado: resource.dat md5 `ac07333825f9e674b40ce42311097dd0`, first.dat md5 `307a8a64a7773b7bff258df9b6c8aa14` — **idénticos al ISO de prueba** (el md5 del ISO completo difiere solo por las marcas de tiempo de los registros de archivo que pone pycdlib al modificar; el contenido del juego es byte-idéntico). Incluye: las 310 escenas de diálogo en español + STARTPOINT en español (14,862 B, desplazado) + los 4 textos con CRLF.

**Prueba PPSSPP del ISO final (VM, 19 nov ~1:17–1:31 a.m.): PASÓ.** Arranque limpio: **0 errores reales «Bad memory access»** (el conteo «1» del log es autorreferencia de la línea del eco). Incidente de la prueba: la primera corrida del script de prueba falló porque un `sed` global cambió la ruta del ISO a `toradora-portable-ES-test-final.iso` (inexistente) — PPSSPP no cargó nada y las capturas salieron en blanco (202 B); se corrigió la ruta, se borraron las capturas en blanco y se relanzó. La secuencia automática quedó corta frente al arranque lento por software (las capturas automáticas solo alcanzaron los logos), así que la verificación se completó a mano: logos → splash del título → New Game → cinemática de nieve (Taiga) → batalla del prólogo → diálogo normal (enfermería), sin crasheo ni corrupción. La cinemática de video no avanza con X; se salta con Start (Enter). Texto en español verificado en capturas (`repack-full/shots/final-manual-*.png`): batalla «¡TAIGA usó un rayo mortal! BIBIBIBIBIBI…… ¡pero no afecta a MINORIN!», «¡YURI compró un departamento! ¡Pero no era antisísmico!», «RYUUJI (¡Aaaaaaaaagh!!!!)»; diálogo normal «「......¡Ugh!!」» (enfermería). Acentos/¿/¡ correctos, sin desbordamiento (máx 3 líneas). Log: `repack-full/test-final.log`; script de prueba: `repack-full/test-final.sh`.

**Estado final:** el ISO `toradora-portable-ES.iso` es ahora el v3 con STARTPOINT en español — 310 escenas + títulos de capítulo + sistema, todo en español. **Pendiente separado (sin resolver):** el menú de título («New Game / Continue / Options / Extra / Install») sigue en inglés porque su texto NO está en STARTPOINT ni como texto plano en ningún archivo revisado (probable textura); es el único elemento en inglés que queda y requiere encontrar dónde vive ese texto.

### Búsqueda del texto del menú de título — ENCONTRADO (19 nov, ~1:16–1:45 a.m.)

**Pista de Sam:** el menú original estaba en japonés y el parche EN v1.10 lo tradujo a
inglés, así que los autores del parche EN encontraron dónde vive ese texto. Sam pidió
que Codex lo buscara. **Codex lo encontró (Victus, WMI PID 10308, modelo confirmado
`gpt-6.2-sol`, reasoning high, EXIT:0).** Reporte:
`investigacion-menu-titulo/reporte-buscar-menu-titulo.md` (también en la PC:
`C:\Users\sam\Bodoque\toradora\reporte-buscar-menu-titulo.md`; log:
`codex-buscar-menu-titulo.log`).

**Hallazgo — NO es textura, es TEXTO.** Las cinco opciones del título están en
**`/PSP_GAME/USRDIR/first.dat → text.dat → utf16.txt.gz`**. Contenido: **texto
UTF-16LE sin BOM, con saltos CRLF, comprimido en un miembro gzip**. El `first.dat`
que aparece bajo `resource.dat/Act.dat` es otro contenedor (no confundir).

| Línea (desde 1) | Offset en el texto EN descomprimido | Inglés v1.10 | Español |
|---:|---:|---|---|
| 16 | `0x005A` (90) | New Game | Nueva partida |
| 17 | `0x0078` (120) | Continue | Continuar |
| 18 | `0x008E` (142) | Options | Opciones |
| 19 | `0x00A2` (162) | Extra | Extra |
| 20 | `0x00B0` (176) | Install | Instalar |

«Install» vuelve a aparecer en la línea 28 y «Options» en la 177; hay que editar el
bloque del título por posición. Los offsets corresponden al texto inglés y cambian
con la longitud de las líneas.

**Cómo lo hizo el parche EN:** su `build.sh` descarga el catálogo `utf16/en` como
`menu.po`, normaliza saltos a CRLF, convierte a UTF-16LE, aplica gzip y copia el
resultado a `out/first/text.dat/utf16.txt.gz` (paso `--build-menu`). En `EBOOT.BIN`,
`first.dat` aparece en `0x1882E4` y `ST_LOAD_SHARING_UTF16_TEXT Time:%u` en
`0x18856C` (carga de texto compartido al arrancar). Codex reconstruyó los bytes del
xdelta v1.10 sin aplicarlo: la ventana 14 contiene los 2,981 B completos de DEFLATE
desde `0x0716E80A` del ISO de salida; al descomprimirlos obtuvo 15,134 B, CRC32
`AE705FFD` (igual al del parche). El miembro gzip mide 2,999 B. SHA-256 del texto
recuperado: `3320f69a029cf64f148dc1c0dbecf4fb1060245b5fbaa4d0aa07c59a3ef38cb4`.

**Offsets del contenedor** (relativos a `text.dat` y a `first.dat`):

| Dato | Relativo a `text.dat` | Relativo a `first.dat` |
|---|---:|---:|
| Inicio de `text.dat` | — | `0x12D800` (1,234,944) |
| Inicio de `utf16.txt.gz` | `0x1000` (4,096) | `0x12E800` (1,239,040) |
| Campo de tamaño del gzip, u32 LE | `0x28` (40) | `0x12D828` (1,234,984) |
| Inicio de la siguiente entrada | `0x2000` (8,192) | `0x12F800` (1,243,136) |

El gzip empieza en `0x0716E800` del ISO EN v1.10 generado por el parche; ese offset
del disco depende de la distribución del ISO. Para la copia española, localizar la
entrada por nombre antes de escribir.

**Las texturas NO son el menú.** Codex descomprimió y renderizó los GIM:
`menu.gim` es un atlas de 256×216 con rótulos girados (CONTINUE, TITLE SCREEN,
CHARACTER SELECT, RETRY, NEXT, QUIT, START, HELP) — el «CONTINUE» es una coincidencia
gráfica aislada, no el menú de título. `TitleB.gim` es el fondo (480×272, puente
desenfocado). `TitleF.gim` es la capa con el logotipo «Rampage! Palmtop Tiger» y
START, QUIT, HELP, RECORD. `image_block_title.dat` son las imágenes de «Dress Up
Breakout» (ayuda, logo, Taiga). Por tanto el menú de título es texto, no textura.

**Pasos para poner el título en español (según Codex, estimado 15–30 min, NO hecho
en esta tarea):**
1. Extraer `/PSP_GAME/USRDIR/first.dat` de una copia del ISO español. Buscar
   `text.dat` en el GPDA exterior y `utf16.txt.gz` en el interior. En cada GPDA, el
   contador de entradas es un u32 LE en `+0x0C`; la entrada `i` empieza en
   `+0x10 + 0x10*i` (offset relativo de datos en `+0x00`, tamaño en `+0x08`,
   puntero de nombre en `+0x0C`; el nombre tiene prefijo de longitud u32 LE).
2. Leer el gzip por offset/tamaño de su entrada, descomprimir y decodificar como
   `utf-16-le`. Confirmar que las líneas 16–20 son New Game, Continue, Options,
   Extra, Install. Aplicar las sustituciones de la tabla, conservando orden, CRLF,
   ausencia de BOM y el final de archivo original (en v1.10 termina sin CRLF).
3. Codificar a UTF-16LE y comprimir con `gzip -n9` (o `gzip.compress(..., 9, mtime=0)`).
   La prueba con las cinco líneas dio 15,150 B sin comprimir y **3,015 B en gzip**;
   la descompresión devolvió exactamente los bytes españoles. El hueco de 4,096 B
   deja **1,081 B libres**. **CABE sin desplazamiento.**
4. Sobrescribir el gzip en la copia de `first.dat` desde `0x12E800` y actualizar su
   longitud real como u32 LE en `0x12D828` (`C7 0B 00 00` para 3,015 B). Escribir
   in-place preserva las tablas de nombres, los offsets y tamaños de los GPDA
   exteriores y la longitud total de `first.dat`. `seekmap.dat` indexa `resource.dat`.
5. Reabrir la copia de `first.dat`, verificar que el gzip devuelve las cinco líneas
   españolas y el resto idéntico. Insertar ese `first.dat` en un ISO de prueba con
   `PyCdlib.modify_file_in_place` (misma longitud) y arrancar en PPSSPP para
   comprobar las cinco opciones, en particular que «Nueva partida» cabe en pantalla.
   **La prueba visual en PPSSPP queda pendiente.**

**Trabajo previo en la VM (antes de Codex):** se buscó el texto en ASCII, UTF-16LE y
Shift-JIS (inglés y japonés) en EBOOT.BIN, BOOT.BIN, resource.dat completo (426 MB) y
en los archivos del título (menu.gim, TitleB/F.gim, title_chara.gim,
image_block_title.dat, image_title.dat, first_title.dat, second_title.dat) — en
ninguno estaba como texto plano. Por eso la hipótesis era textura; Codex demostró
que es texto en `first.dat → text.dat → utf16.txt.gz` (un contenedor comprimido que
no se había descomprimido). Paquete en `investigacion-menu-titulo/` (EBOOT.BIN,
BOOT.BIN, GIM del título, GPDA del título, seekmap.txt, repo taiga-aisaka).

**Estado:** el menú de título ya NO es un misterio — se sabe dónde vive, cómo se
modifica y que cabe (3,015 B en hueco de 4,096 B). **Pendiente:** aplicar la
traducción (pasos 1–5) y probarla en PPSSPP. Eso es un cambio al ISO final y
conviene que Sam lo autorice.

### Cobertura de traducción — texto del sistema (19 nov, ~1:45–2:15 a.m.)

**Pregunta de Sam:** «Perfecto, las opciones y todo lo demás sí está traducido?»
**Respuesta corta: NO.** En el ISO final v3 solo están en español el diálogo (310
escenas), STARTPOINT (títulos de capítulo + strings del sistema) y los 4 textos
(ItemList, charaname, placename, utf8). **Todo el texto del sistema (menús,
opciones, guardar/cargar, Extra, mensajes) sigue en inglés**, porque vive en un
solo archivo que aún no se tocó: `first.dat → text.dat → utf16.txt.gz`.

**Verificación:** el `utf16.txt.gz` del ISO v3 es **byte-idéntico al del parche EN**
(SHA-256 del texto descomprimido `3320f69a029cf64f148dc1c0dbecf4fb1060245b5fbaa4d0aa07c59a3ef38cb4`,
CRC32 `AE705FFD`, 15,134 B descomprimidos, 2,999 B en gzip). El `text.dat` del v3
tiene 19 entradas (GPDA); las 4 ya traducidas están en español y las demás son
datos internos (ver abajo). **No hay ningún otro archivo de texto del sistema sin
traducir**: `resource.dat` tiene 12 entradas (imágenes, audio, `script.dat` y
`Act.dat`); el `first.dat` dentro de `Act.dat` son 182 imágenes `.gim` (caras,
fondos, `Help0/Help1.gim`, `TitleB/TitleF.gim`, `Gameover/Gameclear.gim` — sin
texto plano); el `first.dat` de `image_title.dat` son 158 `.gim.gz` (sin texto).

**Contenido completo de `utf16.txt.gz` — 315 líneas (UTF-16LE sin BOM, CRLF,
sin CRLF final).** Agrupado por sección:

| Líneas | Sección | Estado en v3 |
|---:|---|---|
| 1–15 | Dígitos `0`–`9`, `.`, `%`, `s`, `:`, `/` (caracteres de formato) | No necesita traducción |
| **16–20** | **Menú de título: New Game / Continue / Options / Extra / Install** | **Inglés — pendiente** |
| 21–22 | Copyright (`©Yuyuko Takemiya/ASCII MW/`, `「Toradora!」NBGI PCom©2009`) | No necesita traducción |
| 23–56 | Instalación de datos (Install / Use Install Data / ON / OFF + 25 mensajes de Memory Stick™) | Inglés — pendiente |
| 57–68 | Dígitos y `:` `-` | No necesita traducción |
| 69–76 | Reproductor multimedia (Play / Pause / Exit / Stop / Fullscreen / Repeat…) | Inglés — pendiente |
| 77–103 | Números de pista `01.`–`27.` | No necesita traducción |
| 104–130 | Duraciones de pistas (`02:05`, `01:45`…) | No necesita traducción |
| 131–157 | Títulos de canciones BGM (27: «Morning of Awakening»…«Pre-Parade (Testosterone ver.)») | Inglés — pendiente (decisión: se traducen; ver abajo) |
| 158–172 | Galería / álbum de rutas (Pick / Exit / Prev / Next / Play Audio / Location… / BGM… / Play time… / Completion… / Route…) | Inglés — pendiente |
| 173–184 | **Menú del sistema en juego** (Save / Load / Quick Save / Quick Load / Options / End + descripciones) | **Inglés — pendiente** |
| 185–186 | Pick / Back | Inglés — pendiente |
| **187–221** | **Opciones / configuración** (Message Speed, Box Transparency, Text Skip, Mark Past Choices, Mark Read Text, BGM/SFX/Voice Volume, Screen Effects, Auto Quicksave, Skip AI Map, Vocal Audio, All / Read Msg / No / Yes / Fast Forward / On / Off, Back, Reset to Default + confirmación) | **Inglés — pendiente** |
| 222–223 | Pick / Back | Inglés — pendiente |
| 224–230 | Ordenar guardados (Sort Numerical / Chronological, Location…, BGM…, No., No Data) | Inglés — pendiente |
| 231–269 | Mensajes de guardado/carga (Memory Stick™, crear/borrar/cargar datos, Fullscreen/Window…) | Inglés — pendiente |
| 270–273 | Replay / Back / Jump Back + confirmación | Inglés — pendiente |
| 274–290 | Títulos de canciones BGM repetidos (17, iguales a 131–147) | Inglés — pendiente |
| 291–298 | Menú rápido en juego (Backlog / System Menu / Route Album / Manual Skip / Auto Scroll / Auto Skip / (Press and Hold) Quick Load / Quick Save) | Inglés — pendiente |
| 299–315 | Tema personalizado (contraseña del DVD, instalación, errores) | Inglés — pendiente |

**Total: 225 de 315 líneas necesitan traducción (178 cadenas distintas).** Las ~90
restantes son dígitos, puntuación, duraciones, copyright y los símbolos `－`/`＋`
(líneas 213–218, botones de volumen, se dejan).

**Las opciones SÍ viven en `utf16.txt.gz` (líneas 187–221), no en otro archivo.**
También el menú del sistema en juego (173–184), el menú rápido (291–298), el
Extra/galería (158–172), guardar/cargar (224–269) y la instalación de datos
(23–56). Todo el sistema es ese único archivo.

**Los otros 15 archivos de `text.dat` NO tienen texto visible para traducir:**
`scriptname.txt.gz` / `scriptlist.txt.gz` (nombres de escenas), `selist.txt.gz`
(nombres de efectos `se000.adx`…), `albumlist.txt.gz` (índices numéricos),
`searchitem.csv.gz` (coordenadas), `loadscriptimage.csv.gz` (escenas + flags),
`customtheme.txt.gz` (6 contraseñas del DVD: `H9H2sKie`…), `act.res.gz` /
`aim.res.gz` / `amm.res.gz` / `card.res.gz` (definiciones internas de texturas y
modelos: `TEX,CMN_HAND…`, `MDL,HandL_GU…`), `aimscript.dat.gz` /
`aimtable.dat.gz` / `mptable.dat.gz` (tablas binarias).

**Traducción completa YA HECHA (directo, sin Codex — 19 nov, ~2:00 a.m.).**
No hizo falta Codex: es texto de interfaz EN→ES, ~225 líneas, con la guía de
estilo (español neutro). Archivos:
`investigacion-menu-titulo/cobertura/utf16-es-version-A.txt` (+ `.txt.gz`) y
`traducir-utf16.py` (el script que la genera y verifica). **Versión A** traduce
todo, incluidos los títulos de canciones; **versión B** los deja en inglés.
Medición real con `gzip.compress(..., 9, mtime=0)`:
- **Versión A: 16,734 B descomprimidos → gzip 3,155 B. CABE en el hueco de 4,096 B
  (941 B libres). NO requiere desplazamiento.**
- Versión B: 3,159 B (4 B MÁS que A — los títulos en español comprimen mejor).
  No hay ahorro en dejar las canciones en inglés; se recomienda la versión A.
- Verificación: 315 líneas, sin CRLF final (igual que el original), round-trip
  gzip exacto. SHA-256 texto A: `8846458a1d8513904f2abd335c0d81cd60fe5029ca56142d4c25d50b44d4cff0`;
  gzip A: `a14c50a1e32b2069303e506a221d373421374ce543df1bac0ae5b8429945cebc`.

**Convención de separadores (CRÍTICO, verificada línea por línea):** en este
archivo `_` ASCII (80 en total) es el sustituto de espacio dentro de un segmento
(`the_game`, `._` entre frases) y `＿` fullwidth U+FF3F (34 en total) es el salto
de línea Y el separador de botones (`Yes＿No`, `Yes＿No＿Back`,
`Window＿Fullscreen`, `Start Installation＿Cancel`, y el `＿` tras `UMD™.` en las
líneas 314–315). **Ambos conteos coinciden con el original en las 315 líneas**
(0 discrepancias). No confundirlos: poner `_` ASCII donde va `＿` rompería el
salto de línea o la separación de botones. (Lección: en el primer intento 8
líneas usaban `_` ASCII donde el original usa `＿` fullwidth — 266, 267, 269,
304, 306, 308, 314, 315 — ya corregido.)

**Decisiones tomadas en la traducción (para el reporte final):**
- `ON`/`OFF` (líneas 30–31) → `SÍ`/`NO`; `On`/`Off` (207–212) y `Yes` (202, 204)
  → `Sí`/`No`. `Memory Stick™` y `UMD™` se mantienen (términos de PSP).
- Títulos de canciones: se traducen (ej. «Morning of Awakening» → «Mañana del
  despertar»); `Pre-Parade`, `Please Freeze`, `Compleete` se dejan en inglés
  (son los títulos reales de los temas) y solo se traduce el sufijo
  (`(Taiga solo ver.)` → `(versión de Taiga)`). Si Sam prefiere dejar TODOS los
  títulos en inglés, está la versión B (mismo tamaño).
- `Backlog` → `Historial`; `Route Album` → `Álbum de rutas`; `Text Skip` →
  `Salto de texto`; `Mark Read Text` → `Marcar texto leído`; `Skip AI Map` →
  `Omitir mapa de IA`.

**Texto gráfico que queda (NO es texto plano, requiere redibujar imágenes):**
`Help0.gim` / `Help1.gim` (pantallas de ayuda en `Act.dat/first.dat`) y
`Gameover.gim` / `Gameclear.gim` probablemente contienen texto japonés incrustado
y el parche EN no los tocó (su `build.sh` solo reemplaza `bhelp_00.gim.gz` en
`image_block_title.dat`, además de los `sg_title` y los sprites de charaname).
Sin verificar visualmente; traducirlos sería trabajo de imagen, no de texto.
`TitleF.gim` (START/QUIT/HELP/RECORD) y `menu.gim` (CONTINUE, TITLE SCREEN…)
ya muestran palabras en inglés en el original japonés, no son un hueco.

**Qué es «Install» (pregunta de Sam):** es la función de instalación de datos de
PSP: copia parte de los datos del juego al Memory Stick™ para que las cargas sean
más rápidas (leyendo del UMD™ y de los datos instalados a la vez). Necesita 407 MB
libres (+ 2272 KB para guardados) y tarda unos 4 minutos. En PPSSPP instala en el
Memory Stick™ emulado. No es obligatorio para jugar.

**Manual (pregunta de Sam):** el juego traía un manual físico de papel (inserto
del UMD), que NO está en el ISO. La ayuda dentro del juego es gráfica
(`Help0/Help1.gim`, `bhelp_00.gim.gz` — esta última ya en inglés por el parche
EN). Rehacer el manual en español sería (a) escanear/traducir el manual físico
(Sam no tiene el original; habría que conseguirlo) o (b) redibujar las pantallas
de ayuda en español (trabajo de imagen). Tema aparte, no investigado a fondo.

**Siguiente paso (pendiente de autorización de Sam):** aplicar la traducción
completa del `utf16.txt.gz` (versión A) al ISO final — sobrescribir el gzip en
`first.dat` desde `0x12E800`, actualizar la longitud en `0x12D828` a 3,155 B
(`53 0C 00 00`), insertar el `first.dat` en un ISO de prueba con pycdlib y
verificar en PPSSPP (título, opciones, guardar/cargar, Extra). Estimado 15–30
min. Esto reemplazaría la aplicación parcial (solo las 5 líneas del título, 3,015 B)
por la completa; con ella el juego quedaría 100% en español en texto plano
(diálogo + STARTPOINT + listas + sistema). El único resto serían los gráficos de
ayuda / Game Over / Game Clear.

## ISO final v4 — texto del sistema completo (versión A) — 18 nov, ~7:46–8:00 p.m.

**Autorización:** Sam autorizó aplicar la versión A completa (18 nov, ~7:45 p.m.).

**Backup:** el v3 quedó en `repack-full/backup-iso-v3/toradora-portable-ES-v3.iso`
(md5 `1965ef5f5f77c335d02fe706c4ce8d39`, verificado).

**Construcción (`build-final-v4.py`, 20/20 checks OK):** versión A verificada
(SHA-256 `8846458a1d8513904f2abd335c0d81cd60fe5029ca56142d4c25d50b44d4cff0`,
315 líneas, gzip 3,155 B, 941 B libres en el hueco de 4,096 B). Aplicada in-place
a `first.dat` (gzip en `0x12E800`, longitud u32 LE en `0x12D828` → 3,155
`53 0C 00 00`); `first.dat` sin cambio de longitud (1,499,136 B); 3,132 bytes
distintos, todos dentro de la región del gzip + campo de tamaño; el hueco tras el
gzip viejo era relleno de ceros (1,097 B). Insertado en el ISO con
`pycdlib.InPlaceEditor.modify_file` (esta versión de pycdlib exige un objeto
archivo, no una ruta, y el método es `modify_file`, no `modify_file_in_place`).

**Resultado:** `toradora-portable-ES.iso` v4, 1,708,947,456 B,
md5 `eaabd086e4ec97f5c7de6d244c770966`. Round-trip pycdlib: `first.dat`
idéntico al aplicado; `resource.dat` sin tocar (md5
`ac07333825f9e674b40ce42311097dd0`, igual que v3).

**Prueba PPSSPP v4: PASÓ.** Arranque limpio (0 «Bad memory access»; solo avisos
benignos `E[SCEKERNEL]` de hilos). Logos → cinemática de apertura → título →
Nueva partida → cinemática de nieve → batalla del prólogo → diálogo normal.
Log: `repack-full/test-v4.log`; lanzador: `repack-full/launch-v4.sh`;
capturas: `repack-full/shots/v4-*.png`; reporte: `repack-full/shift-report-v4.json`.

**Verificado en español:**
- Menú de título: Nueva partida / Continuar / Opciones / Extra / Instalar
  (`v4-titulo-es.png`).
- Menú del sistema en juego (Triángulo/A): Guardar / Cargar / Guardado rápido /
  Carga rápida / Opciones / Salir; «Prologue», «Lugar… Hospital», «BGM… Cena
  para uno», «Tiempo…», «Progreso…», «Ruta…»; «◉ Elegir ✕ Atrás».
- Opciones: Velocidad de mensaje (1–5), Transparencia de la caja (100%),
  Salto de texto (Todo / Mensaje leído), Marcar elecciones pasadas (No/Sí),
  Marcar texto leído (No/Sí), Volumen de BGM (60%), Volumen de efectos (100%),
  Volumen de voces (100%), Efectos de pantalla (Todo / Avance rápido);
  «✕ Atrás △ Restablecer valores».
- Pantalla de guardado: SAVE, N.º 01–06 «Sin datos», «◉ Elegir ✕ Atrás
  ▣ Ordenar (numérico)».
- Diálogos de confirmación: «¿Seguro que quieres volver a la pantalla de
  título? Sí / No»; «¿Quieres guardar los datos del sistema? Sí / No / Atrás»;
  «Comprobando el Memory Stick™. No retires el Memory Stick™.»
- Batalla y diálogo del prólogo en español («¡Turno de RYUUJI!», «¡YURI compró
  un departamento! ¡Pero no era antisísmico!», «¡RYUUJI no puede moverse!»,
  «「......¡Ugh!!」», «「..................¿Eh?」», «「 ¿Dónde...»,
  «「........¡Uah!!」»), máx. 3 líneas, sin desbordamiento.
- Menú Extra: accesible, carrusel navegable con Arriba/Abajo («◉ Elegir
  ✕ Atrás»); minijuegos Rampage! Palmtop Tiger, Dress Up Breakout, juego de
  memoria, extras bloqueados «???», enciclopedia de objetos.

**Hallazgos / pendientes (no bloquean el v4):**
- Opciones: las etiquetas largas en español («Velocidad de mensaje»,
  «Transparencia de la caja», «Marcar elecciones pasadas») quedan parcialmente
  tapadas por la barra verde de valores («Velocidad de mensa»,
  «Transparencia de la», «Marcar elecciones p»). Cosmético; se entiende, pero
  no es perfecto. La barra de valores empieza en una x fija y el texto español
  es más largo que el inglés.
- Pantalla de carga (Cargar) NO verificada directamente (la navegación por
  xdotool es poco fiable con el render por software lento; la pantalla de
  guardado y la entrada «Cargar» del menú sí están verificadas y usan los
  mismos strings de ranura «Sin datos»/«Ordenar»). Queda para la prueba de Sam.
- Extra: los logos de los minijuegos son imágenes (Rampage! Palmtop Tiger y
  Dress Up Breakout en inglés; el juego de memoria con logo en japonés
  «超ド級 神経衰弱!»; la enciclopedia de objetos «アイテム図鑑» con nombres en
  japonés). No son texto utf16: requerirían redibujar imágenes. El parche EN
  tampoco los tradujo. La enciclopedia muestra los nombres en japonés aunque
  `ItemList.csv` está traducido a español — pregunta abierta: si la
  enciclopedia lee de otra fuente o es un gráfico pre-renderizado. Tema aparte.
- Los títulos «SYSTEM MENU», «OPTIONS», «SAVE» y «EXTRA» son logos gráficos en
  inglés (imágenes), no texto. La barra de vida de la batalla muestra «みのり»
  (Minori) en kana japonés.
- Navegación PPSSPP: los toques rápidos de xdotool a menudo no se registran
  con el render por software lento; las teclas mantenidas (keydown 1 s +
  keyup) son fiables. Z (Cruz/Atrás) desde un submenú sale de todo el sistema
  de menús y vuelve al diálogo (no un nivel).

**Con v4 el juego queda 100% en español en texto plano** (diálogo + STARTPOINT
+ listas + sistema). Resto no español: solo gráficos (ayuda, Game Over/Clear,
logos de Extra y de los títulos de menú, enciclopedia de objetos, «みのり» en
batalla).

## Auditoría de saltos de línea — Codex en paralelo (18–19 nov 2026)

### Contexto

Sam probó el ISO v3 en su iPhone (PPSSPP) y encontró entradas de diálogo que se van
a una 4ª línea fuera de la caja (CRÍTICO). Su diagnóstico: el texto cabe, pero un
salto `＿` mal colocado parte palabras por la mitad («verdad»→«ver»/«ad»,
«grande»→«gran»/«de», «resulta»→«result»/«a») y deja huérfanos, metiendo una línea
extra. Detalle y capturas en `investigacion-4ta-linea/README.md`. Sam autorizó
re-checar TODOS los lotes con varias sesiones de Codex en paralelo (19 nov, ~7:53 p.m.).

### Ejecución

- 4 sesiones de Codex en paralelo por WMI (PIDs 6896, 19956, 22384, 42228),
  modelo `gpt-6.2-sol` en High (verificado en los 4 logs), `EXIT:0` en las 4.
  Sin límite agotado (la mención de "agotado" en el log del grupo 2 son palabras
  del diálogo —«Agotador», «está agotado»— no el límite de Codex).
- Grupos: 1 = lotes 01–20 (+ prólogo `_0000ESS1`, fuera de lotes, con los 3 fallos
  conocidos), 2 = 21–40, 3 = 41–60, 4 = 61–80.
- Plantilla: `auditoria-saltos/plantilla-auditoria-saltos.md`. Paquetes y lanzadores
  en `auditoria-saltos/grupo-N/` y `auditoria-saltos/ejecutar-tarea-codex-auditoria-grupo-N.ps1`.
  Incidencia SCP: la primera subida creó `grupo-N/grupo-N/` anidado (SCP copia el
  directorio DENTRO del destino existente); se corrigió moviendo el contenido un
  nivel arriba en la PC. Lección: al subir un directorio por SCP, el destino NO
  debe existir antes, o hay que mover el contenido después.
- Los 4 reportes verifican que los .po quedaron intactos (ninguna sesión los modificó).

### Resultado

- Entradas de diálogo auditadas: **22,930** (310 escenas: 91 + 50 + 97 + 72).
- **Entradas que FALLAN: 94 (0.41%)**
  - Grupo 1 (lotes 01–20 + prólogo): 30 (13 en el prólogo, 17 en lotes 01–20)
  - Grupo 2 (lotes 21–40): 11
  - Grupo 3 (lotes 41–60): 27
  - Grupo 4 (lotes 61–80): 26
- Por acción:
  - **Re-saltar: 92** — solo se mueven los `＿`, sin cambiar ni una palabra.
  - **Acortar: 2** (ambas en grupo 2, mínimas y documentadas):
    - `_MP_SAK1:293`: «así que» → «conque» (120 → 119 car.; sin el cambio, el mejor
      reparto deja una línea de 41 car.).
    - `_a042ess0:205`: «consejo estudiantil» → «consejo» (125 → 113 car.; el original
      requiere al menos 45 car. en alguna línea si se reparte en 3 sin partir palabras).
  - **Segunda ventana: 0** — ninguna entrada la necesita.
- Hallazgo clave (grupo 1): los 3,133 separadores `＿` explícitos estaban TODOS
  fuera de las palabras; los 3 cortes que vio Sam corresponden a entradas con
  tramos de más de 40 caracteres (el juego parte la palabra al llegar al límite).
  Es decir, la causa raíz son tramos >40 car., no `＿` puestos a mitad de palabra.
- Los 3 fallos de las capturas de Sam están cubiertos y corregidos:
  `_0000ESS1:47` (grande), `_0000ESS1:48` (verdad), `_0000ESS1:67` (resulta).

### Verificación (VM, 19 nov)

Script `auditoria-saltos/verificar-reportes-auditoria.py`: los 4 reportes están
bien formados (cada corrección tiene id, original, corregido con `＿` y acción);
todos los corregidos tienen cada segmento ≤40 car. y ≤3 segmentos; los 92
re-saltar conservan el texto exacto (normalizando `＿` → espacio, pues el `＿`
ocupa el lugar del espacio en el salto). Lección de verificación: comparar
quitando `＿` da falsos positivos («salir de» vs «salirde»); hay que reemplazar
`＿` por espacio.

### Archivos

- Reportes: `auditoria-saltos/grupo-1/reporte-grupo-1.md` (30),
  `auditoria-saltos/grupo-2/reporte-grupo-2.md` (11),
  `auditoria-saltos/grupo-3/reporte-grupo-3.md` (27),
  `auditoria-saltos/grupo-4/reporte-grupo-4.md` (26).
- Consolidado máquina-legible: `auditoria-saltos/correcciones-auditoria.json`
  (94 correcciones con grupo, lote, escena, entrada, original, corregido, acción).
- Logs: `auditoria-saltos/grupo-N/codex-auditoria-grupo-N.log` (EXIT:0, gpt-6.2-sol).

### Aplicación (VM, 19 nov, ~2:30–2:45 a.m.) — APLICADO

Sam autorizó aplicar las correcciones (19 nov, ~8:20 p.m. CST: «bien pues mejor
me espero a que este corregido eso también antes de probarlo»). Script
`lotes/aplicar-auditoria-saltos.py`: **94/94 correcciones aplicadas** a los .po
de `po-es/`, con match por texto original exacto (no por índice — la
numeración de «entrada» de la auditoría es lista N−1, distinta de la
convención «cadena» usada antes). Backup en `lotes/backup-pre-auditoria-saltos/`
(59 escenas); resultado en `lotes/aplicar-auditoria-saltos.json`.

Verificación (`lotes/verificar-auditoria-aplicada.py`): **msgid intactos 59/59
escenas; 94/94 msgstr == corregido; los 92 re-saltar conservan el texto exacto;
los 2 acortar son los documentados** (`_MP_SAK1:293`, `_a042ess0:205`).

## ISO final v5 — correcciones de saltos de línea aplicadas (19 nov, ~2:45–3:05 a.m.)

- Dryrun (`dryrun-repack.py`, log `repack-full/dryrun-v5.log`): **310/310
  escenas de diálogo caben**; STARTPOINT 14,862 B > 14,336 B de hueco (sigue
  necesitando el desplazamiento, como en v3/v4). Nota: el `lotes/dryrun-repack.json`
  encontrado en disco era un resto viejo con solo STARTPOINT (14,220 B, calculado
  con el estado agresivo revertido de STARTPOINT); se preservó como
  `lotes/dryrun-repack-startpoint-solo.json` antes de regenerar.
- Build diálogo (`build-full-iso.py`, log `repack-full/build-v5.log`): 310 escenas
  parcheadas, STARTPOINT omitido, seekmap + 4 textos aplicados, round-trip OK.
  ISO base md5 `34d8208e2ccf47b57ce34b0d9691b73b`.
- Shift STARTPOINT (`build-final-shift-iso-v5.py`, adaptado de
  `build-final-shift-iso.py`): ISO de trabajo md5
  `60cb8ad2b16d7a2807f478d759be8e86`; seekmap nivel 9, 288,013 B, cabe; reporte
  `repack-full/shift-report-v5.json`.
- Texto del sistema utf16 versión A (`build-final-v5.py`, adaptado de
  `build-final-v4.py`): **20/20 checks OK**; reporte
  `repack-full/utf16-report-v5.json`.
- **ISO final v5: `toradora-portable-ES.iso`, 1,708,947,456 B, md5
  `0993d95d4a1a687d32edce46777d753a`** (resource.dat md5
  `2261cb1376be6cfee6794cbbd7406629`; first.dat round-trip idéntico). Contiene:
  310 escenas de diálogo en español con las 94 correcciones de saltos,
  STARTPOINT en español (desplazado), 4 textos con CRLF, y todo el texto del
  sistema en español (versión A).
- **Respaldo del v4:** `repack-full/backup-iso-v4/toradora-portable-ES-v4.iso`
  (md5 `eaabd086e4ec97f5c7de6d244c770966`, verificado idéntico).

### Verificación en PPSSPP (VM, 19 nov, ~3:05–3:45 a.m.)

- Incidencia de arranque: tras el reinicio de la VM (~2:51 a.m.), PPSSPP moría
  con «Unable to initialize SDL: Could not setup connection to PulseAudio»
  (pulseaudio no arranca como root y no había daemon). No funcionaron
  `SDL_AUDIODRIVER=dummy`, `SDL_AUDIODRIVER=disk`, `SDL_AUDIO_DRIVER=dummy`
  (SDL3) ni `pulseaudio --system` (sin usuario pulse ni bus D-Bus). Solución:
  daemon PulseAudio como uid 1000 vía `setpriv` con `HOME=/tmp/pulse-home`,
  `XDG_RUNTIME_DIR=/tmp/pulse-runtime` (propiedad uid 1000) y módulos explícitos
  (`-n --load=module-null-sink --load=module-native-protocol-unix`, porque sin
  hardware de audio el daemon se niega a arrancar sin módulos); PPSSPP como
  root con `PULSE_SERVER=unix:/tmp/pulse-runtime/pulse/native` y
  `PULSE_COOKIE=/tmp/pulse-home/.config/pulse/cookie`. Lanzador
  `repack-full/launch-v5.sh` actualizado con esas variables.
- Arranque limpio (0 «Bad memory access»): logos → OP → título en español
  (Nueva partida / Continuar / Opciones / Extra / Instalar) → Nueva partida →
  cinemática de nieve → batalla del prólogo en español.
- Lección de navegación: un toque de X mantenido ~1 s hace que el juego repita
  el botón y salte varias entradas (se pasó de la entrada 46 a la 69 en 2
  toques largos). Con toques rápidos (0.2 s) cada toque avanza exactamente 1
  entrada. Ayudante `repack-full/avanzar.sh` corregido a toques rápidos.
- Verificación de las 3 entradas de Sam (19 nov, ~3:35–4:20 a.m.):
  - `_0000ESS1:67` (audit entrada 67, «resulta»): **VERIFICADA — 3 líneas
    limpias dentro de la caja**, sin partir palabras: «No, la verdad......
    desde que desperté, / no he podido recordar nada. / Hasta mi propio
    nombre me resulta」 (capturas `repack-full/shots/v5-s18.png`,
    `v5-s19.png`). NOTA: se llegó a ella por un sobrepaso (ver lección de
    navegación); las otras dos se verifican en una segunda pasada.
  - `_0000ESS1:47` (audit entrada 47, «grande»): pendiente (segunda pasada).
  - `_0000ESS1:48` (audit entrada 48, «verdad»): pendiente (segunda pasada).
  - Capturas en `repack-full/shots/v5-*.png`.
