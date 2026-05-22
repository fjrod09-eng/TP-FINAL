from Producto import *
class Electrodomesticos(Producto):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo)
        self.__sector="Electrodomesticos"
    
    def get_sector(self):
        return self.__sector
    
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

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}\n -Stock en gondola: {self.get_stock_gondola()}\n -Precio: {self.get_precio}")

    