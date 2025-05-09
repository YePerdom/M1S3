# Se establece una lista para ir almacenando los productos que se deseen añadir al inventario.
inventario = [
    {
        'leche':[2500.0,20.0]
    },
    {
        'arroz':[1750.0,17.0]
    },
    {
        'maiz':[700.0,20.0]
    }
]

# # Se define la función "anadir_producto", para añadir articulos. 
def anadir_producto(nombre, precio, cantidad):

    articulo = {
        nombre:[precio,cantidad]
    }

    return inventario.append(articulo)

# Se define la función "buscar_producto_nombre", para buscar productos por su nombre.
def buscar_producto_nombre(nombre):

    for articulo in inventario:
        if nombre in articulo:
            nombre_articulo = nombre
            for precio, cantidad in articulo.values():
                precio = float(precio)
                cantidad = float(cantidad)

            busqueda = f"{nombre_articulo}      {precio}     {cantidad}\n"
            break
        else:
            busqueda = f"\nEl articulo no se encuentra registrado.\n"

    return busqueda

# Se define la función "actualizar_precio", para buscar modificar el precio del articulo.
def actualizar_precio(nombre,nuevo_precio):

    for articulo in inventario:
        if nombre in articulo:
            nombre_articulo = nombre
            for precio, cantidad in articulo.values():
                precio = float(nuevo_precio)
                cantidad = float(cantidad)

            actualizacion = f"{nombre_articulo}:     {precio}     {cantidad}"
            break
        else:
            actualizacion = f"El articulo no se encuentra registrado."

    return actualizacion

# Se define la función "actualizar_cantidad", para modificar la cantidad de un articulo.
def actualizar_cantidad(nombre,nueva_cantidad):

    for articulo in inventario:
        if nombre in articulo:
            nombre_articulo = nombre
            for precio, cantidad in articulo.values():
                precio = float(precio)
                cantidad = float(nueva_cantidad)

            actualizacion = f"{nombre_articulo}:     {precio}     {cantidad}"
            break
        else:
            actualizacion = f"El articulo no se encuentra registrado."
            
    return actualizacion

# Se define la función "eliminar_producto", para eliminar un articulo.
def eliminar_producto(nombre):

    for articulo in inventario:
        if nombre in articulo:
            index = inventario.index(articulo)
            inventario.pop(index)
            resultado = f"El articulo '{nombre}' ha sido eliminado."
            break
        else:
            resultado = f"El articulo no se encuentra registrado."
    
    return resultado

# Se define la función "lista_articulos", para mostrar la lista de  articulos.
def lista_articulos():

    lista_de_articulos = ""
    for articulo in inventario:
        for clave, valor in articulo.items():
            nombre_articulo = clave
            precio = valor[0]
            cantidad = valor[1]
    
        lista_de_articulos += f"{nombre_articulo}:     {precio}     {cantidad}.\n"

    return lista_de_articulos

# Se define lambda para la suma total del inventario.
total = lambda inventario: sum(precio * cantidad for articulo in inventario for precio, cantidad in articulo.values())

# Se muestra bienvenida en consola.
print(f"\nBienvenid@ al sistema de inventario\n{'='* 50}\n")

