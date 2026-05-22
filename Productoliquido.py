from Producto import *
class Productoliquido(Producto):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo,cantidad_litros):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo)
        self.__cantidad_litros=cantidad_litros

    def get_cantidad_litros(self):
        return self.__cantidad_litros
    def get_marca(self):
        return self._marca
    def get_nombre_producto(self):
        return self._nombre_producto
    def get_precio(self):
        return self._precio
    def get_codigo(self):
        return self._codigo
    def get_umbral_minimo(self):
        return self._umbral_minimo
    
    def mostrar_en_tablet(self):
        pass
    
    