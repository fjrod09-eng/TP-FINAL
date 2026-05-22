from Inventario import *

class Carrito:
    def __init__(self):
        self.productos=[]

    def escanear_codigo(self,inventario,gondola):
        
        codigo=print("Ingrese el codigo del producto a buscar: ")
        product=Inventario.buscar_prod_por_cod()

        if product is None:
            print("Producto no encontrado")
            






