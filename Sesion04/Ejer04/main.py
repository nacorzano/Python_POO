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
    while (opcion < 1 or opcion > 4):
        opcion = int(input(f"*** MENU ***\n1. Introducir nuevo producto\n2. Buscar libro con mas paginas\n3. Comparar paginas de dos libros\n4. Salir\n\nSeleccion: "))


        if opcion == 1:
            t_codigo = int(input("Introduce codigo: "))
            t_nombre = input("Introduce nombre: ")
            t_precio = input("Introduce precio: ")
            t_stock = int(input("Introduce stock: "))
            prod.append(Producto(t_codigo, t_nombre, t_precio, t_stock))
            print(f"Total productos: {Producto.total}")
        
        elif opcion == 4:
            repetir = False

        else:
            Libro.limpiar_pantalla()
"""
        if opcion == 2:
            x = Libro.haylibros(lib)
            if x == True:
                Libro.maximopaginas(lib)
            else:
                print(f"Aun no hay libros registrados\n")
            input("\nPulsa una intro para continuar")


        if opcion == 3:
            x = Libro.haylibros(lib)
            if x == True:
                Libro.comparapaginas(lib)
            else:
                print(f"Aun no hay libros registrados\n")
            input("\nPulsa intro para continuar")

"""
        
