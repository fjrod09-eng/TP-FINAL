from generadores import *


def main():
    print("SUPERMERCADO ")

    almacen, inventario, proveedor, carrito, gondolas, deposito = supermercado()

    print("\nProductos cargados.")

    seguir = True

    while seguir:
        mostrar_menu()

        opcion = input("Ingrese una opción: ").strip()

        if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:

            gondola_elegida = elegir_gondola(opcion, gondolas)

            print("\n========== PRODUCTOS DISPONIBLES ==========")
            gondola_elegida.mostrar_productos()

            print("\n========== ESCANEAR PRODUCTO ==========")

            productos_vendidos = carrito.escanear_codigo(
                inventario,
                gondola_elegida
            )

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

            total_sin_promos = almacen.precio_final_pre_promos(
                carrito.productos_en_carrito
            )

            total_con_promos = almacen.precio_final_con_promos(
                carrito.productos_en_carrito
            )

            print(f"\nTotal sin promociones: ${total_sin_promos}")
            print(f"Total con promociones: ${total_con_promos}")
            print("Gracias por comprar en el supermercado.")

            seguir = False

        elif opcion == "0":

            print("Saliste del sistema sin finalizar la compra.")
            seguir = False

        else:

            print("Opción inválida. Intente nuevamente.")


main()