control = True
while control:
    
    print("¿Qué desea realizar?\n")
    try:
        # Se establece un menu de opciones validando que el usuario ingrese solo caracteres INT  en un rango de 0 a 7.
        menu = int(input("1) Añadir un articulo.\n2) Buscar un articulo.\n3) Modificar precio de un articulo.\n4) Modificar cantidad de un articulo.\n5) Eliminar articulo.\n6) Lista de Articulos.\n7) Valor total del inventario.\n0) Salir.\n\n"))
        # Se establece un condicional para determirar la intercación, dependiendo de la eleccion del usuario.
        if 0 <= menu <= 7:
            if menu == 0:
                print("Gracias por utilizar nustro sistema")
                control = False
             
            # opcion 1   
            elif menu == 1:
                # Se valida que el articulo a elejir no se encuentre registrado anteriormente. (incompleto retorna ruido si el producto se encuentra)
                nuevo_articulo = input("\nNombre de nuevo articulo: ")
                for articulo in inventario:
                    if nuevo_articulo in articulo:
                        print(f"\nEl articulo {nuevo_articulo} ya se encuentra registrado en el inventario.\n")
                        
                        menu = 8
                        break            
                    
                    # Se valida que solo se puedan ingresar caracteres de tipo FLOAT en las variables.
                    while menu == 1:
                        try:
                            precio = float(input("Precio de nuevo articulo: "))
                            break
                        except:
                                print("\nPor favor, ingrese unicamente números.\n")           
                    while menu == 1:
                        try:
                            cantidad = float(input("Cantidad de nuevo articulo: "))
                            break
                        except:
                            print("\nPor favor, ingrese unicamente números.\n")
                        # Se añade el producto
                        anadir_producto(nuevo_articulo,precio,cantidad)
                        print("\nProducto añadido al inventario.\n")
                        continue
                continue
            
            # Opcion 2.
            elif menu == 2:
                # Se valida que el articulo se encuentre en la lista de inventario.
                producto = input("\nIndique el nombre del articulo que desea ver: ")
                buscado = buscar_producto_nombre(producto)
                if producto in buscado:
                    print("Articulo      Precio      Cantidad  ")
                    print(buscado)
                else:
                    print(buscado)
            
            # Opcion 3.
            elif menu == 3:
                # Se valida que el articulo se encuentre en la lista de inventario.
                producto = input("\nNombre de articulo: ")
                buscado = buscar_producto_nombre(producto)
                if producto in buscado:
                    print("\nArticulo      Precio      Cantidad  ")
                    print(buscado)
                else:
                    print(buscado)
                    continue
                      
                # Se valida que solo se puedan ingresar caracteres de tipo FLOAT en las variables.
                while menu == 3:
                        try:
                            precio = float(input("Nuevo precio de articulo: "))
                            break
                        except:
                                print("\nPor favor, ingrese unicamente números.\n")
                
                # Se actualiza el precio del producto.
                actualizacion = actualizar_precio(producto,precio)
                if producto in actualizacion:
                    print("\nActualizado")
                    print("Articulo      Precio      Cantidad  ")
                    print(actualizacion)
                else:
                    print(actualizacion)
            
            #Opcion 4.
            elif menu == 4:
                # Se valida que el articulo se encuentre en la lista de inventario.
                producto = input("\nNombre de articulo: ")
                buscado = buscar_producto_nombre(producto)
                if producto in buscado:
                    print("\nArticulo      Precio      Cantidad  ")
                    print(buscado)
                else:
                    print(buscado)
                    continue
                
                # Se valida que solo se puedan ingresar caracteres de tipo FLOAT en las variables.
                while menu == 4:
                        try:
                            cantidad = float(input("Nueva cantidad de articulo: "))
                            break
                        except:
                                print("\nPor favor, ingrese unicamente números.\n")
                
                # Se actualiza la cantidad del producto.
                actualizacion = actualizar_cantidad(producto,cantidad)
                if producto in actualizacion:
                    print("\nActualizado")
                    print("Articulo      Precio      Cantidad  ")
                    print(actualizacion)
                else:
                    print(actualizacion)
               
            #Opcion 5.     
            elif menu == 5:
                # Se valida que el articulo se encuentre en la lista de inventario.
                producto = input("\nNombre de articulo: ")
                buscado = buscar_producto_nombre(producto)
                if producto in buscado:
                    print("\nArticulo      Precio      Cantidad  ")
                    print(buscado)
                else:
                    print(buscado)
                    continue
                
                # Se elimina el atriculo encontrado en el inventario
                resultado = eliminar_producto(producto)
                print(resultado)
            
            # Opcion 6.  
            elif menu == 6:
                # Se muestra la lista de articulos.
                print("\nArticulo      Precio      Cantidad  ")
                print(lista_articulos())

            # Opcion 7.
            elif menu == 7:
                # Se muestra el valor total del inventario
                print(f"\n valor total de inventario : ${total(inventario)}\n")
                
        else:
            # Se imprime un mensaje en dado caso elija un numero menor que 0 o mayor que 7.
            print("\nHa selecionado una opción inexistente.\n")
            continue
    except:
        # Se imprime un mensaje en dado caso inserte un caracter diferente de tipo INT.
        print("\nPor favor, ingrese unicamente números.\n")

#funcionalidades imcompletas, no se almacenan los datos modificados, tales como precio y cantidad