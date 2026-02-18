import json

def guardar_info_gastos(gastos):
    with open("gastos.json", "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, ensure_ascii=False, indent=4)

def cargar_info_gastos():
    try:
        with open("gastos.json", "r", encoding="utf-8") as archivo:
            json.load(archivo)
    except FileExistsError:
        return []
        
def cargar_config():
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.load(f)
    except FileNotFoundError:
        return {"presupuesto: 0"}