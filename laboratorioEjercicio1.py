def transformador_texto(frase, opcion):

    ## Ejercicio 1:
    ## Crear una función que reciba un texto y un número. Según el número:
    ## 1. Convertir todo el texto a mayúsculas
    ## 2. Convertir todo el texto a minúsculas
    ## 3. Colocar la primera letra en mayúscula

    if opcion == 1:
        resultado = frase.upper()
        print("Transformación a Mayúsculas:")
        return resultado

    elif opcion == 2:
        resultado = frase.lower()
        print("Transformación a Minúsculas:")
        return resultado

    elif opcion == 3:
        resultado = frase.capitalize()
        print("Primera letra en Mayúscula:")
        return resultado

    # Por si mandan un número que no existe
    else:
        return "Opción no válida. Elige 1, 2 o 3."


## Pruebas del ejercicio

frase_prueba = "hola mundo lleno de infieles"

# aquí probamos la opción 1
print(transformador_texto(frase_prueba, 1))

# aquí probamos la opción 2
print(transformador_texto("TENGO MIEDO", 2))

# aquí probamos la opción 3
print(transformador_texto(frase_prueba, 3))
