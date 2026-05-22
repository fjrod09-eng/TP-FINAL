from Inventario import *
from miserrores import *


class Carrito:
    def __init__(self):
        self.productos_en_carrito=[]

    def escanear_codigo(self,inventario,gondola):
        
        codigo=input("Ingrese el codigo del producto a buscar: ")
        product=inventario.buscar_prod_por_cod(codigo)

        if product is None:
            print("Producto no encontrado")
        else: 
            print("Producto encontrado")
            print(f"Nombre del producto: {product.get_nombre_producto()}")
            print(f"Marca del producto: {product.get_marca()}")
            print(f"Precio del producto: {product.get_precio()}")
            respuesta=input("Desea llevar el producto? ")

            try:
                
                if respuesta.lower()=="si":
                    try: 
                        cantidad=int(input("Cuanta cantidad quiere llevar de ese producto: "))
                        if type(cantidad)== type(1.1):
                            raise valorError
                        else: 
                            productos_retirados=gondola.descontar_producto(codigo,cantidad)
                            for i in productos_retirados:
                                self.productos_en_carrito.append(i)
                            return self.productos_en_carrito
                                
                    except valorError:
                        print("La cantidad debe ser un entero")
                elif respuesta.lower()=="no":
                    return
                else:
                    if respuesta.lower()!="si" and respuesta.lower()!="no": 
                        raise siError
            except siError:
                print("Palabra no valida")
            



                

                    


            






