def transformar_lista_palabras(lista_de_datos, opcion):

    ## Ejercicio 4:
    ## Crear una función que reciba una lista de palabras y un número.
    ## La función debe transformar cada palabra de la lista según la opción seleccionada (1, 2 o 3).

    lista_transformada = []

    for palabra in lista_de_datos:

        if opcion == 1:
            resultado = palabra.upper()

        elif opcion == 2:
            resultado = palabra.lower()

        elif opcion == 3:
            resultado = palabra.capitalize()  # Primera letra en mayúscula

        else:
            resultado = "Opción Inválida"

        lista_transformada.append(resultado)

    return lista_transformada


## DATOS DE PRUEBA

mis_series = [
    "juegos de tronos",
    "casa de papel",
    "tumba de luciernagas",
    "casa de dragones",
]

print("LISTA ORIGINAL")
print(mis_series)

# Opción 3: primera letra en mayúscula
resultado_final = transformar_lista_palabras(mis_series, 3)
print("Lista Transformada (Primera letra mayúscula)")
print(resultado_final)

# Opción 1: todas las palabras en MAYÚSCULAS
resultado_mayus = transformar_lista_palabras(mis_series, 1)
print("LISTA TRANSFORMADA (Mayúsculas)")
print(resultado_mayus)
