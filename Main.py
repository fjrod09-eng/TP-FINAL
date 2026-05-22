from Galletitas import *
from Gaseosas import *
from Golosinas import *
from Perfumeria import *
from Electrodomesticos import *
from Carniceria import *
from Verduleria import *
from Fiambreria import *
from Gondola import *
from Deposito import *
from Inventario import *
from Proveedor import *
from Carrito import *
from Almacen import *


def mostrar_lista_productos(lista):
    for producto in lista:
        print(
            f"- Código: {producto.get_codigo()} | "
            f"Producto: {producto.get_nombre_producto()} | "
            f"Marca: {producto.get_marca()} | "
            f"Precio: ${producto.get_precio()}"
        )


def main():

    print("\n======================================")
    print("CREACIÓN DE PRODUCTOS")
    print("======================================")

    # Galletitas
    pitusas1 = Galletitas("Pitusas", "pitusas", 330, "001", 5)
    pitusas2 = Galletitas("Pitusas", "pitusas", 330, "001", 5)
    pitusas3 = Galletitas("Pitusas", "pitusas", 330, "001", 5)

    sonrisas1 = Galletitas("Bagley", "sonrisas", 400, "002", 5)
    sonrisas2 = Galletitas("Bagley", "sonrisas", 400, "002", 5)

    porte1 = Galletitas("Porteñitas", "porteñitas", 1200, "003", 5)
    porte2 = Galletitas("Porteñitas", "porteñitas", 1200, "003", 5)

    # Gaseosas
    coca1 = Gaseosas("Coca Cola", "coca cola", 3000, "004", 5, 1.5)
    coca2 = Gaseosas("Coca Cola", "coca cola", 3000, "004", 5, 1.5)

    sprite1 = Gaseosas("Sprite", "sprite", 3000, "005", 5, 1.5)
    sprite2 = Gaseosas("Sprite", "sprite", 3000, "005", 5, 1.5)

    manaos1 = Gaseosas("Manaos", "manaos naranja", 1000, "006", 5, 2.25)
    manaos2 = Gaseosas("Manaos", "manaos naranja", 1000, "006", 5, 2.25)

    # Perfumería
    lavandina1 = Perfumeria("Ayudin", "lavandina", 900, "007", 5, 1.5)
    lavandina2 = Perfumeria("Ayudin", "lavandina", 900, "007", 5, 1.5)

    zorro1 = Perfumeria("Zorro", "jabon en polvo", 900, "008", 5, 0.4)
    zorro2 = Perfumeria("Zorro", "jabon en polvo", 900, "008", 5, 0.4)

    jabon1 = Perfumeria("Nivea", "jabon tocador", 200, "009", 5, 0.125)
    jabon2 = Perfumeria("Nivea", "jabon tocador", 200, "009", 5, 0.125)

    # Otros productos
    caramelo1 = Golosinas("Fizz", "caramelos fizz", 100, "010", 5)
    cafetera1 = Electrodomesticos("Philips", "cafetera", 50000, "020", 2)
    asado1 = Carniceria("Swift", "asado", 12000, "030", 3, 2.5, "asado", "kilo")
    chorizo1 = Carniceria("Paladini", "chorizo", 800, "031", 5, venta_por="unidad")
    papa1 = Verduleria("Central", "papa", 900, "040", 5, 2)
    jamon1 = Fiambreria("Paladini", "jamon", 6000, "050", 4, 0.5, "jamon cocido")

    print("Productos creados correctamente.")

    print("\n======================================")
    print("MOSTRAR PRODUCTOS EN TABLET")
    print("======================================")

    pitusas1.mostrar_en_tablet()
    print()
    coca1.mostrar_en_tablet()
    print()
    lavandina1.mostrar_en_tablet()
    print()
    asado1.mostrar_en_tablet()
    print()
    chorizo1.mostrar_en_tablet()
    print()
    papa1.mostrar_en_tablet()
    print()
    jamon1.mostrar_en_tablet()

    print("\n======================================")
    print("CREACIÓN DE GÓNDOLAS")
    print("======================================")

    gondola_galletitas = Gondola(
        "Galletitas",
        [pitusas1, pitusas2, pitusas3, sonrisas1, sonrisas2, porte1, porte2]
    )

    gondola_gaseosas = Gondola(
        "Gaseosas",
        [coca1, coca2, sprite1, sprite2, manaos1, manaos2]
    )

    gondola_perfumeria = Gondola(
        "Perfumeria",
        [lavandina1, lavandina2, zorro1, zorro2, jabon1, jabon2]
    )

    gondola_golosinas = Gondola("Golosinas", [caramelo1])
    gondola_electro = Gondola("Electrodomesticos", [cafetera1])
    gondola_carniceria = Gondola("Carniceria", [asado1, chorizo1])
    gondola_verduleria = Gondola("Verduleria", [papa1])
    gondola_fiambreria = Gondola("Fiambreria", [jamon1])

    print("Góndolas creadas correctamente.")

    print("\n======================================")
    print("MOSTRAR PRODUCTOS DE GÓNDOLA")
    print("======================================")

    gondola_galletitas.mostrar_productos()
    print()
    gondola_gaseosas.mostrar_productos()
    print()
    gondola_perfumeria.mostrar_productos()

    print("\n======================================")
    print("STOCK EN GÓNDOLA")
    print("======================================")

    print("Pitusas:", gondola_galletitas.mostrar_stock_por_codigo("001"))
    print("Sonrisas:", gondola_galletitas.mostrar_stock_por_codigo("002"))
    print("Porteñitas:", gondola_galletitas.mostrar_stock_por_codigo("003"))
    print("Coca Cola:", gondola_gaseosas.mostrar_stock_por_codigo("004"))
    print("Sprite:", gondola_gaseosas.mostrar_stock_por_codigo("005"))
    print("Manaos:", gondola_gaseosas.mostrar_stock_por_codigo("006"))

    print("\n======================================")
    print("DESCONTAR PRODUCTOS DE GÓNDOLA")
    print("======================================")

    productos_retirados = gondola_galletitas.descontar_producto("001", 2)

    print("Productos retirados:")
    mostrar_lista_productos(productos_retirados)

    print("Pitusas restantes en góndola:", gondola_galletitas.mostrar_stock_por_codigo("001"))

    print("\n======================================")
    print("CREACIÓN DE DEPÓSITO")
    print("======================================")

    pitusas_dep1 = Galletitas("Pitusas", "pitusas", 330, "001", 5)
    pitusas_dep2 = Galletitas("Pitusas", "pitusas", 330, "001", 5)
    pitusas_dep3 = Galletitas("Pitusas", "pitusas", 330, "001", 5)

    coca_dep1 = Gaseosas("Coca Cola", "coca cola", 3000, "004", 5, 1.5)
    coca_dep2 = Gaseosas("Coca Cola", "coca cola", 3000, "004", 5, 1.5)

    deposito = Deposito(
        [pitusas_dep1, pitusas_dep2, pitusas_dep3, coca_dep1, coca_dep2]
    )

    print("Pitusas en depósito:", deposito.contar_deposito("001"))
    print("Coca Cola en depósito:", deposito.contar_deposito("004"))

    print("\n======================================")
    print("INVENTARIO")
    print("======================================")

    inventario = Inventario()

    inventario.agregar_producto_a_inventario(pitusas1)
    inventario.agregar_producto_a_inventario(sonrisas1)
    inventario.agregar_producto_a_inventario(porte1)
    inventario.agregar_producto_a_inventario(coca1)
    inventario.agregar_producto_a_inventario(sprite1)
    inventario.agregar_producto_a_inventario(manaos1)
    inventario.agregar_producto_a_inventario(lavandina1)
    inventario.agregar_producto_a_inventario(zorro1)
    inventario.agregar_producto_a_inventario(jabon1)
    inventario.agregar_producto_a_inventario(caramelo1)
    inventario.agregar_producto_a_inventario(cafetera1)
    inventario.agregar_producto_a_inventario(asado1)
    inventario.agregar_producto_a_inventario(chorizo1)
    inventario.agregar_producto_a_inventario(papa1)
    inventario.agregar_producto_a_inventario(jamon1)

    producto_buscado = inventario.buscar_prod_por_cod("004")

    if producto_buscado is not None:
        print("Producto encontrado por código 004:")
        print("Nombre:", producto_buscado.get_nombre_producto())
        print("Marca:", producto_buscado.get_marca())
        print("Precio:", producto_buscado.get_precio())

    print("\n======================================")
    print("STOCK TOTAL ENTRE GÓNDOLA Y DEPÓSITO")
    print("======================================")

    stock_total_pitusas = inventario.stock_total(
        gondola_galletitas,
        deposito,
        "001"
    )

    print("Stock total de Pitusas:", stock_total_pitusas)

    print("\n======================================")
    print("REPONER DESDE DEPÓSITO")
    print("======================================")

    cantidad_actual = gondola_galletitas.mostrar_stock_por_codigo("001")

    if cantidad_actual > 0:
        gondola_galletitas.descontar_producto("001", cantidad_actual)

    print("Pitusas en góndola antes de reponer:", gondola_galletitas.mostrar_stock_por_codigo("001"))
    print("Pitusas en depósito antes de reponer:", deposito.contar_deposito("001"))

    inventario.reponer_desde_deposito(
        deposito,
        gondola_galletitas,
        2,
        "001"
    )

    print("Pitusas en góndola después de reponer:", gondola_galletitas.mostrar_stock_por_codigo("001"))
    print("Pitusas en depósito después de reponer:", deposito.contar_deposito("001"))

    print("\n======================================")
    print("GENERAR PEDIDO")
    print("======================================")

    proveedor = Proveedor("Proveedor Central")

    inventario.generar_pedido(
        pitusas1,
        proveedor,
        gondola_galletitas,
        deposito
    )

    print("\n======================================")
    print("PROMOCIONES")
    print("======================================")

    almacen = Almacen()

    carrito_promos = [
        pitusas1,
        pitusas2,
        pitusas3,
        sonrisas1,
        sonrisas2,
        porte1,
        porte2,
        coca1,
        coca2,
        sprite1,
        sprite2,
        manaos1,
        manaos2,
        lavandina1,
        lavandina2,
        zorro1,
        zorro2,
        jabon1,
        jabon2
    ]

    print("Productos en carrito para probar promociones:")
    mostrar_lista_productos(carrito_promos)

    total_sin_promos = almacen.precio_final_pre_promos(carrito_promos)
    total_con_promos = almacen.precio_final_con_promos(carrito_promos)

    print("\nTotal sin promociones:", total_sin_promos)
    print("Total con promociones:", total_con_promos)

    print("\n======================================")
    print("CARRITO CON ESCANEO")
    print("======================================")

    carrito = Carrito()

    print("Código recomendado para probar: 004")
    print("Ese código corresponde a Coca Cola.")
    print("Cuando pregunte cantidad, podés poner 1 o 2.")

    carrito.escanear_codigo(inventario, gondola_gaseosas)

    print("\nProductos en carrito:")

    mostrar_lista_productos(carrito.productos_en_carrito)

    print("\n======================================")
    print("FIN DEL MAIN")
    print("======================================")


main()