def transformador_seguro(texto, opcion):

    ## Ejercicio 5:
    ## Crear una función que reciba un texto y un número.
    #  Si el número no es 1, 2 o 3, debe mostrar un mensaje de “opción inválida”.

    if opcion == 1:
        resultado = texto.upper()
        print("Acción 1 (Mayúsculas):", resultado)

    elif opcion == 2:
        resultado = texto.lower()
        print("Acción 2 (Minúsculas):", resultado)

    elif opcion == 3:
        resultado = texto.capitalize()  # Primera letra en mayúscula
        print("Acción 3 (Primera letra mayúscula):", resultado)

    else:
        print("OPCIÓN INVÁLIDA")
        print("Por favor, elige un número que esté en el sistema (1, 2 o 3).")


## PRUEBAS DE VALIDACIÓN

serie_ejemplo = "Juegos de tronos"

# Prueba con opción válida
print("Prueba 1")
transformador_seguro(serie_ejemplo, 1)

# Prueba con opción inválida
print("Prueba 2")
transformador_seguro(serie_ejemplo, 5)

# Prueba con otra opción inválida
print("Prueba 3")
transformador_seguro("Casa de dragones", 0)

# Prueba con opción 3
print("Prueba 4")
transformador_seguro("Casa de dragones", 3)
