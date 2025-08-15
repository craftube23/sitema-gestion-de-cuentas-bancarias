import json
import os

ARCHIVO_DATOS = "data/data.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump({}, archivo, indent=4)
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        