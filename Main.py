from Almacen import *
from Inventario import *
from Gondola import *
from Deposito import *
from Proveedor import *
from Carrito import *

from Galletitas import *
from Gaseosas import *
from Golosinas import *
from Perfumeria import *
from Electrodomesticos import *
from Carniceria import *
from Verduleria import *
from Fiambreria import *


def crear_galletitas(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo):
    lista = []

    for i in range(cantidad):
        producto = Galletitas(marca, nombre_producto, precio, codigo, umbral_minimo)
        lista.append(producto)

    return lista


def crear_gaseosas(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo, cantidad_litros):
    lista = []

    for i in range(cantidad):
        producto = Gaseosas(marca, nombre_producto, precio, codigo, umbral_minimo, cantidad_litros)
        lista.append(producto)

    return lista


def crear_perfumeria(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo, cantidad_litros):
    lista = []

    for i in range(cantidad):
        producto = Perfumeria(marca, nombre_producto, precio, codigo, umbral_minimo, cantidad_litros)
        lista.append(producto)

    return lista


def crear_golosinas(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo):
    lista = []

    for i in range(cantidad):
        producto = Golosinas(marca, nombre_producto, precio, codigo, umbral_minimo)
        lista.append(producto)

    return lista


def crear_electrodomesticos(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo):
    lista = []

    for i in range(cantidad):
        producto = Electrodomesticos(marca, nombre_producto, precio, codigo, umbral_minimo)
        lista.append(producto)

    return lista


def crear_carniceria(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo, peso, tipo_de_corte, venta_por):
    lista = []

    for i in range(cantidad):
        producto = Carniceria(marca, nombre_producto, precio, codigo, umbral_minimo, peso, tipo_de_corte, venta_por)
        lista.append(producto)

    return lista


def crear_verduleria(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo, peso):
    lista = []

    for i in range(cantidad):
        producto = Verduleria(marca, nombre_producto, precio, codigo, umbral_minimo, peso)
        lista.append(producto)

    return lista


def crear_fiambreria(cantidad, marca, nombre_producto, precio, codigo, umbral_minimo, peso, tipo_de_fiambre):
    lista = []

    for i in range(cantidad):
        producto = Fiambreria(marca, nombre_producto, precio, codigo, umbral_minimo, peso, tipo_de_fiambre)
        lista.append(producto)

    return lista


def cargar_inventario(inventario, lista_productos):
    codigos_cargados = []

    for producto in lista_productos:
        if producto.get_codigo() not in codigos_cargados:
            inventario.agregar_producto_a_inventario(producto)
            codigos_cargados.append(producto.get_codigo())


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Ver góndola de galletitas")
    print("2. Ver góndola de gaseosas")
    print("3. Ver góndola de golosinas")
    print("4. Ver góndola de perfumería")
    print("5. Ver góndola de electrodomésticos")
    print("6. Ver góndola de carnicería")
    print("7. Ver góndola de verdulería")
    print("8. Ver góndola de fiambrería")
    print("9. Ver carrito")
    print("10. Finalizar compra")
    print("0. Salir sin comprar")


def elegir_gondola(opcion, gondolas):
    if opcion == "1":
        return gondolas["galletitas"]
    elif opcion == "2":
        return gondolas["gaseosas"]
    elif opcion == "3":
        return gondolas["golosinas"]
    elif opcion == "4":
        return gondolas["perfumeria"]
    elif opcion == "5":
        return gondolas["electrodomesticos"]
    elif opcion == "6":
        return gondolas["carniceria"]
    elif opcion == "7":
        return gondolas["verduleria"]
    elif opcion == "8":
        return gondolas["fiambreria"]
    else:
        return None


