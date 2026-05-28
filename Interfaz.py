# import tkinter as tk

# from Main import crear_sistema

# # =========================================
# # CREAR SISTEMA
# # =========================================

# gondolas, carrito, inventario, proveedor, deposito, almacen = crear_sistema()

# # =========================================
# # FUNCIONES
# # =========================================

# def mostrar_gondola(nombre_gondola):

#     gondola = gondolas[nombre_gondola]

#     texto = f"GÓNDOLA: {gondola.get_sector()}\n\n"

#     productos_unicos = []

#     for producto in gondola._Gondola__productos:

#         ya_existe = False

#         for p in productos_unicos:
#             if p.get_codigo() == producto.get_codigo():
#                 ya_existe = True

#         if not ya_existe:
#             productos_unicos.append(producto)

#     for producto in productos_unicos:

#         stock = gondola.contar_producto(producto.get_codigo())

#         texto += (
#             f"Código: {producto.get_codigo()}\n"
#             f"Producto: {producto.get_nombre_producto()}\n"
#             f"Marca: {producto.get_marca()}\n"
#             f"Precio: ${producto.get_precio()}\n"
#             f"Stock: {stock}\n"
#             f"\n"
#         )
    

#     texto_productos.config(text=texto)
# def buscar_prod():
#     codigo = entrada_codigo.get()
#     producto = inventario.buscar_prod_por_cod(codigo)

#     if producto is None:

#         texto_productos.config(
#             text="Producto no encontrado"
#         )

#     else:

#         texto = (
#             f"Producto: {producto.get_nombre_producto()}\n"
#             f"Marca: {producto.get_marca()}\n"
#             f"Precio: ${producto.get_precio()}"
#         )
        

#         texto_productos.config(text=texto)    

# # =========================================
# # VENTANA
# # =========================================

# ventana = tk.Tk()

# ventana.title("Supermercado")

# ventana.geometry("700x700")
# frame_izquierdo = tk.Frame(ventana)

# frame_izquierdo.pack(
#     side="left",
#     padx=20,
#     pady=20
# )

# frame_derecho = tk.Frame(ventana)

# frame_derecho.pack(
#     side="right",
#     padx=20,
#     pady=20
# )

# # =========================================
# # TITULO
# # =========================================

# titulo = tk.Label(
#     frame_izquierdo,
#     text="=== SUPERMERCADO ===",
#     font=("Arial", 22)
# )

# titulo.pack(pady=20)

# # =========================================
# # BOTONES
# # =========================================

# boton_galletitas = tk.Button(
#     frame_izquierdo,
#     text="Galletitas",
#     width=30,
#     command=lambda: mostrar_gondola("galletitas")
# )

# boton_galletitas.pack(pady=5)

# boton_gaseosas = tk.Button(
#     frame_izquierdo,
#     text="Gaseosas",
#     width=30,
#     command=lambda: mostrar_gondola("gaseosas")
# )

# boton_gaseosas.pack(pady=5)

# boton_golosinas = tk.Button(
#     frame_izquierdo,
#     text="Golosinas",
#     width=30,
#     command=lambda: mostrar_gondola("golosinas")
# )

# boton_golosinas.pack(pady=5)

# boton_perfumeria = tk.Button(
#     frame_izquierdo,
#     text="Perfumería",
#     width=30,
#     command=lambda: mostrar_gondola("perfumeria")
# )

# boton_perfumeria.pack(pady=5)

# boton_electro = tk.Button(
#     frame_izquierdo,
#     text="Electrodomésticos",
#     width=30,
#     command=lambda: mostrar_gondola("electrodomesticos")
# )

# boton_electro.pack(pady=5)

# boton_carniceria = tk.Button(
#     frame_izquierdo,
#     text="Carnicería",
#     width=30,
#     command=lambda: mostrar_gondola("carniceria")
# )

# boton_carniceria.pack(pady=5)

# boton_verduleria = tk.Button(
#     frame_izquierdo,
#     text="Verdulería",
#     width=30,
#     command=lambda: mostrar_gondola("verduleria")
# )

# boton_verduleria.pack(pady=5)

# boton_fiambreria = tk.Button(
#     frame_izquierdo,
#     text="Fiambrería",
#     width=30,
#     command=lambda: mostrar_gondola("fiambreria")
# )

# boton_fiambreria.pack(pady=5)

# label_codigo = tk.Label(
#     frame_izquierdo,
#     text="Ingrese código:"
# )
# "-------------------------------------------------------------------"
# label_codigo.pack(pady=5)


# entrada_codigo = tk.Entry(
#     frame_izquierdo
# )

# entrada_codigo.pack(pady=5)
# "                                                                          Funciones para que ande el apartado de escribir"                                                               
# boton_buscar = tk.Button(
#     frame_izquierdo,
#     text="Elegir producto",
#     command=buscar_prod
# )

# boton_buscar.pack(pady=10)
# "-------------------------------------------------------------"
# # =========================================
# # TEXTO PRODUCTOS
# # =========================================

# texto_productos = tk.Label(
#     frame_derecho,
#     text="Seleccione una góndola",
#     justify="left",
#     font=("Arial", 11)
# )

# texto_productos.pack(pady=20)


# boton_gaseosas = tk.Button(





# )

# # =========================================

# ventana.mainloop()