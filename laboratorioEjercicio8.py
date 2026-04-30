# Definimos la función de transformación
def aplicar_transformacion(texto_entrada, opcion_entrada):

    ## Ejercicio 8:
    ## Crear un programa con menú que permita al usuario ingresar un texto y elegir una opción (1, 2 o 3).
    #  El programa debe usar una función para aplicar la transformación seleccionada.

    if opcion_entrada == 1:
        return texto_entrada.upper()
    elif opcion_entrada == 2:
        return texto_entrada.lower()
    elif opcion_entrada == 3:
        return texto_entrada.capitalize()  # Primera letra en mayúscula
    else:
        return "ERROR: Opción no válida."


# PROGRAMA PRINCIPAL (Menú)
print("## BIENVENIDO INFIELES ##")
print("-- Basado en Programación Lineal --")

# Solicitud del texto
texto_usuario = input("Ingresa el texto a procesar: (juegos de tronos")

# Menú de opciones
print("\n¿Qué quieres hacer con tu texto?")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en mayúscula")
print("4. Salir del programa")

seleccion = input("Elige una opción (1-4): ")

# Validación y ejecución
if seleccion.isdigit():
    opcion_num = int(seleccion)

    if opcion_num == 4:
        print("Saliendo del sistema... ¡Adiós infieles!")
    elif opcion_num in [1, 2, 3]:
        resultado_final = aplicar_transformacion(texto_usuario, opcion_num)
        print("\nRESULTADO EN MEMORIA:")
        print(resultado_final)
    else:
        print("Esa opción no está en el índice del menú.")
else:
    print("Error: Debes ingresar un número válido (1-4).")