def main():

    print("========== INICIO DEL SISTEMA ==========")

    almacen = Almacen()
    inventario = Inventario()
    proveedor = Proveedor("Proveedor Central")
    carrito = Carrito()

    print("\n========== CREANDO PRODUCTOS ==========")

    # -----------------------------
    # GÓNDOLA 1: GALLETITAS
    # -----------------------------
    pitusas_gondola = crear_galletitas(4, "ParNor", "pitusas", 330, "001", 5)
    sonrisas_gondola = crear_galletitas( 3, "Bagley", "sonrisas", 400, "002", 5)
    portenitas_gondola = crear_galletitas( 2, "Bagley", "porteñitas", 1200, "003", 5)

    pitusas_deposito = crear_galletitas( 6, "ParNor", "pitusas", 330, "001", 5)
    sonrisas_deposito = crear_galletitas( 6, "Bagley", "sonrisas", 400, "002", 5)
    portenitas_deposito =crear_galletitas( 6, "Bagley", "porteñitas", 1200, "003", 5)

    # -----------------------------
    # GÓNDOLA 2: GASEOSAS
    # -----------------------------
    coca_gondola = crear_gaseosas( 3, "Coca Cola", "coca cola", 3000, "004", 5, 2.25)
    sprite_gondola = crear_gaseosas( 3, "Sprite", "sprite", 3000, "005", 5, 2.25)
    manaos_gondola = crear_gaseosas( 2, "Manaos", "manaos naranja", 1000, "006", 5, 2.25)

    coca_deposito = crear_gaseosas( 8, "Coca Cola", "coca cola", 3000, "004", 5, 2.25)
    sprite_deposito = crear_gaseosas( 8, "Sprite", "sprite", 3000, "005", 5, 2.25)
    manaos_deposito = crear_gaseosas( 8, "Manaos", "manaos naranja", 1000, "006", 5, 2.25)

    # -----------------------------
    # GÓNDOLA 3: PERFUMERÍA
    # -----------------------------
    lavandina_gondola = crear_perfumeria( 3, "Ayudin", "lavandina", 900, "007", 5, 1.5)
    zorro_gondola = crear_perfumeria( 3, "Zorro", "jabon en polvo", 900, "008", 5, 0.4)
    jabon_gondola = crear_perfumeria( 3, "Nivea", "jabon tocador", 200, "009", 5, 0.125)

    lavandina_deposito = crear_perfumeria( 8, "Ayudin", "lavandina", 900, "007", 5, 1.5)
    zorro_deposito =crear_perfumeria( 8, "Zorro", "jabon en polvo", 900, "008", 5, 0.4)
    jabon_deposito = crear_perfumeria( 8, "Nivea", "jabon tocador", 200, "009", 5, 0.125)

    # -----------------------------
    # GÓNDOLA 4: GOLOSINAS
    # -----------------------------
    fizz_gondola = crear_golosinas( 5, "Arcor", "caramelos fizz", 200, "010", 5)
    masticables_gondola = crear_golosinas( 5, "Arcor", "caramelos masticables frutales", 100, "011", 5)
    miel_gondola =crear_golosinas(5, "Arcor", "caramelos de miel", 75, "012", 5)

    fizz_deposito = crear_golosinas( 10, "Arcor", "caramelos fizz", 200, "010", 5)
    masticables_deposito = crear_golosinas( 10, "Arcor", "caramelos masticables frutales", 100, "011", 5)
    miel_deposito = crear_golosinas( 10, "Arcor", "caramelos de miel", 75, "012", 5)

    # -----------------------------
    # GÓNDOLA 5: ELECTRODOMÉSTICOS
    # -----------------------------
    freidora_gondola = crear_electrodomesticos( 2, "Electrolux", "freidora de aire", 100000, "013", 2)
    pava_gondola = crear_electrodomesticos(2, "Bluesky", "pava electrica", 45000, "014", 2)
    cafetera_gondola = crear_electrodomesticos( 2, "Mandine", "cafetera", 50000, "015", 2)

    freidora_deposito = crear_electrodomesticos( 5, "Electrolux", "freidora de aire", 100000, "013", 2)
    pava_deposito = crear_electrodomesticos( 5, "Bluesky", "pava electrica", 45000, "014", 2)
    cafetera_deposito = crear_electrodomesticos( 5, "Mandine", "cafetera", 50000, "015", 2)

    # -----------------------------
    # GÓNDOLA 6: CARNICERÍA
    # -----------------------------
    asado= Carniceria( "La Anónima", "asado", 9000, "016", 2, 0, "asado", "kilo")
    vacio= Carniceria(  "La Anónima", "vacio", 11000, "017", 2, 0, "vacio", "kilo")
    chorizo_gondola = crear_carniceria( 3, "Paladini", "chorizo", 1200, "018", 2, None, None, "unidad")
    morcilla_gondola = crear_carniceria( 3, "Paladini", "morcilla", 1000, "019", 2, None, None, "unidad")

    
    chorizo_deposito = crear_carniceria( 5, "Paladini", "chorizo", 1200, "018", 2, None, None, "unidad")
    morcilla_deposito = crear_carniceria( 5, "Paladini", "morcilla", 1000, "019", 2, None, None, "unidad")

    # -----------------------------
    # GÓNDOLA 7: VERDULERÍA
    # -----------------------------
    papa = Verduleria(  "Sin marca", "papa", 1200, "020", 3, 0)
    tomate = Verduleria(  "Sin marca", "tomate", 1800, "021", 3, 0)
    manzana= Verduleria(  "Sin marca", "manzana", 2500, "022", 3, 0)



    # -----------------------------
    # GÓNDOLA 8: FIAMBRERÍA
    # -----------------------------
    jamon = Fiambreria(  "Paladini", "jamon", 8500, "023", 2, 0, "jamon")
    queso= Fiambreria( "La Paulina", "queso", 7800, "024", 2, 0, "queso")
    salame= Fiambreria( "Tandil", "salame", 12000, "025", 2, 0, "salame")


    # -----------------------------
    # CREAR GÓNDOLAS
    # -----------------------------
    gondola_galletitas = Gondola("Galletitas", pitusas_gondola + sonrisas_gondola + portenitas_gondola)
    gondola_gaseosas = Gondola("Gaseosas", coca_gondola + sprite_gondola + manaos_gondola)
    gondola_perfumeria = Gondola("Perfumeria", lavandina_gondola + zorro_gondola + jabon_gondola)
    gondola_golosinas = Gondola("Golosinas", fizz_gondola + masticables_gondola + miel_gondola)
    gondola_electrodomesticos = Gondola("Electrodomesticos", freidora_gondola + pava_gondola + cafetera_gondola)
    gondola_carniceria = Gondola("Carniceria", [asado, vacio] + chorizo_gondola + morcilla_gondola,{"016":20, "017":15}) #20 kg de asado y 15 de vacio       
    gondola_verduleria = Gondola("Verduleria", [papa,tomate,manzana],{"020":10,"021":10,"022":10}) #10 kg de papa tomate y manzana
    gondola_fiambreria = Gondola("Fiambreria", [jamon,queso,salame],{"023":2,"024":2,"025":2}) #2 kg de queso, jamon y salamw

    gondolas = {
        "galletitas": gondola_galletitas,
        "gaseosas": gondola_gaseosas,
        "perfumeria": gondola_perfumeria,
        "golosinas": gondola_golosinas,
        "electrodomesticos": gondola_electrodomesticos,
        "carniceria": gondola_carniceria,
        "verduleria": gondola_verduleria,
        "fiambreria": gondola_fiambreria
    }

    # -----------------------------
    # CREAR DEPÓSITO GENERAL
    # -----------------------------
    productos_deposito = (
        pitusas_deposito + sonrisas_deposito + portenitas_deposito +coca_deposito + sprite_deposito + manaos_deposito +lavandina_deposito + zorro_deposito + jabon_deposito +
        fizz_deposito + masticables_deposito + miel_deposito +freidora_deposito + pava_deposito + cafetera_deposito + chorizo_deposito + morcilla_deposito 
    )

    deposito = Deposito(productos_deposito,{ "016": 10.0, "017": 8,  "020": 5,  "021": 5, "022": 4, "023": 3, "024": 2,  "025": 2 })

    # -----------------------------
    # CARGAR INVENTARIO
    # -----------------------------
    todos_los_productos_gondola = (
        pitusas_gondola + sonrisas_gondola + portenitas_gondola +coca_gondola + sprite_gondola + manaos_gondola +lavandina_gondola + zorro_gondola + jabon_gondola +
        fizz_gondola + masticables_gondola + miel_gondola +freidora_gondola + pava_gondola + cafetera_gondola +[asado ,vacio] + chorizo_gondola + 
        morcilla_gondola +[papa , tomate , manzana] +[jamon , queso, salame]
    )

    cargar_inventario(inventario, todos_los_productos_gondola)

   

    seguir = True
    #return gondolas, carrito, inventario, proveedor, deposito, almacen
    while seguir:
        mostrar_menu()
        opcion = input("Ingrese una opción: ").strip()

        if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            gondola_elegida = elegir_gondola(opcion, gondolas)

            print("\n========== PRODUCTOS DISPONIBLES ==========")
            gondola_elegida.mostrar_productos()

            print("\n========== ESCANEAR PRODUCTO ==========")
            productos_vendidos = carrito.escanear_codigo(inventario, gondola_elegida)

            if len(productos_vendidos) > 0:
                producto_vendido = productos_vendidos[0]

                print("\n========== CONTROL AUTOMÁTICO DE STOCK ==========")
                inventario.controlar_stock_despues_de_venta(
                producto_vendido,
                proveedor,
                gondola_elegida,
                deposito
                )

        elif opcion == "9":
            carrito.mostrar_carrito()

        elif opcion == "10":
            print("\n========== FINALIZAR COMPRA ==========")

            carrito.mostrar_carrito()

            total_sin_promos = almacen.precio_final_pre_promos(carrito.productos_en_carrito)
            total_con_promos = almacen.precio_final_con_promos(carrito.productos_en_carrito)

            print(f"\nTotal sin promociones: ${total_sin_promos}")
            print(f"Total con promociones: ${total_con_promos}")
            print("Gracias por comprar en el supermercado.")

            seguir = False

        elif opcion == "0":
            print("Saliste del sistema sin finalizar la compra.")
            seguir = False

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()