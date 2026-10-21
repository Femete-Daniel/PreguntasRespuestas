# El reto FEMETE: aplicación de concurso (sin Internet)

Todo vive en una sola carpeta:

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La aplicación. No se toca nunca. |
| `FEMETE_150_preguntas.csv` | **Tus preguntas.** Es lo único que editas. |
| `logo.png` | Logo de FEMETE (cabecera y pantalla inicial). Si falta, la app muestra el texto «FEMETE». |
| `preguntas.js` | Copia del CSV que la app lee al abrirse con doble clic. Se regenera. |
| `convertir_csv.py` | Regenera `preguntas.js` desde el CSV (opcional, necesita Python 3). |

## Usar la aplicación
Doble clic en `index.html` (Chrome, Edge, Firefox o Safari). No necesita Internet ni instalar nada.
Pulsa **Comenzar**. Atajos: `1/2/3` o `A/B/C` eligen respuesta; `Enter` comprueba y avanza.

## Formato del CSV
Columnas: `ID; Tema; Pregunta; Opción A; Opción B; Opción C; Correcta; Respuesta correcta; Referencia`.
- La fila de cabecera es opcional. Sin ella, la app asume ese orden de columnas.
- Separador `;`, `,` o tabulador (se detecta solo). Vale UTF-8 o «ANSI» de Excel.
- `Correcta` debe ser A, B o C. Si existe `Respuesta correcta`, debe coincidir con el texto de esa opción.
- `Referencia` no se muestra en pantalla.

## Actualizar las preguntas (elige una vía)
**A. Sin programar (la más sencilla).** Edita el CSV y guárdalo (en Excel: *Guardar como → CSV*).
Abre `index.html` → **Cargar CSV…** → elige el archivo. Se usa al instante.
Para que quede fijo: **Guardar como preguntas.js** y copia ese archivo sobre el de la carpeta.

**B. Con Python.** Edita el CSV, ejecuta `python3 convertir_csv.py` y recarga `index.html`.

**C. Lectura directa del CSV.** En la carpeta ejecuta `python3 -m http.server 8000`
y abre `http://localhost:8000/index.html`. La app lee el CSV directamente en cada carga, sin conversión.
(Un navegador abierto con doble clic no puede leer archivos de la carpeta por seguridad; por eso existen A y B.)

La pantalla inicial indica de dónde vienen los datos, cuántas preguntas hay y, si el CSV tiene errores,
la fila e ID exactos. Con errores no se permite empezar.

## Reglas de juego
- Bloques de 3 preguntas por participante, contador propio que empieza en 0.
- Cada pregunta se puntúa una vez; tras comprobar queda bloqueada.
- El resultado aparece tras comprobar la 3.ª respuesta (botón «Ver resultado»).
- Sin repetir preguntas en la sesión. Si el total no es múltiplo de 3, las sobrantes se avisan al inicio y al final.
- Al terminar: «Reiniciar sesión» baraja de nuevo (pide confirmación). La casilla «Orden aleatorio» permite usar el orden del CSV.
- Cerrar o recargar la página reinicia la sesión.
