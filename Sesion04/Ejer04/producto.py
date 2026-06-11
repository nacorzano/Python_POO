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
        total+=1


    def limpiar_pantalla():
       subprocess.run('cls', shell=True)
