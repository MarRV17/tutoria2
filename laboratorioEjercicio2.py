def procesar_palabra(palabra, tipo_cambio):

    ## Ejercicio 2:
    ## Crear una función que reciba una palabra y un número,
    ## y muestre el resultado en pantalla aplicando la transformación correspondiente (1, 2 o 3).

    if tipo_cambio == 1:
        # MAYÚSCULAS
        resultado = palabra.upper()

    elif tipo_cambio == 2:
        # minúsculas
        resultado = palabra.lower()

    elif tipo_cambio == 3:
        # primera letra en mayúscula
        resultado = palabra.capitalize()

    else:
        resultado = "Error: Opción no válida (usa 1, 2 o 3)"

    print("Resultado:", resultado)


# Ejemplo 1: queremos la palabra en mayúsculas
procesar_palabra("INFIEL", 1)

# Ejemplo 2: queremos corregir una frase en mayúsculas a minúsculas
procesar_palabra("ROSAS", 2)

# Ejemplo 3: queremos solo la primera letra en mayúscula
procesar_palabra("CAMINAR", 3)
