from abc import ABC, abstractmethod
class Inventario():
    def __init__(self):
        self.productos=[] #diccionario(marca,nombre,...)
    
    def agregar_producto_a_inventario(self,producto:Producto):
        self.productos.append(producto)
    
    def reponer_desde_deposito(self,producto,cantidad_a_reponer):
        print(f"Stock en gondola: {producto.get_stock_gondola()}")
        if producto.get_stock_gondola()==0 and producto.get_stock_deposito()>=cantidad_a_reponer:
            nuevo_stock_gondola=producto.get_stock_gondola()+cantidad_a_reponer
            nuevo_stock_deposito=producto.get_stock_deposito()-cantidad_a_reponer

            producto.set_stock_gondola(nuevo_stock_gondola)
            producto.set_stock_deposito(nuevo_stock_deposito)
            print("Reposicion hecha")

        else:
            print("No hay suficiente stock en deposito del producto para reponer")  

        print(f"Nuevo stock en gondola: {producto.get_stock_gondola()} ")

    def generar_pedido(self,producto:Producto,proveedor:Proveedor):
        stock_total=producto.stock_total()


        if stock_total==0 or stock_total<producto.get_umbral_minimo():
            cant_a_pedir=producto.get_umbral_minimo()-stock_total  
            if cant_a_pedir<=0:
                cant_a_pedir=producto.get_umbral_minimo()
            
            nuevo_pedido=Pedido(producto,cant_a_pedir)

            print("Se genero un pedido")
            proveedor.recibir_pedido(nuevo_pedido)
        
        else:
            print("Hay suficiente stock, no hace falta generar un pedido. ")

class Producto(ABC):
    # Clase abstracta para todos los productos del supermercado.
    def __init__(self,marca,nombre_producto,stock_gondola, precio, codigo, stock_deposito, umbral_minimo):
        self.__codigo = codigo
        self.__marca = marca
        self.__nombre_producto = nombre_producto
        self.__precio = precio
        self.__stock_gondola = stock_gondola
        self.__stock_deposito = stock_deposito
        self.__umbral_minimo = umbral_minimo

    def get_marca(self):
        return self.__marca
    def get_nombre_producto(self):
        return self.__nombre_producto
    def get_stock_gondola(self):
        return self.__stock_gondola
    def set_stock_gondola(self,nuevo_stock):
        self.__stock_gondola=nuevo_stock
    def get_precio(self):
        return self.__precio
    def get_codigo(self):
        return self.__codigo
    def get_stock_deposito(self):
        return self.__stock_deposito
    def set_stock_deposito(self,nuevo_stock_deposito):
        self.__stock_deposito=nuevo_stock_deposito
    def get_umbral_minimo(self):
        return self.__umbral_minimo
    
    def stock_total(self):
        return self.__stock_gondola+self.__stock_deposito
    
    def stock_en_gondola(self):
        if self.__stock_gondola>0:
            return True
        else:
            return False
        
    def descontar_por_unidad(self):   #REVISAR EL TEMA DE QUE ALGUIEN SE LLEVE 20 PRODUCTOS. ACA ESTAMOS RESTANDO SOLO 1. (PARAMETRO CON CANTIDAD A LLEVAR?)
        if self.stock_en_gondola():
            self.__stock_gondola-=1
            print("Se desconto un producto")
        else:
            print("No hay stock del producto en gondola")

    @abstractmethod #metodo abstracto de todas las clases hijas
    def mostrar_en_tablet(self):
        pass
class Productoliquido(Producto):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo,cantidad_litros):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo)
        self.__cantidad_litros=cantidad_litros

    def get_cantidad_litros(self):
        return self.__cantidad_litros
    
  
class Producto_por_kilo(Producto):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo,peso):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo)
        self.__peso=peso

    def get_peso(self):
        return self.__peso
    
    def calcular_precio(self):
        if self.__peso is None:
            return self.get_precio()
        else:
            return self.get_precio() * self.__peso


    

class Carniceria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso=None,tipo_de_corte=None, venta_por="kilo"): #ponemos =kilo para que por defecto sea por kilo, como caso particular qwue sesa unidad
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso)
        self.__tipo_de_corte=tipo_de_corte
        self.__sector="Carniceria"
        self.__venta_por=venta_por

    def get_tipo_de_corte(self):
        return self.__tipo_de_corte
    
    def mostrar_en_tablet(self):
        if self.__venta_por == "unidad":

            print(
                f"- Sector: {self.__sector}\n- Producto: {self.get_nombre_producto()}\n- Precio por unidad: ${self.get_precio()}")
        else:

            print(
                f"- Sector: {self.__sector}\n - Tipo de corte: {self.__tipo_de_corte}\n- Precio por kg: ${self.get_precio()}\n- Peso real: {self.get_peso()} kg\n- Precio final: ${self.calcular_precio()}")

