from abc import ABC, abstractmethod

class Producto(ABC):
    # Clase abstracta para todos los productos del supermercado.
    def __init__(self,marca,nombre_producto, precio, codigo, umbral_minimo):
        self._codigo = codigo
        self._marca = marca
        self._nombre_producto = nombre_producto
        self._precio = precio
        self._umbral_minimo = umbral_minimo

    
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
    


    @abstractmethod #metodo abstracto de todas las clases hijas
    def mostrar_en_tablet(self):
        pass
    
    
    
