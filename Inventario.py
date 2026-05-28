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
    
    def producto_es_por_kilo(self, producto):
        if producto.get_sector() == "Verduleria":
            return True

        if producto.get_sector() == "Fiambreria":
            return True

        if producto.get_sector() == "Carniceria":
            if producto.get_venta_por() == "kilo":
                return True

        return False
    
    def reponer_desde_deposito(self, producto, deposito, gondola):
        codigo = producto.get_codigo()
        umbral = producto.get_umbral_minimo()

        if self.producto_es_por_kilo(producto):
            stock_gondola = gondola.mostrar_stock_kilos(codigo)
            stock_deposito = deposito.mostrar_stock_kilos(codigo)

            print(f"Stock en góndola: {stock_gondola} kg")
            print(f"Stock en depósito: {stock_deposito} kg")
            print(f"Umbral mínimo: {umbral} kg")

            if stock_gondola >= umbral:
                print("La góndola tiene stock suficiente.")
                return

            if stock_deposito == 0:
                print("No hay stock en depósito para reponer.")
                return

            cantidad_necesaria = umbral - stock_gondola
            cantidad_real_a_reponer = min(cantidad_necesaria, stock_deposito)

            kilos_repuestos = deposito.descontar_producto_por_peso(codigo, cantidad_real_a_reponer)
            gondola.agregar_stock_kilos_existente(codigo, kilos_repuestos)

            print(f"Se repusieron {kilos_repuestos} kg desde depósito a góndola.")

        else:
            stock_gondola = gondola.mostrar_stock_por_codigo(codigo)
            stock_deposito = deposito.contar_deposito(codigo)

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
       
    

    def stock_total(self, producto, gondola, deposito):
        codigo = producto.get_codigo()

     
        if producto.get_sector() in ["Carniceria", "Verduleria", "Fiambreria"] and not (producto.get_sector() == "Carniceria" and producto.get_venta_por() == "unidad"):
            stock_gondola = gondola.mostrar_stock_kilos(codigo)
            stock_deposito = deposito.mostrar_stock_kilos(codigo)
        else:
            stock_gondola = gondola.mostrar_stock_por_codigo(codigo)
            stock_deposito = deposito.contar_deposito(codigo)

        return stock_gondola + stock_deposito

    def generar_pedido(self,producto:Producto,proveedor:Proveedor,gondola,deposito):
        stock_total=self.stock_total(producto,gondola,deposito)


        if stock_total<producto.get_umbral_minimo():
            cant_a_pedir=producto.get_umbral_minimo()*2
            
            nuevo_pedido=Pedido(producto,cant_a_pedir)

            print("Se genero un pedido")
            cantidad_recibida=proveedor.recibir_pedido(nuevo_pedido)
            if self.producto_es_por_kilo(producto):
                deposito.agregar_stock_kilos_existente(producto.get_codigo(), cantidad_recibida)
                print(f"Se agregaron {cantidad_recibida} kg al depósito.")
            
            else:
                nuevos_productos=[]

                for _ in range(cantidad_recibida):
                    nuevos_productos.append(producto)

                deposito.agregar_productos(nuevos_productos)

                print(f"Se agregaron {cantidad_recibida} unidades al depósito.")
                print(f"Nuevo stock en depósito: {deposito.contar_deposito(producto.get_codigo())}")

        else:
            print("Hay suficiente stock, no hace falta generar un pedido. ")

    def controlar_stock_despues_de_venta(self, producto, proveedor, gondola, deposito):
        self.reponer_desde_deposito(producto, deposito, gondola)
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

                
        







    





    