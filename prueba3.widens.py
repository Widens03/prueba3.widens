import json
import datetime
ventas=[]
precios={
    "cuatro quesos":{"pequeña":5000, "mediana":9000, "familia":12000},
    "hawaiana":{"pequeña":6000, "mediana":9000, "familia":12000},
    "napolitana":{"pequeña":5500, "mediana":8500, "familia":11000},
    "pepperoni":{"pequeña":7000, "mediana":10000, "familia":13000}
}
descuentos={
    "estudiante diurno":0.12,
    "estudiante vespertino":0.14,
    "administrativo":0.10
}
   
def registrar_venta():
    tipo_cliente=input("ingrese el nombre del cliente: ")
    tipo_usuario=input("ingrese el tipo de usuario (estudiante diurno, estudiante vespertino, administrativo): ").lower()
    tipo_pizza=input("ingrese el tipo de pizza:(cuatro quesos, hawaiana, napolitana, pepperoni): ").lower()
    tamaño_pizza=input("ingrese el tamaño de la pizza (pequeña, mediana, familiar): ").lower()
       
    if tipo_pizza in precios and tamaño_pizza not in precios [tipo_pizza]:
        print("tipo de pizza o tamaño invalido.")
        return
        
    precio_base=precios[tipo_pizza][tamaño_pizza]
    descuento=descuentos.get(tipo_cliente, 0)
    precio_final=precio_base*(1-descuento)
        
         
    venta={
        "tipo_cliente": tipo_cliente,
        "tipo_pizza": tipo_pizza,
         "tamaño_pizza": tamaño_pizza,
        "tipo_usuario": tipo_usuario,
        "precio_final": precio_final,
        "fecha_hora": datetime.datetime.now().strftime("%y-%m-%d %d:%m:%s")
        }
    ventas.append(venta)
    print("venta registrada con exito")

def mostrar_ventas():
    if not ventas:
        print("no hay ventas registradas")
        return
    for venta in ventas:
        print(venta)
        
def buscar_ventas_por_cliente():
    cliente=input("Nombre del cliente a buscar: ")
    ventas_cliente=[venta for venta in ventas if venta["cliente"]==cliente]
    if not ventas_cliente:
        print(f"no se encontraron ventas para el cliente{cliente}.")
        return
    for venta in ventas_cliente:
        print(venta)
        
def guardar_ventas_por_cliente():
    cliente=input("Nombre del cliente a buscar: ")
    ventas_cliente=[venta for venta in ventas if venta["cliente"]==cliente]
    if not ventas_cliente:
        print(f"no se encontraron ventas para el cliente{cliente}.")
        return
    for venta in ventas_cliente:
        print(venta)
        
def guardar_ventas():
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo)
        print("ventas guadadas con exito.")
        
def cargar_ventas():
    global ventas
    try:
        with open("ventas.json", "r") as archivo:
            ventas=json.load(archivo)
        print("ventas cargadas con exito.")
    except FileNotFoundError:
        print("no se encontro el archivo de ventas.")
        
def generar_boleta():
    nombre_cliente=input("Nombre del cliente para generar la boleta{cliente}.")
    ventas_cliente=[venta for venta in ventas if venta["cliente"]==nombre_cliente]
    if not ventas_cliente:
        print(f"Factura para {nombre_cliente}:")
        total = 0
        for venta in ventas_cliente:
            print(venta)
            total += venta["precio_final"]
        print(f"Total a pagar: {total}")
    else:
        print("No se encontraron ventas para este cliente.")
        
def menu():
    while True:
        print("\n----menu de ventas----")
        print("1. registrar una venta.")
        print("2. mostrar todas las ventas.")
        print("3. buscar ventas por cliente.")
        print("4. guardar las ventas en un archivo.")
        print("5. cargar las ventas desde un archivo.")
        print("6. generar boleta.")
        print("7. salir.")
    
        opcion=input("seleccione una opcion")
    
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
              mostrar_ventas()
        elif opcion == "3":
              buscar_ventas_por_cliente()
        elif opcion == "4":
             guardar_ventas()
        elif opcion == "5":
              cargar_ventas()
        elif opcion == "6":
              generar_boleta()
        elif opcion == "7":
              print("Gracias por usar el sistema de ventas.")
              break
        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()
