from Almacen import *
from Gondola import *
from Deposito import *
from Inventario import *
from Proveedor import *


def main():

    almacen = Almacen()
    inventario = Inventario()
    proveedor = Proveedor("Proveedor Central")

    print("\n========== REGISTRO DE PRODUCTOS ==========")

    pitusas1 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)
    pitusas2 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)
    pitusas3 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)

    coca1 = almacen.registrar_producto("gaseosas", "Coca Cola", "coca cola", 2500, "GAS001", 5, cantidad_litros=1.5)
    coca2 = almacen.registrar_producto("gaseosas", "Coca Cola", "coca cola", 2500, "GAS001", 5, cantidad_litros=1.5)

    caramelo1 = almacen.registrar_producto("golosinas", "Fizz", "caramelos fizz", 300, "GOL001", 5)
    lavandina1 = almacen.registrar_producto("perfumeria", "Ayudin", "lavandina", 900, "PER001", 5, cantidad_litros=1.5)
    cafetera1 = almacen.registrar_producto("electrodomesticos", "Philips", "cafetera", 50000, "ELE001", 2)

    asado1 = almacen.registrar_producto("carniceria", "Swift", "asado", 12000, "CAR001", 3, peso=2.5, tipo_de_corte="Asado")
    chorizo1 = almacen.registrar_producto("carniceria", "Paladini", "chorizo", 800, "CAR002", 5)

    papa1 = almacen.registrar_producto("verduleria", "Central", "papa", 900, "VER001", 5, peso=2.0)
    jamon1 = almacen.registrar_producto("fiambreria", "Paladini", "jamon", 6000, "FIA001", 4, peso=0.5, tipo_de_fiambre="Jamón cocido")

    print("\n========== CREAR GÓNDOLAS ==========")

    gondola_galletitas = Gondola("Galletitas", [pitusas1, pitusas2, pitusas3])
    gondola_gaseosas = Gondola("Gaseosas", [coca1, coca2])
    gondola_golosinas = Gondola("Golosinas", [caramelo1])
    gondola_perfumeria = Gondola("Perfumeria", [lavandina1])
    gondola_electro = Gondola("Electrodomesticos", [cafetera1])
    gondola_carniceria = Gondola("Carniceria", [asado1, chorizo1])
    gondola_verduleria = Gondola("Verduleria", [papa1])
    gondola_fiambreria = Gondola("Fiambreria", [jamon1])

    print("\n========== MOSTRAR PRODUCTOS DE GÓNDOLA ==========")
    gondola_galletitas.mostrar_productos()
    gondola_carniceria.mostrar_productos()

    print("\n========== MOSTRAR EN TABLET ==========")
    pitusas1.mostrar_en_tablet()
    coca1.mostrar_en_tablet()
    lavandina1.mostrar_en_tablet()
    asado1.mostrar_en_tablet()
    chorizo1.mostrar_en_tablet()
    papa1.mostrar_en_tablet()
    jamon1.mostrar_en_tablet()

    print("\n========== CONTAR STOCK EN GÓNDOLA ==========")
    print("Pitusas en góndola:", gondola_galletitas.mostrar_stock_por_codigo("GAL001"))
    print("Coca en góndola:", gondola_gaseosas.mostrar_stock_por_codigo("GAS001"))

    print("\n========== DESCONTAR PRODUCTOS DE GÓNDOLA ==========")
    comprados = gondola_galletitas.descontar_producto("GAL001", 2)

    print("Productos retirados:")
    for producto in comprados:
        print(producto.get_nombre_producto())

    print("Pitusas restantes en góndola:", gondola_galletitas.mostrar_stock_por_codigo("GAL001"))

    print("\n========== CREAR DEPÓSITO ==========")

    pitusas_dep1 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)
    pitusas_dep2 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)
    pitusas_dep3 = almacen.registrar_producto("galletitas", "Pitusas", "pitusas", 1500, "GAL001", 5)

    coca_dep1 = almacen.registrar_producto("gaseosas", "Coca Cola", "coca cola", 2500, "GAS001", 5, cantidad_litros=1.5)

    deposito = Deposito([pitusas_dep1, pitusas_dep2, pitusas_dep3, coca_dep1])

    print("Pitusas en depósito:", deposito.contar_deposito("GAL001"))
    print("Coca en depósito:", deposito.contar_deposito("GAS001"))

    print("\n========== REPONER DESDE DEPÓSITO ==========")

    # Primero vacío lo que quedó de Pitusas en góndola
    gondola_galletitas.descontar_producto("GAL001", 1)

    print("Pitusas en góndola antes de reponer:", gondola_galletitas.mostrar_stock_por_codigo("GAL001"))

    inventario.reponer_desde_deposito(
        deposito,
        gondola_galletitas,
        2,
        "GAL001"
    )

    print("Pitusas en góndola después de reponer:", gondola_galletitas.mostrar_stock_por_codigo("GAL001"))
    print("Pitusas en depósito después de reponer:", deposito.contar_deposito("GAL001"))

    print("\n========== GENERAR PEDIDO ==========")

    inventario.generar_pedido(
        pitusas1,
        proveedor,
        gondola_galletitas,
        deposito
    )

    print("\n========== PROBAR ERROR DE CLASIFICACIÓN ==========")

    producto_error = almacen.registrar_producto(
        "carniceria",
        "Pitusas",
        "pitusas",
        1500,
        "GAL999",
        5
    )

    print("Resultado del producto mal cargado:", producto_error)

    print("\n========== FIN DEL MAIN ==========")


main()