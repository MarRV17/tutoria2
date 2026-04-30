def transformar_dinamico(texto_usuario, opcion_elegida):

    ## Ejercicio 3:
    ## Solicitar al usuario un texto y un número.
    ## Enviar esos datos a una función que aplique la transformación según la opción elegida.

    if opcion_elegida == 1:
        resultado = texto_usuario.upper()
    elif opcion_elegida == 2:
        resultado = texto_usuario.lower()
    elif opcion_elegida == 3:
        resultado = texto_usuario.capitalize()  # Primera letra en mayúscula
    else:
        resultado = "La opción no existe en el sistema."

    print("PROCESO COMPLETADO")
    print(f"Resultado: {resultado}")


# 2. Solicitud de datos (entrada del usuario)

print("BIENVENIDO AL SISTEMA DE LAS INFIELES")
frase = input("Pon un nombre de una infiel: ")

print("Menu de opciones:")
print("1. Todo a Mayúsculas")
print("2. Todo a Minúsculas")
print("3. Primera letra en Mayúscula")

seleccion = input("Elige el número de tu opción: ")

# 3. Ejecución o validación
if seleccion.isdigit():
    opcion_num = int(seleccion)
    transformar_dinamico(frase, opcion_num)
else:
    print("Error: Debes ingresar un número válido (1, 2 o 3).")
