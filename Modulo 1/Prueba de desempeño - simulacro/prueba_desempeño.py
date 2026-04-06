# =============================================================================
# SISTEMA DE GESTIÓN DE CLIENTES
# Permite registrar, mostrar, buscar, actualizar y eliminar clientes
# mediante un menú interactivo en consola.
# =============================================================================

# Lista global que almacena todos los clientes registrados como diccionarios
lista_clientes = []


# -----------------------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# Estas funciones se encargan de asegurar que los datos ingresados por el
# usuario sean del tipo y rango correcto antes de usarlos en el sistema.
# -----------------------------------------------------------------------------

def validacion_cedula():
    """
    Solicita y valida el número de cédula del cliente.
    - Solo acepta números enteros positivos.
    - Repite la solicitud si el valor ingresado es inválido.
    Retorna: (int) La cédula válida ingresada por el usuario.
    """
    while True:  # Bucle infinito hasta obtener un valor válido
        try:
            cedula = int(input("Ingrese numero de cedula del cliente: "))
            if cedula <= 0:
                # Se rechaza si es cero o negativo
                print("Numero de identificacion invalido")
            else:
                return cedula  # Se retorna solo si es un número positivo
        except ValueError:
            # Se activa si el usuario ingresa texto u otro tipo no convertible a entero
            print("Tipo de identificacion invalidad")


def validacon_edad():
    """
    Solicita y valida la edad del cliente.
    - Solo acepta números enteros positivos.
    - Repite la solicitud si el valor ingresado es inválido.
    Retorna: (int) La edad válida ingresada por el usuario.
    """
    while True:
        try:
            edad = int(input("Ingrese la edad del cliente: "))
            if edad <= 0:
                # Se rechaza si la edad es cero o negativa
                print("¡Edad invalidad, intente nuevamente!")
            else:
                return edad  # Se retorna solo si es un número positivo
        except ValueError:
            # Se activa si el usuario ingresa texto u otro tipo no convertible a entero
            print("¡El tipo de dato es invalido, intente nuevamente!")


def validacon_plan():
    """
    Solicita y valida el tipo de plan del cliente.
    - Solo acepta los valores: 'mensual', 'trimestral' o 'anual'.
    - Repite la solicitud si el valor ingresado no coincide con ninguna opción.
    Retorna: (str) El plan válido ingresado por el usuario.
    """
    while True:
        try:
            plan = input("tipo de plan del cliente: ")
            # Se verifica si el plan ingresado es una de las opciones permitidas
            if plan == "mensual":
                return plan
            elif plan == "trimestral":
                return plan
            elif plan == "anual":
                return plan
            else:
                # Si no coincide con ninguna opción válida, se informa al usuario
                print("¡Plan invalido, intente nuevamente!")
        except ValueError:
            # Captura de error en caso de tipo de dato inesperado (poco probable con input())
            print("¡Tipo de dato invalido!")


def validacon_estado():
    """
    Solicita y valida el estado del cliente.
    - Solo acepta los valores: 'activo' o 'inactivo'.
    - Repite la solicitud si el valor ingresado no es válido.
    Retorna: (str) El estado válido ingresado por el usuario.
    """
    while True:
        try:
            estado = input("En que estado se encuentra el cliente: ")
            # Se verifica si el estado ingresado es uno de los permitidos
            if estado == "activo":
                return estado
            elif estado == "inactivo":
                return estado
            else:
                # Si no es ninguno de los dos, se solicita nuevamente
                print("¡Estado invalido, intente nuevamente!")
        except ValueError:
            # Captura de error en caso de tipo de dato inesperado
            print("¡Tipo de dato invalido!")


# -----------------------------------------------------------------------------
# FUNCIONES CRUD (Crear, Leer, Actualizar, Eliminar)
# Operaciones principales del sistema sobre la lista de clientes.
# -----------------------------------------------------------------------------

