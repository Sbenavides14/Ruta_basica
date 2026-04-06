\# Inventory Management System

\## Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python, ejecutado en consola. Permite al usuario registrar productos, visualizar el inventario almacenado y calcular estadísticas básicas como el valor total y la cantidad total de productos.

El sistema está diseñado siguiendo principios básicos de programación estructurada, haciendo uso de funciones, validaciones y estructuras de control como ciclos y condicionales.

\## Cómo funciona

1. El programa inicia ejecutando la función principal main(), la cual muestra un menú interactivo en consola.
1. El usuario puede seleccionar una de las siguientes opciones:
- Agregar producto
- Mostrar inventario
- Calcular estadísticas
- Salir del programa

3\. Al seleccionar Agregar producto:

- Se solicita el nombre del producto.
- Se valida que el precio sea un número decimal mayor que 0.
- Se valida que la cantidad sea un número entero mayor que 0.
- El producto se almacena como un diccionario dentro de una lista global llamada inventory.

4\. Al seleccionar Mostrar inventario:

- Se verifica si el inventario está vacío.
- En caso contrario, se recorren los productos y se muestran en formato enumerado.

5\. Al seleccionar Calcular estadísticas:

- Se calcula el valor total del inventario (precio × cantidad).
- Se calcula la cantidad total de productos.
- Se muestran los resultados en consola.

6\. El programa se ejecuta en un ciclo while True, permitiendo múltiples operaciones hasta que el usuario seleccione salir.

7\. Las funciones price\_validation() y quantity\_validation() garantizan que los datos ingresados sean válidos mediante manejo de errores (try-except).

\## Estado

Proyecto funcional y estable. Cumple con las operaciones básicas de un sistema de inventario en consola.
