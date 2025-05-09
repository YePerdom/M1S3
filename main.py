# # Se establece una lista para ir almacenando los productos que se deseen añadir al inventario.
# inventario = []

# # Se define la función "anadir_producto", para añadir articulos. 
# def anadir_producto(nombre, precio, cantidad):

#     articulo = {
#         nombre:[precio,cantidad]
#     }

#     return inventario.append(articulo)

# # Se define la función "buscar_producto_nombre", para buscar productos por su nombre.
# def buscar_producto_nombre(nombre):

#     for articulo in inventario:
#         if nombre in articulo:
#             nombre_articulo = nombre
#             for precio, cantidad in articulo.values():
#                 precio = float(precio)
#                 cantidad = float(cantidad)
           
#             busqueda = f"{nombre_articulo}:     {precio}     {cantidad}"
#             break
#         else:
#             busqueda = f"El articulo {nombre_articulo} no se encuentra registrado."

#     return busqueda

# # Se define la función "actualizar_precio", para buscar modificar el precio del articulo.
# def actualizar_precio(nombre,nuevo_precio):

#     for articulo in inventario:
#         if nombre in articulo:
#             nombre_articulo = nombre
#             for precio, cantidad in articulo.values():
#                 precio = float(nuevo_precio)
#                 cantidad = float(cantidad)

#             actualizacion = f"{nombre_articulo}:     {precio}     {cantidad}"
#             break
#         else:
#             actualizacion = f"El articulo {nombre_articulo} no se encuentra registrado."

#     return actualizacion

# # Se define la función "actualizar_cantidad", para modificar la cantidad de un articulo.
# def actualizar_cantidad(nombre,nueva_cantidad):

#     for articulo in inventario:
#         if nombre in articulo:
#             nombre_articulo = nombre
#             for precio, cantidad in articulo.values():
#                 precio = float(precio)
#                 cantidad = float(nueva_cantidad)

#             actualizacion = f"{nombre_articulo}:     {precio}     {cantidad}"
#             break
#         else:
#             actualizacion = f"El articulo {nombre_articulo} no se encuentra registrado."
            
#     return actualizacion

# # Se define la función "eliminar_producto", para eliminar un articulo.
# def eliminar_producto(nombre):

#     for articulo in inventario:
#         if nombre in articulo:
#             index = inventario.index(articulo)
#             inventario.pop(index)
#             resultado = f"El articulo '{nombre}' ha sido eliminado."
#             break
#         else:
#             resultado = f"El articulo {nombre} no se encuentra registrado."
    
#     return resultado

# # Se define la función "eliminar_producto", para eliminar un articulo.
# def lista_articulos():

#     lista_de_articulos = ""
#     for articulo in inventario:
#         for clave, valor in articulo.items():
#             nombre_articulo = clave
#             precio = valor[0]
#             cantidad = valor[1]
    
#         lista_de_articulos += f"{nombre_articulo}:     {precio}     {cantidad}.\n"

#     return lista_de_articulos