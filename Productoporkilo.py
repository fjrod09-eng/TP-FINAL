from Producto import *
from abc import ABC, abstractmethod
class Producto_por_kilo(Producto):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo,peso):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo)
        self._peso=peso

    @abstractmethod
    def get_peso(self):
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
    def set_peso(self,nuevo_peso):
        pass
    
    @abstractmethod
    def calcular_precio(self):
        pass
    @abstractmethod
    def get_precio_final(self):
        pass
    @abstractmethod
    def mostrar_en_tablet(self):
        pass
