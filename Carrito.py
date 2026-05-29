from Inventario import *
from miserrores import *



class Carrito:
    def __init__(self):
        self.productos_en_carrito=[]

    def escanear_codigo(self,inventario,gondola):
        
        
        product=inventario.buscar_prod_por_cod()

        if product is None:
            print("Búsqueda cancelada.")
            return []

        codigo = product.get_codigo()
        

        if product is None:
            print("Producto no encontrado")
            return []

        
        if product.get_sector() != gondola.get_sector():
            print(f"ERROR: El producto {product.get_nombre_producto()} pertenece a {product.get_sector()}, no a {gondola.get_sector()}.")
            print("No se puede agregar desde esta góndola.")
            return []
        
        else: 
            print("Producto encontrado")
            print(f"Nombre del producto: {product.get_nombre_producto()}")
            print(f"Marca del producto: {product.get_marca()}")
            print(f"Precio del producto: {product.get_precio()}")
            while True:
                respuesta=input("Desea llevar el producto?(si/no) ")
                if respuesta.lower() == "si" or respuesta == "no":
                    break
                else:
                    print("Respuesta no válida. Ingrese 'si' o 'no'.")

            if respuesta.lower() == "no":
                print("Producto no agregado al carrito")
                return []
            
            if respuesta.lower() == "si":
                
                
                    if product.get_sector() == "Carniceria" and product.get_venta_por() == "unidad":
                        while True:
                            try:

                                cantidad=int(input("Cuantas unidades quiere llevar de ese producto: ").strip())
                                if  cantidad<=0 :
                                    raise valorError
                                break

                            except ValueError:
                                print("La cantidad debe ser un numero entero  ")
                                return []
                        
                            except valorError:
                                print("La cantidad debe ser mayor a 0 ")
                                return []

                        productos_retirados=gondola.descontar_producto(codigo,cantidad)
                        for i in productos_retirados:
                            self.productos_en_carrito.append(i)

                        return productos_retirados
                        
                                
                    
                    elif product.get_sector() in ["Carniceria", "Verduleria", "Fiambreria"]:
                        while True:
                            try:
                                peso = float(input("Cuantos kg quiere llevar?: ").strip().replace(",", "."))

                                if peso <= 0:
                                    raise valorError

                                break

                            except ValueError:
                                print("El peso debe ser un numero. Ejemplo: 2.5")

                            except valorError:
                                print("El peso debe ser mayor a 0.")

                        kg_descontados = gondola.descontar_producto_por_peso(codigo, peso)

                        if kg_descontados > 0:
                            producto_comprado=product.crear_compra_por_peso(kg_descontados)
                            self.productos_en_carrito.append(producto_comprado)

                            print(f"Se agregó {kg_descontados} kg de {producto_comprado.get_nombre_producto()} al carrito.")
                            return [producto_comprado]

                        else:
                            return []

                
                    else:

                        while True:
                            try:
                                cantidad = int(input("Cuanta cantidad quiere llevar de ese producto: ").strip())

                                if cantidad <= 0:
                                    raise valorError

                                break

                            except ValueError:
                                print("La cantidad debe ser un numero entero.")

                            except valorError:
                                print("La cantidad debe ser mayor a 0.")

                        productos_retirados = gondola.descontar_producto(codigo, cantidad)

                        for i in productos_retirados:
                            self.productos_en_carrito.append(i)

                        return productos_retirados

    def mostrar_carrito(self):
        print("\n--- PRODUCTOS EN CARRITO ---")

        if len(self.productos_en_carrito) == 0:
            print("El carrito está vacío.")
            return

        productos_agrupados = {}

        for producto in self.productos_en_carrito:
            codigo = producto.get_codigo()

            if codigo not in productos_agrupados:
                productos_agrupados[codigo] = {"producto": producto,"cantidad": 1,"total": producto.get_precio_final()}
            else:
                productos_agrupados[codigo]["cantidad"] += 1
                productos_agrupados[codigo]["total"] += producto.get_precio_final()

        for codigo in productos_agrupados:
            producto = productos_agrupados[codigo]["producto"]
            cantidad = productos_agrupados[codigo]["cantidad"]
            total = productos_agrupados[codigo]["total"]

            
            print(f"Producto: {producto.get_nombre_producto()}")
            print(f"Marca: {producto.get_marca()}")
            print(f"Código: {producto.get_codigo()}")

            if producto.get_sector() in ["Carniceria", "Verduleria", "Fiambreria"] and not (
                producto.get_sector() == "Carniceria" and producto.get_venta_por() == "unidad"):
                print(f"Peso: {producto.get_peso()} kg")
                print(f"Precio por kg: ${producto.get_precio()}")
                print(f"Precio final: ${producto.get_precio_final()}")
            else:
                print(f"Cantidad: {cantidad}")
                print(f"Precio por unidad: ${producto.get_precio()}")
                print(f"Subtotal: ${total}")


                

                    


            






