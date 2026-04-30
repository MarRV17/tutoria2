def transformar_y_contar(texto, opcion):

    ## Ejercicio 6:
    ## Crear una función que reciba un texto y un número,
    # transforme el texto según la opción y luego devuelva la cantidad de caracteres del resultado.

    # 1. Lógica de transformación
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()  # Primera letra en mayúscula
    else:
        # Opción inválida
        print("Opción inválida en el sistema.")
        return 0

    # 2. Mostramos el resultado transformado
    print(f"Texto procesado: {resultado}")

    # 3. Retornamos la cantidad de caracteres
    cantidad = len(resultado)
    return cantidad


## PRUEBAS DE EJECUCIÓN

# Ejemplo con Dragon Ball
serie = "Juegos de tronos"
print("--INICIANDO PROCESO --")
total_caracteres = transformar_y_contar(serie, 1)
print(f"La cantidad de caracteres es: {total_caracteres}")

# Ejemplo con frase con espacios
frase_larga = "  Casa de dragones  "
conteo_Casadedragones = transformar_y_contar(frase_larga, 3)
print(
    f"La frase '{frase_larga.strip()}' tiene {conteo_Casadedragones} caracteres (incluyendo espacios)."
)
