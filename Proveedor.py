from pedido import *
class Proveedor:
    def __init__(self,nombre_proveedor):
        self.__nombre_provedor=nombre_proveedor

    def get_nombre_proveedor(self):
        return self.__nombre_provedor
    
    def recibir_pedido(self,Pedido:Pedido):
        print(f"El proveedor {self.__nombre_provedor} recibio un pedido de reposicion")

        Pedido.mostrar_pedido()
        return Pedido.get_cantidad()

        