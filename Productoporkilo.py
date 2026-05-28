from Producto import *
class Producto_por_kilo(Producto):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo,peso):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo)
        self.__peso=peso

    def get_peso(self):
        return self.__peso
    
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
    def set_peso(self,nuevo_peso):
        self.__peso=nuevo_peso
    
    def calcular_precio(self):
        if self.__peso is None:
            return self.get_precio()
        else:
            return self.get_precio() * self.__peso
        
    def get_precio_final(self):
        return self.calcular_precio()
        
    def mostrar_en_tablet(self):
        pass