def registrar_clientes():
    """
    Solicita los datos de un nuevo cliente, los valida y los agrega
    a la lista global 'lista_clientes' como un diccionario.
    Campos registrados: nombre, cédula, edad, plan y estado.
    """
    # Se solicita el nombre y se normaliza (sin espacios extra, en minúsculas)
    nombre = input("ingrese el nombre del cliente: ").strip().lower()

    # Se llaman las funciones de validación para cada campo
    cedula = validacion_cedula()
    edad = validacon_edad()

    # Se muestran las opciones disponibles antes de pedir el plan
    print("------------------------------------")
    print("Planes: Mensual - trimestral - Anual")
    print("------------------------------------")
    plan = validacon_plan()

    # Se muestran las opciones de estado antes de pedirlo
    print("------------------------------------")
    print("Estado: Activo - Inactivo")
    print("------------------------------------")
    estado = validacon_estado()

    # Se crea el diccionario con los datos del cliente
    cliente = {
        "nombre": nombre,
        "cedula": cedula,
        "edad": edad,
        "plan": plan,
        "estado": estado
    }

    # Se agrega el diccionario del cliente a la lista global
    lista_clientes.append(cliente)
    print("cliente agregado satifactoriamente")


def mostrar_clientes():
    """
    Muestra en consola todos los clientes registrados en 'lista_clientes'.
    Si la lista está vacía, informa que no hay clientes registrados.
    Usa enumerate para mostrar un índice numérico junto a cada cliente.
    """
    if len(lista_clientes) == 0:
        # Caso en que no se ha registrado ningún cliente aún
        print("No hay clientes registrados.")
    else:
        # Se recorre la lista mostrando cada cliente con su número de posición
        for indice, datos in enumerate(lista_clientes, start=1):
            print(
                f"{indice}. - Nombre: {datos['nombre']} | "
                f"Cedula: {datos['cedula']} | "
                f"Edad: {datos['edad']} | "
                f"Plan: {datos['plan']} | "
                f"Estado: {datos['estado']}"
            )


def buscar_clientes():
    """
    Busca un cliente en 'lista_clientes' por nombre (búsqueda parcial).
    - La búsqueda no distingue entre mayúsculas y minúsculas.
    - Muestra los datos del cliente si lo encuentra.
    - Informa si no existe ningún cliente con ese nombre.
    Retorna: (dict) El primer cliente encontrado, o None si no hay coincidencia.
    """
    nombre_cliente = input("Ingrese el nombre del cliente: ").strip().lower()

    for client in lista_clientes:
        # Se verifica si el nombre buscado está contenido en el nombre del cliente
        if nombre_cliente in client["nombre"].lower():
            print(
                f"Nombre: {client['nombre']} | "
                f"Cedula: {client['cedula']} | "
                f"Edad: {client['edad']} | "
                f"Plan: {client['plan']} | "
                f"Estado: {client['estado']}"
            )
            return client  # Se retorna el primer cliente que coincida
    else:
        # El bloque else del for se ejecuta si el bucle terminó sin encontrar coincidencia
        print("cliente no encontrado")


def actualizar_clientes():
    """
    Busca un cliente por nombre y permite actualizar todos sus campos:
    cédula, edad, plan y estado.
    - Si el cliente existe, solicita los nuevos valores con validación.
    - Si no existe, informa al usuario.
    Nota: el nombre del cliente no se actualiza en esta función.
    """
    nombre_cliente = input("Ingrese el nombre del cliente: ").strip().lower()
    cliente = None  # Variable que almacenará el cliente encontrado

    # Se busca el cliente en la lista por nombre (búsqueda parcial)
    for c in lista_clientes:
        if nombre_cliente in c["nombre"].lower():
            cliente = c
            break  # Se detiene al encontrar el primer cliente que coincida

    if cliente:
        # Se solicitan y validan los nuevos valores para cada campo
        actualizar_cedula = validacion_cedula()
        actualizar_edad = validacon_edad()

        print("------------------------------------")
        print("Planes: Mensual - trimestral - Anual")
        print("------------------------------------")
        actualizar_plan = validacon_plan()

        print("------------------------------------")
        print("Estado: Activo - Inactivo")
        print("------------------------------------")
        actualizar_estado = validacon_estado()

        try:
            # Se actualizan los campos del diccionario del cliente con los nuevos valores
            if actualizar_cedula:
                cliente["cedula"] = int(actualizar_cedula)
            if actualizar_edad:
                cliente["edad"] = int(actualizar_edad)
            if actualizar_plan:
                cliente["plan"] = actualizar_plan
            if actualizar_estado:
                cliente["estado"] = actualizar_estado
            print("¡Cliente actualizado satifactoriamente!")
        except ValueError:
            # Se captura error si alguna conversión de tipo falla inesperadamente
            print("¡tipo de dato incorrecto, intente nuevamnete!")
    else:
        print("¡Cliente no encontrado!")


