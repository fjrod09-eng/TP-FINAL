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


def crear_varias_unidades(clase, cantidad, *args, **kwargs):
    lista = []

    for i in range(cantidad):
        producto = clase(*args, **kwargs)
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


def crear_sistema():

    print("========== INICIO DEL SISTEMA ==========")

    almacen = Almacen()
    inventario = Inventario()
    proveedor = Proveedor("Proveedor Central")
    carrito = Carrito()

    print("\n========== CREANDO PRODUCTOS ==========")

    # -----------------------------
    # GÓNDOLA 1: GALLETITAS
    # -----------------------------
    pitusas_gondola = crear_varias_unidades(Galletitas, 4, "ParNor", "pitusas", 330, "001", 5)
    sonrisas_gondola = crear_varias_unidades(Galletitas, 3, "Bagley", "sonrisas", 400, "002", 5)
    portenitas_gondola = crear_varias_unidades(Galletitas, 2, "Bagley", "porteñitas", 1200, "003", 5)

    pitusas_deposito = crear_varias_unidades(Galletitas, 6, "ParNor", "pitusas", 330, "001", 5)
    sonrisas_deposito = crear_varias_unidades(Galletitas, 6, "Bagley", "sonrisas", 400, "002", 5)
    portenitas_deposito = crear_varias_unidades(Galletitas, 6, "Bagley", "porteñitas", 1200, "003", 5)

    # -----------------------------
    # GÓNDOLA 2: GASEOSAS
    # -----------------------------
    coca_gondola = crear_varias_unidades(Gaseosas, 3, "Coca Cola", "coca cola", 3000, "004", 5, 2.25)
    sprite_gondola = crear_varias_unidades(Gaseosas, 3, "Sprite", "sprite", 3000, "005", 5, 2.25)
    manaos_gondola = crear_varias_unidades(Gaseosas, 2, "Manaos", "manaos naranja", 1000, "006", 5, 2.25)

    coca_deposito = crear_varias_unidades(Gaseosas, 8, "Coca Cola", "coca cola", 3000, "004", 5, 2.25)
    sprite_deposito = crear_varias_unidades(Gaseosas, 8, "Sprite", "sprite", 3000, "005", 5, 2.25)
    manaos_deposito = crear_varias_unidades(Gaseosas, 8, "Manaos", "manaos naranja", 1000, "006", 5, 2.25)

    # -----------------------------
    # GÓNDOLA 3: PERFUMERÍA
    # -----------------------------
    lavandina_gondola = crear_varias_unidades(Perfumeria, 3, "Ayudin", "lavandina", 900, "007", 5, 1.5)
    zorro_gondola = crear_varias_unidades(Perfumeria, 3, "Zorro", "jabon en polvo", 900, "008", 5, 0.4)
    jabon_gondola = crear_varias_unidades(Perfumeria, 3, "Nivea", "jabon tocador", 200, "009", 5, 0.125)

    lavandina_deposito = crear_varias_unidades(Perfumeria, 8, "Ayudin", "lavandina", 900, "007", 5, 1.5)
    zorro_deposito = crear_varias_unidades(Perfumeria, 8, "Zorro", "jabon en polvo", 900, "008", 5, 0.4)
    jabon_deposito = crear_varias_unidades(Perfumeria, 8, "Nivea", "jabon tocador", 200, "009", 5, 0.125)

    # -----------------------------
    # GÓNDOLA 4: GOLOSINAS
    # -----------------------------
    fizz_gondola = crear_varias_unidades(Golosinas, 5, "Arcor", "caramelos fizz", 200, "010", 5)
    masticables_gondola = crear_varias_unidades(Golosinas, 5, "Arcor", "caramelos masticables frutales", 100, "011", 5)
    miel_gondola = crear_varias_unidades(Golosinas, 5, "Arcor", "caramelos de miel", 75, "012", 5)

    fizz_deposito = crear_varias_unidades(Golosinas, 10, "Arcor", "caramelos fizz", 200, "010", 5)
    masticables_deposito = crear_varias_unidades(Golosinas, 10, "Arcor", "caramelos masticables frutales", 100, "011", 5)
    miel_deposito = crear_varias_unidades(Golosinas, 10, "Arcor", "caramelos de miel", 75, "012", 5)

    # -----------------------------
    # GÓNDOLA 5: ELECTRODOMÉSTICOS
    # -----------------------------
    freidora_gondola = crear_varias_unidades(Electrodomesticos, 2, "Electrolux", "freidora de aire", 100000, "013", 2)
    pava_gondola = crear_varias_unidades(Electrodomesticos, 2, "Bluesky", "pava electrica", 45000, "014", 2)
    cafetera_gondola = crear_varias_unidades(Electrodomesticos, 2, "Mandine", "cafetera", 50000, "015", 2)

    freidora_deposito = crear_varias_unidades(Electrodomesticos, 5, "Electrolux", "freidora de aire", 100000, "013", 2)
    pava_deposito = crear_varias_unidades(Electrodomesticos, 5, "Bluesky", "pava electrica", 45000, "014", 2)
    cafetera_deposito = crear_varias_unidades(Electrodomesticos, 5, "Mandine", "cafetera", 50000, "015", 2)

    # -----------------------------
    # GÓNDOLA 6: CARNICERÍA
    # -----------------------------
    asado_gondola = crear_varias_unidades(Carniceria, 2, "La Anónima", "asado", 9000, "016", 2, 1.5, "asado", "kilo")
    vacio_gondola = crear_varias_unidades(Carniceria, 2, "La Anónima", "vacio", 11000, "017", 2, 1.2, "vacio", "kilo")
    chorizo_gondola = crear_varias_unidades(Carniceria, 3, "Paladini", "chorizo", 1200, "018", 2, None, None, "unidad")
    morcilla_gondola = crear_varias_unidades(Carniceria, 3, "Paladini", "morcilla", 1000, "019", 2, None, None, "unidad")

    asado_deposito = crear_varias_unidades(Carniceria, 4, "La Anónima", "asado", 9000, "016", 2, 1.5, "asado", "kilo")
    vacio_deposito = crear_varias_unidades(Carniceria, 4, "La Anónima", "vacio", 11000, "017", 2, 1.2, "vacio", "kilo")
    chorizo_deposito = crear_varias_unidades(Carniceria, 5, "Paladini", "chorizo", 1200, "018", 2, None, None, "unidad")
    morcilla_deposito = crear_varias_unidades(Carniceria, 5, "Paladini", "morcilla", 1000, "019", 2, None, None, "unidad")

    # -----------------------------
    # GÓNDOLA 7: VERDULERÍA
    # -----------------------------
    papa_gondola = crear_varias_unidades(Verduleria, 3, "Sin marca", "papa", 1200, "020", 3, 1)
    tomate_gondola = crear_varias_unidades(Verduleria, 3, "Sin marca", "tomate", 1800, "021", 3, 1)
    manzana_gondola = crear_varias_unidades(Verduleria, 3, "Sin marca", "manzana", 2500, "022", 3, 1)

    papa_deposito = crear_varias_unidades(Verduleria, 6, "Sin marca", "papa", 1200, "020", 3, 1)
    tomate_deposito = crear_varias_unidades(Verduleria, 6, "Sin marca", "tomate", 1800, "021", 3, 1)
    manzana_deposito = crear_varias_unidades(Verduleria, 6, "Sin marca", "manzana", 2500, "022", 3, 1)

    # -----------------------------
    # GÓNDOLA 8: FIAMBRERÍA
    # -----------------------------
    jamon_gondola = crear_varias_unidades(Fiambreria, 2, "Paladini", "jamon", 8500, "023", 2, 0.3, "jamon")
    queso_gondola = crear_varias_unidades(Fiambreria, 2, "La Paulina", "queso", 7800, "024", 2, 0.4, "queso")
    salame_gondola = crear_varias_unidades(Fiambreria, 2, "Tandil", "salame", 12000, "025", 2, 0.25, "salame")

    jamon_deposito = crear_varias_unidades(Fiambreria, 5, "Paladini", "jamon", 8500, "023", 2, 0.3, "jamon")
    queso_deposito = crear_varias_unidades(Fiambreria, 5, "La Paulina", "queso", 7800, "024", 2, 0.4, "queso")
    salame_deposito = crear_varias_unidades(Fiambreria, 5, "Tandil", "salame", 12000, "025", 2, 0.25, "salame")

    # -----------------------------
    # CREAR GÓNDOLAS
    # -----------------------------
    gondola_galletitas = Gondola("Galletitas", pitusas_gondola + sonrisas_gondola + portenitas_gondola)
    gondola_gaseosas = Gondola("Gaseosas", coca_gondola + sprite_gondola + manaos_gondola)
    gondola_perfumeria = Gondola("Perfumeria", lavandina_gondola + zorro_gondola + jabon_gondola)
    gondola_golosinas = Gondola("Golosinas", fizz_gondola + masticables_gondola + miel_gondola)
    gondola_electrodomesticos = Gondola("Electrodomesticos", freidora_gondola + pava_gondola + cafetera_gondola)
    gondola_carniceria = Gondola("Carniceria", asado_gondola + vacio_gondola + chorizo_gondola + morcilla_gondola)
    gondola_verduleria = Gondola("Verduleria", papa_gondola + tomate_gondola + manzana_gondola)
    gondola_fiambreria = Gondola("Fiambreria", jamon_gondola + queso_gondola + salame_gondola)

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
        pitusas_deposito + sonrisas_deposito + portenitas_deposito +
        coca_deposito + sprite_deposito + manaos_deposito +
        lavandina_deposito + zorro_deposito + jabon_deposito +
        fizz_deposito + masticables_deposito + miel_deposito +
        freidora_deposito + pava_deposito + cafetera_deposito +
        asado_deposito + vacio_deposito + chorizo_deposito + morcilla_deposito +
        papa_deposito + tomate_deposito + manzana_deposito +
        jamon_deposito + queso_deposito + salame_deposito
    )

    deposito = Deposito(productos_deposito)

    # -----------------------------
    # CARGAR INVENTARIO
    # -----------------------------
    todos_los_productos_gondola = (
        pitusas_gondola + sonrisas_gondola + portenitas_gondola +
        coca_gondola + sprite_gondola + manaos_gondola +
        lavandina_gondola + zorro_gondola + jabon_gondola +
        fizz_gondola + masticables_gondola + miel_gondola +
        freidora_gondola + pava_gondola + cafetera_gondola +
        asado_gondola + vacio_gondola + chorizo_gondola + morcilla_gondola +
        papa_gondola + tomate_gondola + manzana_gondola +
        jamon_gondola + queso_gondola + salame_gondola
    )

    cargar_inventario(inventario, todos_los_productos_gondola)

    print("\nSistema cargado correctamente.")

    # -----------------------------
    # PRUEBA AUTOMÁTICA DE TABLET
    # -----------------------------
    print("\n========== PRUEBA DE MOSTRAR EN TABLET ==========")
    pitusas_gondola[0].mostrar_en_tablet()
    coca_gondola[0].mostrar_en_tablet()
    lavandina_gondola[0].mostrar_en_tablet()
    asado_gondola[0].mostrar_en_tablet()
    chorizo_gondola[0].mostrar_en_tablet()
    papa_gondola[0].mostrar_en_tablet()
    jamon_gondola[0].mostrar_en_tablet()

    # -----------------------------
    # MENÚ DE COMPRA
    # -----------------------------
    seguir = True
    return gondolas, carrito, inventario, proveedor, deposito, almacen
    # while seguir:
    #     mostrar_menu()
    #     opcion = input("Ingrese una opción: ").strip()

    #     if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    #         gondola_elegida = elegir_gondola(opcion, gondolas)

    #         print("\n========== PRODUCTOS DISPONIBLES ==========")
    #         gondola_elegida.mostrar_productos()

    #         print("\n========== ESCANEAR PRODUCTO ==========")
    #         productos_vendidos = carrito.escanear_codigo(inventario, gondola_elegida)

    #         if len(productos_vendidos) > 0:
    #             producto_vendido = productos_vendidos[0]

    #             print("\n========== CONTROL AUTOMÁTICO DE STOCK ==========")
    #             inventario.controlar_stock_despues_de_venta(
    #                 producto_vendido,
    #                 proveedor,
    #                 gondola_elegida,
    #                 deposito
    #             )

    #     elif opcion == "9":
    #         carrito.mostrar_carrito()

    #     elif opcion == "10":
    #         print("\n========== FINALIZAR COMPRA ==========")

    #         carrito.mostrar_carrito()

    #         total_sin_promos = almacen.precio_final_pre_promos(carrito.productos_en_carrito)
    #         total_con_promos = almacen.precio_final_con_promos(carrito.productos_en_carrito)

    #         print(f"\nTotal sin promociones: ${total_sin_promos}")
    #         print(f"Total con promociones: ${total_con_promos}")
    #         print("Gracias por comprar en el supermercado.")

    #         seguir = False

    #     elif opcion == "0":
    #         print("Saliste del sistema sin finalizar la compra.")
    #         seguir = False

    #     else:
    #         print("Opción inválida. Intente nuevamente.")


# if __name__ == "__main__":
#     main()