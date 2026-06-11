from libro import Libro

repetir = True
lib = []
while(repetir):
    Libro.limpiar_pantalla()
    opcion = 0
    while (opcion < 1 or opcion > 4):
        opcion = int(input(f"*** MENU ***\n1. Introducir nuevo libro\n2. Buscar libro con mas paginas\n3. Comparar paginas de dos libros\n4. Salir\n\nSeleccion: "))


        if opcion == 1:
            t_isbn = int(input("Introduce ISBN: "))
            t_tit = input("Introduce titulo: ")
            t_aut = input("Introduce autor: ")
            t_pag = int(input("Introduce numero de paginas: "))
            lib.append(Libro(t_isbn, t_tit, t_aut, t_pag))


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


        if opcion == 4:
            repetir = False

        else:
            Libro.limpiar_pantalla()



    
