from Productoporkilo import *
class Verduleria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo, peso):
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo, peso)
        self.__sector="Verduleria"
    
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
        print(f"- Sector: {self.__sector}\n -Nombre:{self.get_nombre_producto()}-\n - Precio por kg: ${self.get_precio()}\n - Peso real: {self.get_peso()} kg\n - Precio final: ${self.calcular_precio()}")


#COMO NOS VAN A EVALUAR. si esposibe que ellos agreguen en e main un objeto por ejmplo flyyn puff y que lo mandes a carniceria o si van a ser gente buena. si van a ser malos oreguntar como hcer porwque son infigas las posibilidades .