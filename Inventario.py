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
    
    def reponer_desde_deposito(self, producto, deposito, gondola, codigo):
       
        stock_gondola = gondola.mostrar_stock_por_codigo(codigo)
        stock_deposito = deposito.contar_deposito(codigo)
        umbral = producto.get_umbral_minimo()

        print(f"Stock en góndola: {stock_gondola}")
        print(f"Stock en depósito: {stock_deposito}")
        print(f"Umbral mínimo: {umbral}")

        if stock_gondola >= umbral:
            print("La góndola tiene stock suficiente.")
            return

        if stock_deposito == 0:
            print("No hay stock en depósito para reponer.")
            return

        cantidad_necesaria = umbral - stock_gondola
        cantidad_real_a_reponer = min(cantidad_necesaria, stock_deposito)

        productos_repuestos = deposito.descontar_producto(codigo, cantidad_real_a_reponer)
        gondola.agregar_productos(productos_repuestos)

        print(f"Se repusieron {cantidad_real_a_reponer} productos desde depósito a góndola.")
        print(f"Nuevo stock en góndola: {gondola.mostrar_stock_por_codigo(codigo)}")
        print(f"Nuevo stock en depósito: {deposito.contar_deposito(codigo)}")


    def stock_total(self,gondola,deposito,codigo):
        stockgon=gondola.mostrar_stock_por_codigo(codigo)
        stockdep=deposito.contar_deposito(codigo)
        stocktotal=stockgon+stockdep
        return stocktotal

    def generar_pedido(self,producto:Producto,proveedor:Proveedor,gondola,deposito):
        stock_total=self.stock_total(gondola,deposito,producto.get_codigo())


        if stock_total<producto.get_umbral_minimo():
            cant_a_pedir=producto.get_umbral_minimo()-stock_total  
            
            nuevo_pedido=Pedido(producto,cant_a_pedir)

            print("Se genero un pedido")
            proveedor.recibir_pedido(nuevo_pedido)
        
        else:
            print("Hay suficiente stock, no hace falta generar un pedido. ")

    def controlar_stock_despues_de_venta(self, producto, proveedor, gondola, deposito):
        codigo = producto.get_codigo()

        stock_gondola = gondola.mostrar_stock_por_codigo(codigo)
        umbral = producto.get_umbral_minimo()

        if stock_gondola < umbral:
            self.reponer_desde_deposito(producto, deposito, gondola,codigo)

        self.generar_pedido(producto, proveedor, gondola, deposito)

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

                
        







    





    