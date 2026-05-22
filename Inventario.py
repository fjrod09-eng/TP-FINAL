from Producto import *
from Proveedor import *
from pedido import *
from Gondola import *
from Deposito import *
class Inventario():
    def __init__(self):
        self.productos=[] #lista(marca,nombre,...)
    
    def agregar_producto_a_inventario(self,producto:Producto):
        self.productos.append(producto)
    
    def reponer_desde_deposito(self,deposito,gondola,cantidad,codigo):
        print(f"Stock en gondola: {gondola.mostrar_stock_por_codigo(codigo)}")
        if gondola.mostrar_stock_por_codigo(codigo)==0 and deposito.contar_deposito(codigo)>=cantidad:
            productos_repuestos=deposito.descontar_producto(codigo,cantidad)
            gondola.agregar_productos(productos_repuestos)
            print(f"Se repusieron {cantidad} en la gondola")
            
        else:
            print("No hay suficiente stock en deposito del producto para reponer")  


    def stock_total(self,gondola,deposito,codigo):
        stockgon=gondola.mostrar_stock_por_codigo(codigo)
        stockdep=deposito.contar_deposito(codigo)
        stocktotal=stockgon+stockdep
        return stocktotal

    def generar_pedido(self,producto:Producto,proveedor:Proveedor,gondola,deposito):
        stock_total=self.stock_total(gondola,deposito,producto.get_codigo())


        if stock_total==0 or stock_total<producto.get_umbral_minimo():
            cant_a_pedir=producto.get_umbral_minimo()-stock_total  
            if cant_a_pedir<=0:
                cant_a_pedir=producto.get_umbral_minimo()
            
            nuevo_pedido=Pedido(producto,cant_a_pedir)

            print("Se genero un pedido")
            proveedor.recibir_pedido(nuevo_pedido)
        
        else:
            print("Hay suficiente stock, no hace falta generar un pedido. ")

    def monitorear_producto(self):
        nombre=input("Ingrese el nombre del producto a monitorear: ")
        
        for i in self.productos:
            if i.get_nombre_producto().lower()==nombre.lower():
                print(f"Producto encontrado:{i.get_nombre_producto()}")
                print(f"Stock en gondola: {i.get_stock_gondola()}")
                print(f"Stock en deposito: {i.get_stock_deposito()}")

                return 
            
    
        print("Producto no encontrado")
        
    def buscar_prod_por_cod(self,codigo):
        
        for i in self.productos:
            if i.get_codigo()==codigo:
                
                return i
            
        print("Producto no encontrado")
        return None

                
        







    





    