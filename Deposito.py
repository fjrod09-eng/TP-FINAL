class Deposito: 
    def __init__(self,lista_de_productos,stock_kilos=None):
        self.__productos=lista_de_productos
        
        if stock_kilos is None:
            self.__stock_kilos={}

        else: 
            self.__stock_kilos=stock_kilos


    def contar_deposito(self,codigo):
        cont=0
        for i in self.__productos:
            if codigo==i.get_codigo():
                cont+=1
        
        return cont
    
    def agregar_stock_kilos(self, codigo, kilos):
        self.__stock_kilos[codigo] = kilos


    def mostrar_stock_kilos(self, codigo):
        return self.__stock_kilos.get(codigo, 0)


    def descontar_producto_por_peso(self, codigo, peso):
        stock_disponible = self.mostrar_stock_kilos(codigo)

        if stock_disponible == 0:
            print("No hay stock disponible en kilos en depósito.")
            return 0

        if peso > stock_disponible:
            print(f"No hay {peso} kg disponibles en depósito.")
            print(f"Stock disponible en depósito: {stock_disponible} kg")
            return 0

        self.__stock_kilos[codigo] = stock_disponible - peso

        print(f"Se retiraron {peso} kg del depósito.")
        print(f"Nuevo stock en depósito: {self.__stock_kilos[codigo]} kg")

        return peso


    def agregar_stock_kilos_existente(self, codigo, kilos):
        stock_actual = self.mostrar_stock_kilos(codigo)
        self.__stock_kilos[codigo] = stock_actual + kilos
    
    def descontar_producto(self,codigo, cantidad):
        stock_disponible=self.contar_deposito(codigo)
        
        if stock_disponible>=cantidad:
            eliminados=0
            nueva_lista=[]
            productos_retirados=[]

            for producto in self.__productos:
                if producto.get_codigo()==codigo and eliminados<cantidad:
                    productos_retirados.append(producto)
                    eliminados+=1

                else:
                    nueva_lista.append(producto)

            self.__productos=nueva_lista
            print(f"Se retiraron {cantidad} productos del deposito")
            return productos_retirados
        
        else:
            print("No hay suficiente stock en deposito")
            return []


    def agregar_productos(self,lista_productos):
        for producto in lista_productos:
            self.__productos.append(producto)
    

            
            
        







        