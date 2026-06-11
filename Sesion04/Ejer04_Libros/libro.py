import subprocess

class Libro:
    def __init__(self, isbn, titulo, autor, paginas):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas    
    def __str__(self):
        return f"*** DATOS STR ***\nISBN: {self.isbn}\nTitulo: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.paginas}"



    def limpiar_pantalla():
       subprocess.run('cls', shell=True)



    def maximopaginas(lib):        
        max = 0        
        for i in lib:                     
            if i.paginas > max:
                max = i.paginas
                maxtit = i.titulo               
        print(f"\nEl libro con mas paginas tiene {max} paginas y es {maxtit}\n")


    def haylibros(lib):
        if len(lib) > 0:
            return True
        return False



    def comparapaginas(lib):        
        print("Estos son los libros registrados")
        x = 0
        for i in lib:
             print(f"\n{x+1} -> {i.titulo}")                                         
             x+=1   
        print(f"\n")
        r = True
        while(r):
            #print(f"Longitud de la lista: {len(lib)}")         
            l1 = int(input("Elige el primero libro a comparar: "))
            l2 = int(input("Elige el segundo libro a comparar: "))
            if (l1 > 0 and l1 <= len(lib)) and (l2 > 0 and l2 <= len(lib)):
                r = False
            else:
                print(f"\nSeleccion incorrecta. Vuelve a intentarlo\n")
        l1-=1; l2-=1
        if lib[l1].paginas > lib[l2].paginas:
            print(f"\n{lib[l1].titulo} tiene mas paginas\n")
        elif lib[l2].paginas > lib[l1].paginas:
                print(f"\n{lib[l2].titulo} tiene mas paginas\n") 
        else:
            print(f"\nLos libros seleccionados tienen el mismo numero de paginas")

            

            
    
