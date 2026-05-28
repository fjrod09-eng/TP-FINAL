from Inventario import *
from Producto import *
class Gondola:

    def __init__(self, sector, productos,stock_kilos=None):
        self.__sector = sector
        self.__productos = productos

        if stock_kilos is None:
            self.__stock_kilos={}
        else:
            self.__stock_kilos=stock_kilos
    


    def get_sector(self):
        return self.__sector
    
    def agregar_stock_kilos(self, codigo, kilos):
        self.__stock_kilos[codigo] = kilos

    def mostrar_stock_kilos(self, codigo):
        return self.__stock_kilos.get(codigo, 0)
    def mostrar_productos(self):
        print(f"Góndola: {self.__sector}")

        for producto in self.__productos:
            print(f"{producto.get_codigo()} \n- {producto.get_nombre_producto()} \n-{producto.get_marca()}\n-${producto.get_precio()}")

    def contar_producto(self, codigo):
        contador = 0

        for producto in self.__productos:
            if producto.get_codigo() == codigo:
                contador += 1

        return contador
    
    def agregar_stock_kilos_existente(self, codigo, kilos):
        if codigo in self.__stock_kilos:
            self.__stock_kilos[codigo] += kilos
        else:
            self.__stock_kilos[codigo] = kilos

        print(f"Se agregaron {kilos} kg a la góndola.")
        
    def descontar_producto_por_peso(self, codigo, peso):
        stock_disponible = self.mostrar_stock_kilos(codigo)

        if stock_disponible == 0:
            print("No hay stock disponible en kilos.")
            return 0

        if peso > stock_disponible:
            print(f"No hay {peso} kg disponibles.")
            print(f"Stock disponible: {stock_disponible} kg")

            respuesta = input(f"Desea llevar los {stock_disponible} kg disponibles? ").strip().lower()

            if respuesta == "si":
                peso = stock_disponible

            elif respuesta == "no":
                print("No se retiro ningun producto de la gondola.")
                return 0

            else:
                print("Palabra invalida")
                return 0

        self.__stock_kilos[codigo] = stock_disponible - peso

        print(f"Se retiraron {peso} kg de la gondola.")
        print(f"Nuevo stock en gondola: {self.__stock_kilos[codigo]} kg")

        return peso

    def descontar_producto(self, codigo, cantidad):

        stock_disponible = self.contar_producto(codigo)

        if stock_disponible==0:
            print("No hay stock disponible ")
            return []
        
        if stock_disponible<cantidad:
            print(f"No hay {cantidad} unidades disponibles")
            print(f"Stock disponible: {stock_disponible}")

            respuesta=input(f"Desea llevar las {stock_disponible} unidades que hay? ")
            

            if respuesta.strip().lower()=="si":
                cantidad=stock_disponible
            
            elif respuesta.strip().lower()=="no":
                print("No se retiro ningun producto de la gondola")
                return []
            
            else: 
                print("Palabra invalida")
                return []


        eliminados = 0 
        nueva_lista = []
        productos_a_retirar=[]

        for producto in self.__productos:

            if producto.get_codigo() == codigo and eliminados < cantidad:
                productos_a_retirar.append(producto)
                eliminados += 1

            else:
                nueva_lista.append(producto)

        self.__productos = nueva_lista

        print(f"Se retiraron {cantidad} productos de la góndola.")
        return productos_a_retirar
        

    def agregar_productos(self,lista_productos):
        for producto in lista_productos:
            self.__productos.append(producto)


    def mostrar_stock_por_codigo(self, codigo):

        stock = self.contar_producto(codigo)
        return stock






            




        



    