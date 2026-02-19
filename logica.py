from storage import guardar_info_gastos

def agregar_gasto(gastos):
    precio = float(input("Escribe el precio: "))
    categoria = input("Escribe la categoría: ")
    descripcion = input("Escribe una descripción: ")
    fecha = input("Escribe la fehca: ")
    
    gasto = {
        "precio": precio,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha" : fecha
    }
    
    gastos.apppend(gasto)
    guardar_info_gastos(gastos)
    print("Gasto agregado correctamente")
    
def ver_gastos():
    for gasto in gastos:
        print("Precio -> $", gasto["precio"])
        print("Categoría ->", gasto["categoria"])
        print("Descripción ->", gasto["descripcion"])
        print("Fecha ->", gasto["fecha"])
        print("-" * 20)
    
        