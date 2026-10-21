#!/usr/bin/env python3
"""Copia el CSV de preguntas a preguntas.js (el archivo que lee index.html al abrirlo con doble clic).
Uso:  python3 convertir_csv.py [archivo.csv]
Sin argumento usa FEMETE_150_preguntas.csv (o el primer .csv de esta carpeta).
No interpreta las preguntas: solo embebe el texto del CSV; index.html lo valida y lo entiende."""
import sys, json, glob, os, datetime
here = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "FEMETE_150_preguntas.csv")
if not os.path.exists(src):
    found = sorted(glob.glob(os.path.join(here, "*.csv")))
    if not found: sys.exit("No se encuentra ningún archivo .csv en esta carpeta.")
    src = found[0]
raw = open(src, "rb").read()
try: text = raw.decode("utf-8-sig")
except UnicodeDecodeError: text = raw.decode("cp1252")   # CSV guardado desde Excel en «ANSI»
out = os.path.join(here, "preguntas.js")
with open(out, "w", encoding="utf-8") as f:
    f.write("window.PREGUNTAS_DATA = " + json.dumps({"archivo": os.path.basename(src),
        "generado": datetime.datetime.now().isoformat(timespec="seconds"), "csv": text}, ensure_ascii=False) + ";\n")
print(f"OK: {len(text.splitlines())} líneas de '{os.path.basename(src)}' guardadas en {out}")
