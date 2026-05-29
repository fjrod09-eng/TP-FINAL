from Productoporkilo import *
class Carniceria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, precio, codigo, umbral_minimo, peso=None,tipo_de_corte=None, venta_por="kilo"): #ponemos =kilo para que por defecto sea por kilo, como caso particular qwue sesa unidad
        super().__init__(marca, nombre_producto, precio, codigo, umbral_minimo, peso)
        self.__tipo_de_corte=tipo_de_corte
        self.__sector="Carniceria"
        self.__venta_por=venta_por
        

    def get_sector(self):
        return self.__sector
    def get_peso(self):
        return self._peso
    def get_tipo_de_corte(self):
        return self.__tipo_de_corte
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
    def get_venta_por(self):
        return self.__venta_por
    
    def set_peso(self,nuevo_peso):
        self._peso=nuevo_peso
    
    def calcular_precio(self):
        if self.get_peso() is None:
            return self.get_precio()
        else:
            return self.get_precio() * self.get_peso()
        
    def get_precio_final(self):
        return self.calcular_precio()
    
    def crear_compra_por_peso(self, peso_comprado):
        return Carniceria(self.get_marca(),self.get_nombre_producto(),self.get_precio(),self.get_codigo(),self.get_umbral_minimo(),peso_comprado,self.__tipo_de_corte,self.__venta_por)

    
    def mostrar_en_tablet(self):
        if self.__venta_por == "unidad":

            print(
                f"- Sector: {self.__sector}\n- Producto: {self.get_nombre_producto()}\n- Precio por unidad: ${self.get_precio()}")
        else:

            print(
                f"- Sector: {self.__sector}\n - Tipo de corte: {self.__tipo_de_corte}\n- Precio por kg: ${self.get_precio()}\n- Peso real: {self.get_peso()} kg\n- Precio final: ${self.get_precio_final()}")
            