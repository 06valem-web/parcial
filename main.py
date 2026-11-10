#Integrantes del grupo
#1. Jeronimo Bohorquez
#2. Sara Quintero

def mostrar_productos(productos):
    print("                 Catálogo de productos                 ")
    print("-" * 47)
    print("Código         Producto           Precio    Existencias")
    print("-" * 47)
    for codigo, info in productos.items():
        nombre, precio, existencias = info
        print(f"{codigo:<6} | {nombre:<17} | ${precio:<6} | {existencias}")

def registrar_producto(productos, pedido, codigo, cantidad):
    if codigo not in productos:
        print("Producto no encontrado.")
        return
    
    if cantidad <= 0:
        print("Cantidad no valida.")
        return
    
    nombre, precio, existencias = productos[codigo]
    
    if cantidad > existencias:
        print("No hay suficientes unidades disponibles.")
        return
    
    subtotal = precio * cantidad
    
    pedido.append((codigo, nombre, cantidad, subtotal))
    
    nuevas_existencias = existencias - cantidad
    productos[codigo] = (nombre, precio, nuevas_existencias)
    
    print(f"¡Producto agregado exitosamente! Subtotal: ${subtotal}")

def calcular_total(pedido):
    total = 0
    for item in pedido:
        total += item[3]
    
    if total >= 50000:
        descuento = total * 0.10
    else:
        descuento = 0
        
    total_final = total - descuento

    print("Resumen del pedido")
    print("-" * 42)
    print(f"{'Producto':<17}  {'Cantidad':<8}  {'Subtotal'}")
    print("-" * 42)
    for item in pedido:
        _, nombre, cantidad, subtotal = item
        print(f"{nombre:<17} | {cantidad:<8} | ${subtotal}")
        print("-" * 42)

    print(f"Total: ${int(total) if total.is_integer() else total}")
    print(f"Descuento: ${int(descuento) if descuento.is_integer() else descuento}")
    print(f"Total a pagar: ${int(total_final) if total_final.is_integer() else total_final}")
   

def principal():
    productos = {
        1: ("Cafe", 3000, 20),
        2: ("Jugo natural", 5000, 15),
        3: ("Sandwich", 8000, 10),
        4: ("Empanada", 2500, 25),
        5: ("Hamburguesa", 12000, 8)
    }
    
    pedido = []
    
    while True:
        print("\n")
        print("CAFETERIA")
        print("1. Mostrar productos")
        print("2. Agregar producto al pedido")
        print("3. Finalizar pedido")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            mostrar_productos(productos)
            try:
                codigo = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad deseada: "))
                registrar_producto(productos, pedido, codigo, cantidad)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        elif opcion == "3":
            if len(pedido) == 0:
                print("No ha registrado ningún producto en el pedido.")
            else:
                calcular_total(pedido)
                print("Gracias por su compra")
                break
        else:
            print("Opcion no valida, por favor seleccione una opción del 1 al 3.")

principal()