# Calculadora de Costos de Inventario

## Descripción
La Calculadora de Costos de Inventario es una aplicación desarrollada en Python que permite al usuario ingresar el nombre de un producto, su precio y la cantidad disponible.  

El sistema valida que los datos ingresados sean correctos (valores numéricos y positivos) y, posteriormente, calcula el costo total del inventario.  

Este proyecto está orientado a reforzar conceptos fundamentales de programación como:
- Entrada de datos por consola  
- Validación de información  
- Manejo de excepciones (`try/except`)  
- Uso de funciones y recursividad  

## Cómo funciona

1. El sistema solicita al usuario el nombre del producto.  
2. Se invoca una función para solicitar el precio del producto.  
3. El programa valida que el precio sea un número mayor que cero.  
4. En caso de error (valor no numérico o negativo), se muestra un mensaje y se solicita nuevamente el dato.  
5. Se invoca una función para solicitar la cantidad del producto.  
6. El sistema valida que la cantidad sea un número entero mayor que cero.  
7. Si el valor ingresado es inválido, se repite el proceso hasta obtener un dato correcto.  
8. Se calcula el costo total mediante la multiplicación del precio por la cantidad.  
9. Finalmente, se muestran en pantalla los datos del producto junto con el costo total calculado.  


## Estado: Proyecto funcional y completo. Implementa validación de datos y manejo de errores correctamente.