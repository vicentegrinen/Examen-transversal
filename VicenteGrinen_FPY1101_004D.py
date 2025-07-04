Producto = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']

}

stock = {'8475HD': [387990,10],
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0]
}

def Stock(marca):
    total = 0
    for modelo, datos in Producto.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
    print(f"Stock total de {marca.capitalize()}: {total}")

def Busqueda(precio_m, precio_M):
    try:
        precio_m = int(precio_m)
        precio_M = int(precio_M)
    except ValueError:
        print("ingresar valores enteros Por favor")
        return
    
    Resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if precio_m <= precio <= precio_M and cantidad > 0:
            marca = Producto[modelo][0]
            Resultados.append(f"{marca}===={modelo}")

    if Resultados:
        for item in sorted(Resultados):
            print(item)
    else:
        print("No hay noteboock en ese rango de precio.")

def Actualizar(modelo, precio_nuevo):
    if modelo in stock:
        stock[modelo][0] = precio_nuevo
        return True
    else:
        return False
    

while True: 
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "4":
            print("\nPrograma finalizado.")
            break
        elif opcion == "1":
            marca = input("\nIngrese marca a consultar: ")
            Stock(marca)
        elif opcion == "2":
            precio_m = input("Ingrese precio minimo: ")
            precio_M = input("Ingrese precio maximo: ")
            Busqueda(precio_m, precio_M)
        elif opcion == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    precio_nuevo = int(input("Ingrese precio nuevo: "))
                    if precio_nuevo <= 0:
                        print("El precio debe tener un valor mayor a cero")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero para el precio")
                    continue

                if Actualizar(modelo, precio_nuevo):
                    print("Precio actualizado")
                else:
                    print("El modelo no existe")
                
                repetir = input("¿Desea actualizar otro precio? (s/n)").lower()
                if repetir != "si":
                    break
        else:
            print("Debe seleccionar una opcion valida")



# Fin Del programa
# Que tenga un Buen dia