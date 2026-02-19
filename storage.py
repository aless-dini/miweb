import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_GASTOS = os.path.join(BASE_DIR, "gastos.json")
RUTA_CONFIG = os.path.join(BASE_DIR, "config.json")

def guardar_info_gastos(gastos):
    with open(gastos.json, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, ensure_ascii=False, indent=4)

def cargar_info_gastos():
    if not os.path.exists(RUTA_GASTOS):
        return []
    with open(RUTA_GASTOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_config(config):
    with open("config.json", "w", encoding="utf-8") as archivo:
        json.dump(config, archivo, ensure_ascii=False, indent=4)
        
def cargar_config():
    if not os.path.exists(RUTA_CONFIG):
        return {"presupuesto_mensual": 0}
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)