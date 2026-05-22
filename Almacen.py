from Galletitas import *
from Gaseosas import *
from Golosinas import *
from Perfumeria import *
from Electrodomesticos import *
from Carniceria import *
from Verduleria import *
from Fiambreria import *


class Almacen: 

    def __init__(self):
        self.__productos = []
        self.__galletitas=["pitusas","sonrisas","porteñitas"]
        self.__gaseosas=["coca cola", "sprite", "manaos naranja"]
        self.__perfumeria=["lavandina","jabon en polvo", "jabon tocador"]
        self.__golosinas=["caramelos fizz","caramelos masticables frutales", "caramelos de miel"]
        self.__electrodomesticos=["freidora de aire", "pava electrica", "cafetera"]
        self.__carniceria = ["asado", "vacio", "milanesa","chorizo","morcilla"]
        self.__verduleria = ["papa", "tomate", "manzana"]
        self.__fiambreria = ["jamon", "queso", "salame"]

    def reconocer_tipo(self, nombre_producto):

        nombre = nombre_producto.lower()

        if nombre in self.__galletitas:
            return "galletitas"

        elif nombre in self.__gaseosas:
            return "gaseosas"

        elif nombre in self.__golosinas:
            return "golosinas"

        elif nombre in self.__perfumeria:
            return "perfumeria"

        elif nombre in self.__electrodomesticos:
            return "electrodomesticos"

        elif nombre in self.__carniceria:
            return "carniceria"

        elif nombre in self.__verduleria:
            return "verduleria"

        elif nombre in self.__fiambreria:
            return "fiambreria"

        else:
            return None

    def registrar_producto(self, tipo, marca, nombre_producto, precio, codigo, umbral_minimo,peso=None, tipo_de_corte=None, tipo_de_fiambre=None,cantidad_litros=None):

        tipo = tipo.lower() 
        
        tipo_reconocido = self.reconocer_tipo(nombre_producto)

        if tipo_reconocido is None:
            print("Producto no reconocido por el almacén.")
            return None

        if tipo != tipo_reconocido:
            print(f"ERROR: {nombre_producto} pertenece a {tipo_reconocido}, no a {tipo}.")
            return None

        if tipo == "galletitas": #creo un objeto galletitas

            producto = Galletitas(marca,nombre_producto,precio,codigo,umbral_minimo)

        elif tipo == "gaseosas":

            producto = Gaseosas(marca,nombre_producto,precio,codigo,umbral_minimo,cantidad_litros)

        elif tipo == "golosinas":
            producto = Golosinas(marca,nombre_producto,precio,codigo,umbral_minimo)

        elif tipo == "perfumeria":
            producto = Perfumeria(marca,nombre_producto,precio,codigo,umbral_minimo,cantidad_litros)

        elif tipo == "electrodomesticos":
            producto = Electrodomesticos(marca,nombre_producto,precio,codigo,umbral_minimo)

        elif tipo == "carniceria":
            if nombre_producto.lower() in ["chorizo", "morcilla"]:
                producto = Carniceria(marca,nombre_producto,precio,codigo,umbral_minimo,venta_por="unidad")

            else:
                producto = Carniceria(marca,nombre_producto,precio,codigo,umbral_minimo,peso,tipo_de_corte,venta_por="kilo")

        elif tipo == "verduleria":
            producto = Verduleria(marca,nombre_producto,precio,codigo,umbral_minimo,peso)
    
        elif tipo == "fiambreria":
            producto = Fiambreria(marca,nombre_producto,precio,codigo,umbral_minimo,peso,tipo_de_fiambre)

        else:
            print("No existe tal producto")
            return None

        self.__productos.append(producto) #guarda el producto registrado en el sector correspondiente

        print("Producto  registrado en gondola .")
        print(type(producto))

        return producto