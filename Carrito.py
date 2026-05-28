from Inventario import *
from miserrores import *


class Carrito:
    def __init__(self):
        self.productos_en_carrito=[]

    def escanear_codigo(self,inventario,gondola):
        
        codigo=input("Ingrese el codigo del producto a buscar: ").strip()
        product=inventario.buscar_prod_por_cod(codigo)

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
            respuesta=input("Desea llevar el producto? ")

            try: #carniceria unidad, carniceria peso y prod normal
                
                if respuesta.lower()=="si":

                    if product.get_sector() in ["Carniceria", "Verduleria", "Fiambreria"]:

                        if product.get_sector()== "Carniceria" and product.get_venta_por()=="unidad":

                            try: 
                                cantidad=int(input("Cuantas unidades quiere llevar de ese producto: ").strip())
                                if  cantidad<=0 :
                                    raise valorError

                                productos_retirados=gondola.descontar_producto(codigo,cantidad)
                                for i in productos_retirados:
                                    self.productos_en_carrito.append(i)


                                return productos_retirados
                        
                                
                            except ValueError:
                                print("La cantidad debe ser un numero entero  ")
                                return []
                        
                            except valorError:
                                print("La cantidad debe ser mayor a 0 ")
                                return []
                    
                        else:
                            try:
                                peso = float(input("Cuantos kg quiere llevar?: ").strip().replace(",", "."))

                                if peso <= 0:
                                    raise valorError

                                kg_descontados = gondola.descontar_producto_por_peso(codigo, peso)

                                if kg_descontados>0:
                                
                                    product.set_peso(kg_descontados)
                                    self.productos_en_carrito.append(product)

                                    print(f"Se agregó {peso} kg de {product.get_nombre_producto()} al carrito.")
                                    return [product]

                                else:
                                    return []

                            except ValueError:
                                print("El peso debe ser un numero. Ejemplo: 2.5")
                                return []

                            except valorError:
                                print("El peso debe ser mayor a 0")
                                return []

                    else:
                        try:

                            cantidad = int(input("Cuanta cantidad quiere llevar de ese producto: ").strip())

                            if cantidad <= 0:
                                raise valorError

                            productos_retirados = gondola.descontar_producto(codigo, cantidad)

                            for i in productos_retirados:
                                self.productos_en_carrito.append(i)

                            return productos_retirados

                        except ValueError:
                            print("La cantidad debe ser un numero entero")
                            return []

                        except valorError:
                            print("La cantidad debe ser mayor a 0")
                            return []



                elif respuesta.lower()=="no":
                    print("Producto no agregado al carrito")
                    return []
                

                else: 
                        raise siError
            except siError:
                print("Palabra no valida")
                return []

    def mostrar_carrito(self):
            print("\n--- PRODUCTOS EN CARRITO ---")

            if len(self.productos_en_carrito) == 0:
                print("El carrito está vacío.")
            else:
                for producto in self.productos_en_carrito:
                    print(f"{producto.get_codigo()} - {producto.get_nombre_producto()} - {producto.get_marca()} - ${producto.get_precio()}")
            



                

                    


            






