from storage import cargar_info_gastos, cargar_config
from logica import agregar_presupuesto, agregar_gasto, ver_gastos, ver_por_categoria, ver_gastos_mes_y_presupuesto

def menu(): 
    gastos = cargar_info_gastos()
    config = cargar_config()
    presupuesto_mensual = config.get("presupuesto_mensual")
    
    agregar_presupuesto()

    while True:
        print("1. Agregar gastos")
        print("2. Ver gastos hasta la fecha")
        print("3. Ver gastos por categoría")
        print("4. Ver gastos del mes y presupuesto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_gasto(gastos)
        
        elif opcion == "2":
            ver_gastos(gastos)
        
        elif opcion == "3":
            ver_por_categoria(gastos)
            
        elif opcion == "4":
            ver_gastos_mes_y_presupuesto(gastos, presupuesto_mensual)
        
        elif opcion == "5":
            break
            
        else: 
            print("Respuesta no válida")

menu()