class Electrodomesticos(Producto):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo)
        self.__sector="Electrodomesticos"
    
    def get_sector(self):
        return self.__sector

    def mostrar_en_tablet(self):

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}")

class Fiambreria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso,tipo_de_fiambre):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso)
        self.__tipo_de_fiambre=tipo_de_fiambre
        self.__sector="Fiambreria"

    def get_tipo_de_fiambre(self):
        return self.__tipo_de_fiambre
    
    def mostrar_en_tablet(self):
        print(f"- Sector: {self.__sector}\n -Nombre:{self.get_nombre_producto()}- Tipo de corte: {self.__tipo_de_fiambre}\n - Precio por kg: ${self.get_precio()}\n - Peso real: {self.get_peso()} kg\n - Precio final: ${self.calcular_precio()}")

class Galletitas(Producto):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo)
        self.__sector="Galletitas" #le asigno el sector automaticamente
    
    def get_sector(self):
        return self.__sector

    def mostrar_en_tablet(self):

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}")

class Gaseosas(Productoliquido):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, cantidad_litros):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, cantidad_litros)
        self.__sector="Gaseosas"
    
    def get_sector(self):
        return self.__sector

    def mostrar_en_tablet(self):

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}\n -Cantidasd de litros: {self.get_cantidad_litros()}")

class Golosinas(Producto):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo)
        self.__sector="Golosinas"
    
    def get_sector(self):
        return self.__sector

    def mostrar_en_tablet(self):

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}")


class Proveedor:
    def __init__(self,nombre_proveedor):
        self.__nombre_provedor=nombre_proveedor

    def get_nombre_proveedor(self):
        return self.__nombre_provedor
    
    def recibir_pedido(self,Pedido:Pedido):
        print(f"El proveedor {self.__nombre_provedor} recibio un pedido de reposicion")

        Pedido.mostrar_pedido()
        return Pedido.get_cantidad()

class Pedido:
    def __init__(self,producto:Producto,cantidad):
        self.__producto=producto
        self.__cantidad=cantidad


    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar_pedido(self):
        print(f"PEDIDO-> \n -Nombre del producto: {self.__producto.get_nombre_producto()} \n -Marca: {self.__producto.get_marca()}\n -Cantidad: {self.__cantidad}")


class Perfumeria(Productoliquido):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, cantidad_litros):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, cantidad_litros)
        self.__sector="Perfumeria"
    
    def get_sector(self):
        return self.__sector

    def mostrar_en_tablet(self):

        print( f"-Góndola: {self.__sector}\n -Producto: {self.get_nombre_producto()}\n -Marca: {self.get_marca()}\n -Cantidad de litros: {self.get_cantidad_litros()}")


class Verduleria(Producto_por_kilo):
    def __init__(self, marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso):
        super().__init__(marca, nombre_producto, stock_gondola, precio, codigo, stock_deposito, umbral_minimo, peso)
        self.__sector="Verduleria"
    
    
    def mostrar_en_tablet(self):
        print(f"- Sector: {self.__sector}\n -Nombre:{self.get_nombre_producto()}-\n - Precio por kg: ${self.get_precio()}\n - Peso real: {self.get_peso()} kg\n - Precio final: ${self.calcular_precio()}")

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

    def registrar_producto(self, tipo, marca, nombre_producto,stock_gondola, precio, codigo,stock_deposito, umbral_minimo,peso=None, tipo_de_corte=None, tipo_de_fiambre=None,cantidad_litros=None):

        tipo = tipo.lower() 
        
        tipo_reconocido = self.reconocer_tipo(nombre_producto)

        if tipo_reconocido is None:
            print("Producto no reconocido por el almacén.")
            return None

        if tipo != tipo_reconocido:
            print(f"ERROR: {nombre_producto} pertenece a {tipo_reconocido}, no a {tipo}.")
            return None

        if tipo == "galletitas": #creo un objeto galletitas

            producto = Galletitas(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo)

        elif tipo == "gaseosas":

            producto = Gaseosas(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,cantidad_litros)

        elif tipo == "golosinas":
            producto = Golosinas(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo)

        elif tipo == "perfumeria":
            producto = Perfumeria(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,cantidad_litros)

        elif tipo == "electrodomesticos":
            producto = Electrodomesticos(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo)

        elif tipo == "carniceria":
            if nombre_producto.lower() in ["chorizo", "morcilla"]:
                producto = Carniceria(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,venta_por="unidad")

            else:
                producto = Carniceria(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,peso,tipo_de_corte,venta_por="kilo")

        elif tipo == "verduleria":
            producto = Verduleria(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,peso)
    
        elif tipo == "fiambreria":
            producto = Fiambreria(marca,nombre_producto,stock_gondola,precio,codigo,stock_deposito,umbral_minimo,peso,tipo_de_fiambre)

        else:
            print("No existe tal producto")
            return None

        self.__productos.append(producto) #guarda el producto registrado en el sector correspondiente

        print("Producto  registrado en gondola .")
        print(type(producto))

        return producto