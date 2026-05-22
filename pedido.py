from Producto import *
class Pedido:
    def __init__(self,producto:Producto,cantidad):
        self.__producto=producto
        self.__cantidad=cantidad


    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar_pedido(self):
        print(f"PEDIDO-> \n -Nombre del producto: {self.__producto.get_nombre_producto()} \n -Marca: {self.__producto.get_marca()}\n -Cantidad: {self.__cantidad}")



