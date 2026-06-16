class Instrumento:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def tocar(self):
        return f"Tocando el instrumento {self.tipo}"

    def afinar(self):
        return f"Afinando instrumento {self.tipo}"

class Flauta(Instrumento):
        def __init__(self, nombre, tipo, modelo):
            super().__init__(nombre)
            self.tipo = "Flauta"
            self.modelo = modelo
        
        def flauta_tocar(self):
            super().tocar()
            print(f"Soplando\n\n")

class Flauta(Instrumento):
    pass

class Guitarra(Instrumento):
    pass

class GuitarraElectrica(Guitarra):
    pass

class Tambor(Instrumento):
    pass

