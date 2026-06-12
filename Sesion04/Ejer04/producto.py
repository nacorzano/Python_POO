"""
Producto [codigo, nombre, precio, stock]
contador de productos creados -- tiene que ser un atributo de instancia\
metodo de clase -->
    total_productos: devuelve el total de productos creados
    valor_total_stock: devuelve valor total del stock del producto
    metodo __str__
"""
import subprocess
class Producto:
    total = 0

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre        
        self.precio = precio
        self.stock = stock
        Producto.total+=1

    def __str__(self):
        return f"\nCodigo: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}\n\n" 

    def stock_total(prod):
        x = 0
        for i in prod:
            x += i.stock
        return x

    def valor_total(prod):
        x = 0
        for i in prod:
            x += (i.precio * i.stock)
        return x

    def limpiar_pantalla():
       subprocess.run('cls', shell=True)
