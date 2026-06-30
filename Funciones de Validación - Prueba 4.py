# FUNCIONES DE VALIDACIÓN

def es_titulo_valido(nombre_libro):
    return nombre_libro.strip() != ""

def es_cantidad_valida(texto_cantidad):
    try:
        cantidad = int(texto_cantidad.strip())
    except ValueError:
        return False
    return cantidad >= 0

def es_plazo_valido(texto_dias):
    try:
        dias = int(texto_dias.strip())
    except ValueError:
        return False
    return dias > 0

# ----------------------------------------------------------------------
# FUNCIONES DEL MENÚ

def imprimir_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def obtener_opcion():
    while True:
        opcion_ingresada = input("Seleccione una opción (1-6): ").strip()
        try:
            opcion_num = int(opcion_ingresada)
        except ValueError:
            print("Opción inválida. Debe ingresar un número entre 1 y 6.")
            continue

        if 1 <= opcion_num <= 6:
            return opcion_num
        print("Opción inválida. Debe ingresar un número entre 1 y 6.")

# ----------------------------------------------------------------------
# OPCIÓN 1 - AGREGAR UN LIBRO

def registrar_libro(lista_libros):
    nombre = input("Ingrese el título del libro: ").strip()
    if not es_titulo_valido(nombre):
        print("Error: el título no puede estar vacío.")
        return

    texto_stock = input("Ingrese la cantidad de copias: ").strip()
    if not es_cantidad_valida(texto_stock):
        print("Error: cantidad inválida.")
        return

    texto_plazo = input("Ingrese el período de préstamo (días): ").strip()
    if not es_plazo_valido(texto_plazo):
        print("Error: plazo inválido.")
        return

    nuevo_libro = {
        "nombre": nombre,
        "stock": int(texto_stock),
        "dias": int(texto_plazo),
        "estado": False
    }

    lista_libros.append(nuevo_libro)
    print(f"Libro '{nombre}' agregado correctamente.")

# ----------------------------------------------------------------------
# OPCIÓN 2 - BUSCAR UN LIBRO

def localizar_libro(lista_libros, nombre):
    for indice in range(len(lista_libros)):
        if lista_libros[indice]["nombre"] == nombre:
            return indice
    return -1

def menu_buscar(lista_libros):
    nombre = input("Ingrese el título del libro a buscar: ")
    indice = localizar_libro(lista_libros, nombre)

    if indice != -1:
        libro = lista_libros[indice]
        print(f"\nLibro encontrado en la posición {indice}:")
        print(f"Título: {libro['nombre']}")
        print(f"Copias: {libro['stock']}")
        print(f"Préstamo: {libro['dias']}")
        print(f"Disponible: {libro['estado']}")
    else:
        print(f"El libro '{nombre}' no existe.")

# ----------------------------------------------------------------------
# OPCIÓN 3 - ELIMINAR UN LIBRO

def borrar_libro(lista_libros):
    nombre = input("Ingrese el título del libro a eliminar: ")
    indice = localizar_libro(lista_libros, nombre)

    if indice != -1:
        lista_libros.pop(indice)
        print(f"Libro '{nombre}' eliminado correctamente.")
    else:
        print(f"El libro '{nombre}' no existe.")

# ----------------------------------------------------------------------
# OPCIÓN 4 - ACTUALIZAR LA DISPONIBILIDAD

def actualizar_estado(lista_libros):
    for item in lista_libros:
        if item["stock"] >= 1:
            item["estado"] = True
        else:
            item["estado"] = False

# ----------------------------------------------------------------------
# OPCIÓN 5 - MOSTRAR LIBROS

def listar_libros(lista_libros):
    actualizar_estado(lista_libros)

    print("\n=== LISTA DE LIBROS ===")
    if not lista_libros:
        print("No hay libros registrados.")
        return

    for item in lista_libros:
        situacion = "DISPONIBLE" if item["estado"] else "SIN COPIAS"
        print(f"Título: {item['nombre']}")
        print(f"Copias: {item['stock']}")
        print(f"Préstamo: {item['dias']}")
        print(f"Estado: {situacion}")
        print("*" * 45)

# ----------------------------------------------------------------------
# PROGRAMA PRINCIPAL

inventario = []  # Lista principal de libros

while True:
    imprimir_menu()
    opcion = obtener_opcion()

    if opcion == 1:
        registrar_libro(inventario)
    elif opcion == 2:
        menu_buscar(inventario)
    elif opcion == 3:
        borrar_libro(inventario)
    elif opcion == 4:
        actualizar_estado(inventario)
        print("Disponibilidad actualizada.")
    elif opcion == 5:
        listar_libros(inventario)
    elif opcion == 6:
        print("Gracias por usar el sistema.")
        break