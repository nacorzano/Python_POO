"""
Producto [codigo, nombre, precio, stock]
contador de productos creados -- tiene que ser un atributo de instancia\
metodo de clase -->
    total_productos: devuelve el total de productos creados
    valor_total_stock: devuelve valor total del stock del producto
    metodo __str__
"""
from producto import Producto

repetir = True
prod = []
while(repetir):
    Producto.limpiar_pantalla()
    opcion = 0
    while (opcion < 1 or opcion > 6):

        opcion = int(input(f"*** MENU ***\n1. Introducir nuevo producto\n2. Ver total de productos creados\n3. Ver stock total en tienda\n4. Ver valor total del stock en tienda\n5. Ver listado de productos\n6. Salir\n\nSeleccion: "))

        if opcion == 1:
            t_codigo = int(input("Introduce codigo: ")); t_nombre = input("Introduce nombre: ")
            t_precio = float(input("Introduce precio: ")); t_stock = int(input("Introduce stock: "))
            prod.append(Producto(t_codigo, t_nombre, t_precio, t_stock))            
        
        elif opcion == 2:
            print(f"\nTotal productos creados: {Producto.total}")
            input("\nPulsa una intro para continuar")

        elif opcion == 3:
            aux = Producto.stock_total(prod)
            print(f"Total de stock en la tienda: {aux}")
            input("\nPulsa una intro para continuar")

        elif opcion == 4:
            aux = Producto.valor_total(prod)
            print(f"El valor total del stock en tienda es {aux}")
            input("\nPulsa una intro para continuar")

        elif opcion == 5:
            for aux in prod:
                print(aux)
            input("\nPulsa una intro para continuar")

        elif opcion == 6:
            repetir = False

        else:
            Producto.limpiar_pantalla()
