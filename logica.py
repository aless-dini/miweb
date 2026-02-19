from storage import guardar_info_gastos, guardar_config

def agregar_presupuesto():
    presupuesto =int(input("Agrega el presupuesto mensual: "))
    config = {"presupuesto_mensual": presupuesto}
    guardar_config(config)
    print("Presupuesto guardado correctamente")
    
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
    
def ver_gastos(gastos):
    for gasto in gastos:
        print("Precio -> $", gasto["precio"])
        print("Categoría ->", gasto["categoria"])
        print("Descripción ->", gasto["descripcion"])
        print("Fecha ->", gasto["fecha"])
        print("-" * 20)
        
def ver_por_categoria(gastos):
    respuesta = input("Qué categoría quieres ver?: ").lower().strip()
    encontrado = False
    
    for gasto in gastos:
        encontrado = True
        if gasto["categoria"] == respuesta:
            print("Precio -> $", gasto["precio"])
            print("Categoría ->", gasto["categoria"])
            print("Descripción ->", gasto["descripcion"])
            print("Fecha ->", gasto["fecha"])
            print("-" * 20)
            
    if not encontrado:
        print("Categoría no encontrada")

def ver_gastos_mes_y_presupuesto(gastos, presupuesto_mensual):
    respuesta = input("De qué mes quieres ver los gastos?: ")
    total = 0
    
    for gasto in gastos:
        try:
            partes = gastos["fecha"].split("/")
            mes = partes[1].strip().zfill(2)
        except (IndexError, ValueError):
            continue
        
        if respuesta == mes:
            total += gasto["precio"]
    
    restante = presupuesto_mensual - total
    
    if restante < 0:
        print("HAS SUPERADO EL PRESUPUESTO MENSUAL")
            
    print(f"Gastos del mes {mes}: ${total:,}".replace(",", "."))
    print(f"Presupuesto mensual: {presupuesto_mensual:,}".replace(",", "."))
    print(f"Restante: {restante:,}".replace(",", "."))


        
        
    
        