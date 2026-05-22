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


def crear_unidades(clase_producto, cantidad, *args, **kwargs):
    lista = []

    for i in range(cantidad):
        producto = clase_producto(*args, **kwargs)
        lista.append(producto)

    return lista


def cargar_inventario(inventario, productos_referencia):
    for producto in productos_referencia:
        inventario.agregar_producto_a_inventario(producto)


def mostrar_menu_gondolas():
    print("\n========== GÓNDOLAS DISPONIBLES ==========")
    print("1. Galletitas")
    print("2. Gaseosas")
    print("3. Perfumería")
    print("4. Golosinas")
    print("5. Electrodomésticos")
    print("6. Carnicería")
    print("7. Verdulería")
    print("8. Fiambrería")
    print("0. Volver")


def mostrar_menu_principal():
    print("\n========== SUPERMARKET IOT ==========")
    print("1. Ver productos de una góndola")
    print("2. Agregar productos al carrito")
    print("3. Ver carrito")
    print("4. Ver total a pagar")
    print("5. Probar reposición desde depósito")
    print("6. Probar pedido a proveedor")
    print("0. Salir")


def obtener_gondola_por_opcion(opcion, gondolas):
    if opcion == "1":
        return gondolas["galletitas"]
    elif opcion == "2":
        return gondolas["gaseosas"]
    elif opcion == "3":
        return gondolas["perfumeria"]
    elif opcion == "4":
        return gondolas["golosinas"]
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


def ver_productos_de_gondola(gondolas):
    mostrar_menu_gondolas()

    opcion = input("Seleccione una góndola: ")

    if opcion == "0":
        return

    gondola = obtener_gondola_por_opcion(opcion, gondolas)

    if gondola is None:
        print("Opción inválida.")
    else:
        gondola.mostrar_productos()


