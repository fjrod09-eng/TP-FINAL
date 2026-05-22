class Deposito: 
    def __init__(self,lista_de_productos):
        self.__productos=lista_de_productos
    def contar_deposito(self,codigo):
        cont=0
        for i in self.__productos:
            if codigo==i.get_codigo():
                cont+=1
        
        return cont
    
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
    
            
            
        







        