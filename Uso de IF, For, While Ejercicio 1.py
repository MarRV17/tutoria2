## Ejercicio 1:
## Pide un número al usuario e indica si es positivo, negativo o cero usando if, elif y else.

for i in range(1):
    continuar = "s"

    while continuar == "s":
        numero = int(input("Ingrese un número: "))

        if numero > 0:
            print("Es positivo")
        elif numero < 0:
            print("Es negativo")
        else:
            print("Es cero")