def agregar_producto_al_carrito(carrito, inventario, gondolas, almacen, deposito, proveedor):
    mostrar_menu_gondolas()

    opcion = input("Seleccione la góndola desde donde quiere comprar: ")

    if opcion == "0":
        return

    gondola = obtener_gondola_por_opcion(opcion, gondolas)

    if gondola is None:
        print("Opción inválida.")
        return

    print("\nProductos disponibles en esta góndola:")
    gondola.mostrar_productos()

    codigo = input("\nIngrese el código del producto que quiere llevar: ")

    producto = inventario.buscar_prod_por_cod(codigo)

    if producto is None:
        print("No existe un producto registrado con ese código.")
        return

    print("\nProducto encontrado:")
    print(f"Nombre: {producto.get_nombre_producto()}")
    print(f"Marca: {producto.get_marca()}")
    print(f"Precio: ${producto.get_precio()}")

    try:
        cantidad = int(input("Ingrese la cantidad que quiere llevar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    productos_retirados = gondola.descontar_producto(codigo, cantidad)

    if len(productos_retirados) == 0:
        print("No se agregó nada al carrito.")
        return

    for producto_retirado in productos_retirados:
        carrito.productos_en_carrito.append(producto_retirado)

    print(f"\nSe agregaron {len(productos_retirados)} productos al carrito.")

    total_actual = almacen.precio_final_con_promos(carrito, inventario, gondola )

    print(f"Pantalla OLED del carrito - Total actual con promociones: ${total_actual}")

    stock_actual_gondola = gondola.mostrar_stock_por_codigo(codigo)

    print(f"Stock actual en góndola para el código {codigo}: {stock_actual_gondola}")

    if stock_actual_gondola == 0:
        print("\nLa góndola quedó sin stock. Se intenta reponer desde depósito.")

        inventario.reponer_desde_deposito(
            deposito,
            gondola,
            producto.get_umbral_minimo(),
            codigo
        )

    inventario.generar_pedido(
        producto,
        proveedor,
        gondola,
        deposito
    )


def ver_carrito(carrito):
    print("\n========== CARRITO ==========")

    if len(carrito.productos_en_carrito) == 0:
        print("El carrito está vacío.")
        return

    contador = 1

    for producto in carrito.productos_en_carrito:
        print(
            f"{contador}. Código: {producto.get_codigo()} | "
            f"Producto: {producto.get_nombre_producto()} | "
            f"Marca: {producto.get_marca()} | "
            f"Precio: ${producto.get_precio()}"
        )

        contador += 1


def ver_total(carrito, almacen, inventario, gondola):
    print("\n========== TOTAL A PAGAR ==========")

    if len(carrito.productos_en_carrito) == 0:
        print("El carrito está vacío.")
        return

    total_sin_promos = almacen.precio_final_pre_promos(carrito, inventario, gondola)
    total_con_promos = almacen.precio_final_con_promos(carrito, inventario, gondola)

    print(f"Total sin promociones: ${total_sin_promos}")
    print(f"Total con promociones: ${total_con_promos}")


def probar_reposicion(gondolas, deposito, inventario):
    print("\n========== PRUEBA DE REPOSICIÓN ==========")
    print("Se probará con Manaos Naranja, código 006.")

    gondola_gaseosas = gondolas["gaseosas"]

    stock_actual = gondola_gaseosas.mostrar_stock_por_codigo("006")

    print(f"Stock inicial de Manaos en góndola: {stock_actual}")
    print(f"Stock inicial de Manaos en depósito: {deposito.contar_deposito('006')}")

    if stock_actual > 0:
        gondola_gaseosas.descontar_producto("006", stock_actual)

    print(f"Stock luego de vaciar góndola: {gondola_gaseosas.mostrar_stock_por_codigo('006')}")

    inventario.reponer_desde_deposito(
        deposito,
        gondola_gaseosas,
        3,
        "006"
    )

    print(f"Stock final de Manaos en góndola: {gondola_gaseosas.mostrar_stock_por_codigo('006')}")
    print(f"Stock final de Manaos en depósito: {deposito.contar_deposito('006')}")


def probar_pedido_proveedor(gondolas, deposito, inventario, proveedor):
    print("\n========== PRUEBA DE PEDIDO A PROVEEDOR ==========")
    print("Se probará con Manaos Naranja, código 006.")

    producto = inventario.buscar_prod_por_cod("006")

    if producto is None:
        print("No se encontró el producto.")
        return

    inventario.generar_pedido(
        producto,
        proveedor,
        gondolas["gaseosas"],
        deposito
    )


def main():

    almacen = Almacen()
    inventario = Inventario()
    proveedor = Proveedor("Proveedor Central")
    carrito = Carrito()

    # ======================================================
    # CREACIÓN DE GÓNDOLAS
    # ======================================================

    gondola_galletitas = Gondola(
        "Galletitas",
        crear_unidades(Galletitas, 130, "ParNor", "pitusas", 330, "001", 20)
        + crear_unidades(Galletitas, 100, "Bagley", "sonrisas", 400, "002", 20)
        + crear_unidades(Galletitas, 20, "Bagley", "porteñitas", 1200, "003", 10)
    )

    gondola_gaseosas = Gondola(
        "Gaseosas",
        crear_unidades(Gaseosas, 10, "Coca Cola", "coca cola", 3000, "004", 5, 1.25)
        + crear_unidades(Gaseosas, 500, "Coca Cola", "sprite", 3000, "005", 20, 1.25)
        + crear_unidades(Gaseosas, 3, "Manaos", "manaos naranja", 1000, "006", 5, 1.25)
    )

    gondola_perfumeria = Gondola(
        "Perfumeria",
        crear_unidades(Perfumeria, 900, "Ayudin", "lavandina", 900, "007", 50, 1.5)
        + crear_unidades(Perfumeria, 50, "Zorro", "jabon en polvo", 900, "008", 10, 0.4)
        + crear_unidades(Perfumeria, 30, "Nivea", "jabon tocador", 200, "009", 10, 0.125)
    )

    gondola_golosinas = Gondola(
        "Golosinas",
        crear_unidades(Golosinas, 10000, "Arcor", "caramelos fizz", 200, "010", 100)
        + crear_unidades(Golosinas, 10000, "Arcor", "caramelos masticables frutales", 100, "011", 100)
        + crear_unidades(Golosinas, 10000, "Arcor", "caramelos de miel", 75, "012", 100)
    )

    gondola_electrodomesticos = Gondola(
        "Electrodomesticos",
        crear_unidades(Electrodomesticos, 10, "Electrolux", "freidora de aire", 100000, "020", 2)
        + crear_unidades(Electrodomesticos, 25, "Bluesky", "pava electrica", 45000, "021", 3)
        + crear_unidades(Electrodomesticos, 15, "Mandine", "cafetera", 50000, "022", 3)
    )

    gondola_carniceria = Gondola(
        "Carniceria",
        crear_unidades(Carniceria, 5, "Swift", "asado", 12000, "030", 3, 2.5, "asado", "kilo")
        + crear_unidades(Carniceria, 5, "Swift", "vacio", 11000, "031", 3, 2, "vacio", "kilo")
        + crear_unidades(Carniceria, 20, "Paladini", "chorizo", 800, "032", 5, venta_por="unidad")
    )

    gondola_verduleria = Gondola(
        "Verduleria",
        crear_unidades(Verduleria, 40, "Central", "papa", 900, "040", 5, 2)
        + crear_unidades(Verduleria, 25, "Central", "tomate", 1200, "041", 5, 1.5)
        + crear_unidades(Verduleria, 30, "Central", "manzana", 1500, "042", 5, 1)
    )

    gondola_fiambreria = Gondola(
        "Fiambreria",
        crear_unidades(Fiambreria, 10, "Paladini", "jamon", 6000, "050", 4, 0.5, "jamon cocido")
        + crear_unidades(Fiambreria, 10, "La Paulina", "queso", 7000, "051", 4, 0.4, "queso cremoso")
        + crear_unidades(Fiambreria, 10, "Tandil", "salame", 9000, "052", 4, 0.3, "salame")
    )

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

    # ======================================================
    # CREACIÓN DE DEPÓSITO
    # ======================================================

    deposito = Deposito(
        crear_unidades(Galletitas, 20, "ParNor", "pitusas", 330, "001", 20)
        + crear_unidades(Gaseosas, 10, "Manaos", "manaos naranja", 1000, "006", 5, 1.25)
        + crear_unidades(Golosinas, 50, "Arcor", "caramelos fizz", 200, "010", 100)
        + crear_unidades(Electrodomesticos, 5, "Mandine", "cafetera", 50000, "022", 3)
    )

    # ======================================================
    # CARGA DE INVENTARIO
    # ======================================================

    productos_referencia = [
        Galletitas("ParNor", "pitusas", 330, "001", 20),
        Galletitas("Bagley", "sonrisas", 400, "002", 20),
        Galletitas("Bagley", "porteñitas", 1200, "003", 10),
        Gaseosas("Coca Cola", "coca cola", 3000, "004", 5, 1.25),
        Gaseosas("Coca Cola", "sprite", 3000, "005", 20, 1.25),
        Gaseosas("Manaos", "manaos naranja", 1000, "006", 5, 1.25),
        Perfumeria("Ayudin", "lavandina", 900, "007", 50, 1.5),
        Perfumeria("Zorro", "jabon en polvo", 900, "008", 10, 0.4),
        Perfumeria("Nivea", "jabon tocador", 200, "009", 10, 0.125),
        Golosinas("Arcor", "caramelos fizz", 200, "010", 100),
        Golosinas("Arcor", "caramelos masticables frutales", 100, "011", 100),
        Golosinas("Arcor", "caramelos de miel", 75, "012", 100),
        Electrodomesticos("Electrolux", "freidora de aire", 100000, "020", 2),
        Electrodomesticos("Bluesky", "pava electrica", 45000, "021", 3),
        Electrodomesticos("Mandine", "cafetera", 50000, "022", 3),
        Carniceria("Swift", "asado", 12000, "030", 3, 2.5, "asado", "kilo"),
        Carniceria("Swift", "vacio", 11000, "031", 3, 2, "vacio", "kilo"),
        Carniceria("Paladini", "chorizo", 800, "032", 5, venta_por="unidad"),
        Verduleria("Central", "papa", 900, "040", 5, 2),
        Verduleria("Central", "tomate", 1200, "041", 5, 1.5),
        Verduleria("Central", "manzana", 1500, "042", 5, 1),
        Fiambreria("Paladini", "jamon", 6000, "050", 4, 0.5, "jamon cocido"),
        Fiambreria("La Paulina", "queso", 7000, "051", 4, 0.4, "queso cremoso"),
        Fiambreria("Tandil", "salame", 9000, "052", 4, 0.3, "salame")
    ]

    cargar_inventario(inventario, productos_referencia)

    print("\nSistema SuperMarket IoT iniciado correctamente.")

    # ======================================================
    # MENÚ PRINCIPAL
    # ======================================================

    seguir = True

    while seguir:
        mostrar_menu_principal()

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ver_productos_de_gondola(gondolas)

        elif opcion == "2":
            agregar_producto_al_carrito(
                carrito,
                inventario,
                gondolas,
                almacen,
                deposito,
                proveedor
            )

        elif opcion == "3":
            ver_carrito(carrito)

        elif opcion == "4":
            ver_total(carrito, almacen, inventario, gondola_galletitas)

        elif opcion == "5":
            probar_reposicion(gondolas, deposito, inventario)

        elif opcion == "6":
            probar_pedido_proveedor(gondolas, deposito, inventario, proveedor)

        elif opcion == "0":
            print("\nSaliendo del sistema.")
            seguir = False

        else:
            print("Opción inválida.")


main()