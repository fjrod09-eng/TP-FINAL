from Productoporkilo import *
class Fiambreria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo, peso,tipo_de_fiambre):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo, peso)
        self.__tipo_de_fiambre=tipo_de_fiambre
        self.__sector="Fiambreria"

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
    def get_peso(self):
        return self._peso

    def get_tipo_de_fiambre(self):
        return self.__tipo_de_fiambre
    
    def set_peso(self,nuevo_peso):
        self._peso=nuevo_peso
    
    def calcular_precio(self):
        if self.get_peso() is None:
            return self.get_precio()
        else:
            return self.get_precio() * self.get_peso()
        
    def get_precio_final(self):
        return self.calcular_precio()
    
    def mostrar_en_tablet(self):
        print(f"- Sector: {self.__sector}\n -Nombre:{self.get_nombre_producto()}- Tipo de corte: {self.__tipo_de_fiambre}\n - Precio por kg: ${self.get_precio()}\n - Peso real: {self.get_peso()} kg\n - Precio final: ${self.get_precio_final()}")
    
    def crear_compra_por_peso(self, peso_comprado):
        return Fiambreria(self.get_marca(),self.get_nombre_producto(),self.get_precio(),self.get_codigo(),self.get_umbral_minimo(),peso_comprado,self.__tipo_de_fiambre)