def eliminar_clientes():
    """
    Elimina un cliente de 'lista_clientes' buscándolo por nombre.
    - La búsqueda es parcial y no distingue mayúsculas de minúsculas.
    - Si el cliente existe, lo elimina de la lista.
    - Si no existe, informa al usuario.
    """
    nombre_cliente = input("Ingrese el nombre del cliente: ").strip().lower()
    cliente = None  # Variable que almacenará el cliente encontrado

    # Se recorre la lista buscando un cliente cuyo nombre coincida con el ingresado
    for c in lista_clientes:
        if nombre_cliente in c["nombre"].lower():  # Se verifica el nombre ANTES de asignar
            cliente = c
            break  # Se detiene solo si encontró al cliente correcto

    # Si se encontró un cliente con ese nombre, se elimina de la lista
    if cliente:
        lista_clientes.remove(cliente)
        print("¡Cliente eliminado satisfactoriamente!")
    else:
        # Si 'cliente' sigue siendo None, no se encontró ninguna coincidencia
        print("¡Cliente no encontrado!")

def escribir_lista_csv()

    with open("lista_clientes.csv", "w", newline="", encoding="utf-8") as base_datos:
        writer = csv.writer(base_datos, delimiter=",")
        writer.writerows(lista_clientes)


# -----------------------------------------------------------------------------
# MENÚ PRINCIPAL
# Punto de entrada del programa. Muestra las opciones disponibles y
# redirige al usuario a la función correspondiente según su elección.
# -----------------------------------------------------------------------------

def menu():
    """
    Muestra el menú principal del sistema en un bucle continuo.
    - Solicita al usuario que seleccione una opción numérica (1-6).
    - Llama a la función correspondiente según la opción elegida.
    - La opción 6 termina el programa.
    - Maneja errores si el usuario ingresa un valor no numérico.
    """
    while True:  # El menú se repite hasta que el usuario elija salir (opción 6)
        try:
            print("----------------------")
            print("------ MENU ------")
            print("1. Registrar cliente")
            print("2. Mostrar cliente.")
            print("3. Buscar cliente.")
            print("4. Actualizar cliente.")
            print("5. Eliminar clientes.")
            print("6. salir.")
            print("----------------------")

            opcion = int(input("Ingrese la accion que desea realizar: "))
            print("----------------------")

            # Se ejecuta la función correspondiente a la opción elegida
            if opcion == 1:
                registrar_clientes()
            elif opcion == 2:
                mostrar_clientes()
            elif opcion == 3:
                buscar_clientes()
            elif opcion == 4:
                actualizar_clientes()
            elif opcion == 5:
                eliminar_clientes()
            elif opcion == 6:
                print("¡Hasta pronto!")
                break  # Se sale del bucle y termina el programa
            else:
                # Opción fuera del rango válido (no entre 1 y 6)
                print("¡Opcion invalidad, intente nuevamente!")
        except ValueError:
            # Se activa si el usuario ingresa texto en lugar de un número
            print("¡Opcion invalidad, intente nuevamente!")


# Punto de entrada: se llama al menú para iniciar el programa
menu()
