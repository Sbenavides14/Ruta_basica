lista_estudiantes = []     # Lista vacia, donde seran almacenados los estudiantes registrados

def validacion_id():
    """
    Esta funcio evalua que la dato ingresado por el usuario sea de tipo numerico entero, y que sea mayor a 0. si se cumple la condicion
    lo retorna. sino muestra un mensaje de error, y vuelve a pedir el dato.
    """
    while True:
        try:
            id = int(input("Ingrese la id del estudiante: "))          
            if id <= 0:
                print("La id debe ser un numero entero, positivo.")
            else:
                return id
        except ValueError:
            print("El tipo de dato debe ser numerico.")

def validacion_edad():
    """
    Esta funcion evalua que el dato ingresado por el usuario sea de tipo numerico entero, y que sea mayor a 0. Si se cumple la condicion
    lo retorna. sino muestra un mensaje de error, y vuelve a pedir el dato.
    """
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un numero entero, mayor a 0")
            else:
                return edad
        except ValueError:
            print("el tipo de dato debe ser numerico")
            
def validacion_estado():
    """
    Esta funcion evalua que el el estado ingresado por el usuario sea activo o inactivo. Si se cumple la condicion lo retorna.
    sino muestra un mensaje de error, y vuelve a a pedir el dato
    """
    while True:
        
        estado = str(input("Ingrese el estado del estudiante: ")).strip().lower()
        if estado == "activo":
            return estado
        elif estado == "inactivo":
            return estado
        else:
            print("Estado invalido, debe ser activo o inactivo.")


def registar_estudiantes():
    """
    Esta funcion solicita datos al usuario como (nombre, id, edad, programa, estado) del estudiantes, cada dato a excepcion de programa es validado y guardado
    como un diccionario en una variable llamada estudiantes, que posteriormente es agregado a la lista vacia como un elemento de la misma.
    """
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    id = validacion_id()
    edad = validacion_edad()
    programa = input("Ingrese el programa academico del estudiante: ")
    print("-----------------------------------------------")
    print("Estado:  Activo - Inactivo")
    print("-----------------------------------------------")
    estado = validacion_estado()
    
    estudiante = {
            "nombre": nombre,
            "id":id,
            "edad": edad,
            "programa": programa,
            "estado": estado
    }
    
    lista_estudiantes.append(estudiante)
    print("¡El estudiante a sido agregado satifactoriamente!")


def consultar_estudiantes():
    """"
    Esta funcion permite mostrar en pantalla en forma de lista a todo y cada uno de los estudiantes que se encuentra registrados en la lista
    que mediante un ciclo muestra un estudiante por cada iteracion.
    """
    if len(lista_estudiantes) == 0:
        print("No hay registro de estudiantes.")
    else:
        for indice, dato in enumerate(lista_estudiantes, start=1):
            print(f"{indice}- Nombre: {dato["nombre"]} - Id: {dato["id"]} - Edad: {dato["edad"]} - Programa: {dato["programa"]} - Estado: {dato["estado"]}")


def buscar_estudiantes():
    """
    Esta funcion permite buscar entre todo los estudiantes que hayan en la lista a uno en especifico, con solo solicitar el nombre. 
    Una vez lo encuentra lo muestra en pantalla, sino no lo encuentra muestra un mensaje diciendo que no hay coincidencias.
    """
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    id_estudiante = validacion_id()
    
    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre_estudiante and estudiante["id"] == id_estudiante:
            print(f"Nombre: {estudiante["nombre"]} - Id: {estudiante["id"]} - Edad: {estudiante["edad"]} - Programa: {estudiante["programa"]} - Estado: {estudiante["estado"]}")
            return estudiante
    else:
        print("No hay coincidencias.")

def actualizar_estudiantes():
    """"
    Esta funcion permite actualizar los datos de un estudiante de un estudiante en especifico, son solo ingresar el nombre.
    Busca al estudiantes, solicitas los datos anteriormente mencionados para la actualizacion y los valida. sino se encuntran coincidencias, lo muestra en la pantalla.
    """
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    id_estudiante = validacion_id()
    
    estudiante = None
    
    for alumno in lista_estudiantes:
        if alumno["nombre"] == nombre_estudiante and alumno["id"] == id_estudiante:
            estudiante = alumno
            break
    if estudiante:
        act_nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
        act_id = validacion_id()
        act_edad = validacion_edad()
        act_programa = input("Ingrese el programa academico del estudiante: ")
        print("-----------------------------------------------")
        print("Estado. Activo - Inactivo")
        print("-----------------------------------------------")
        act_estado = validacion_estado()
        
        try:
            if act_nombre:
                estudiante["nombre"] = act_nombre
            if act_id:
                estudiante["id"] = act_id
            if act_edad:
                estudiante["edad"] = act_edad
            if act_programa:
                estudiante["programa"] = act_programa
            if act_estado:
                estudiante["estado"] = act_estado
            print("Estudiante actualizado satifactoriamente.")
        except ValueError:
            print("tipo de dato incorrecto.")
    else:
        print("No hay coincidencias. ")

def eliminar_estudiantes():
    """
    Esta funcion permite al usuario eliminar a un estudiante, previamente registrado  en la lista,
    con solo solicitar el nombre, si lo encuentra muestra un mensaje confirmando la eliminacion del estudiante, sino muestra un mensaje diciendo que no hay coincidencias.
    """
    
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    id_estudiante = validacion_id()
    estudiante = None
    
    for alumno in lista_estudiantes:
        if alumno["nombre"] == nombre_estudiante and alumno["id"] == id_estudiante:
            estudiante = alumno
            break
    if estudiante:
        lista_estudiantes.remove(estudiante)
        print("Estudiante eliminado satifactoriamente: ")
    else:
        print("No hay coincidencias")


def menu():
    """
    Esta es la funcion principal, y desde donde se ejecutan las demas funciones.
    Mediante un menu de opciones, el usuario elije que accion realizar. Si el usuario elije una opcion entre 1 y 5 se ejecuta la funcion especificada.
    Si llega a elegir la opcion 6, el programa rompe el bucle mendiante el break. Pero si la opcion ingresada por el usuario esta por fuera de 1 y 6 o 
    el tipo de dato no es el correcto, pedira la opcion de manera indefinida.
    """
    while True:
        try:
            print("-----------Menu----------")
            print("1. Registrar estudiante.")
            print("2. Consultar estudiantes.")
            print("3. Buscar_estudiantes.")
            print("4. Actualizar estudiantes.")
            print("5. Eliminar estudiantes.")
            print("6. salir.")
            print("-------------------------")
            opcion = int(input("Escoja la accion a realizar: "))
            
            if opcion == 1:
                registar_estudiantes()
            elif opcion == 2:
                consultar_estudiantes()
            elif opcion == 3:
                buscar_estudiantes()
            elif opcion == 4:
                actualizar_estudiantes()
            elif opcion == 5:
                eliminar_estudiantes()
            elif opcion == 6:
                print("¡Hasta pronto!")
                break
            else:
                print("¡Opcion invalidad, intente nuevamente!")
        except ValueError:
            print("¡Opcion invalida, intente nuevamente!")
            
            

menu() #llamada a la funcion principal para que el programa sea ejecutado.