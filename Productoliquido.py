from Producto import *
from abc import ABC , abstractmethod
class Productoliquido(Producto,ABC):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo,cantidad_litros):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo)
        self.__cantidad_litros=cantidad_litros

    @abstractmethod
    def get_cantidad_litros(self):
        pass
    @abstractmethod
    def get_marca(self):
        pass
    @abstractmethod
    def get_nombre_producto(self):
        pass
    @abstractmethod
    def get_precio(self):
        pass
    @abstractmethod
    def get_codigo(self):
        pass
    @abstractmethod
    def get_umbral_minimo(self):
        pass
    @abstractmethod
    def mostrar_en_tablet(self):
        pass
    
    