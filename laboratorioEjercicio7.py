def transformador_en_cadena(texto_base, lista_opciones):

    ##Ejercicio 7:
    ## Crear una función que reciba un texto y una lista de números (entre 1 y 3).
    #  La función debe aplicar cada transformación en orden y devolver el resultado final.

    resultado_actual = texto_base
    print(f"Texto inicial en memoria: '{resultado_actual}'")

    # Recorremos la lista de números
    for opcion in lista_opciones:

        if opcion == 1:
            resultado_actual = resultado_actual.upper()
            print(f"-> Aplicando Mayúsculas: {resultado_actual}")

        elif opcion == 2:
            resultado_actual = resultado_actual.lower()
            print(f"-> Aplicando Minúsculas: {resultado_actual}")

        elif opcion == 3:
            resultado_actual = (
                resultado_actual.capitalize()
            )  # Primera letra en mayúscula
            print(f"-> Aplicando Primera letra mayúscula: {resultado_actual}")

        else:
            print(f"-> Opción {opcion} no reconocida. Saltando...")

    # Retorna el estado final después de todas las modificaciones
    return resultado_actual


## PRUEBAS DE EJECUCIÓN

mi_serie = "Juegos de tronos"
secuencia_de_cambios = [1, 2, 3]  # Mayúsculas → Minúsculas → Primera letra

print("-- INICIANDO CADENA DE TRANSFORMACIÓN --")
resultado_final = transformador_en_cadena(mi_serie, secuencia_de_cambios)

print("- RESULTADO FINAL -")
print(f"Variable final: {resultado_final}")
