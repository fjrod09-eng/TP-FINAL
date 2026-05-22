from Productoporkilo import *
class Fiambreria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo, peso,tipo_de_fiambre):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo, peso)
        self.__tipo_de_fiambre=tipo_de_fiambre
        self.__sector="Fiambreria"

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

    def get_tipo_de_fiambre(self):
        return self.__tipo_de_fiambre
    
    def mostrar_en_tablet(self):
        print(f"- Sector: {self.__sector}\n -Nombre:{self.get_nombre_producto()}- Tipo de corte: {self.__tipo_de_fiambre}\n - Precio por kg: ${self.get_precio()}\n - Peso real: {self.get_peso()} kg\n - Precio final: ${self.calcular_precio()}")