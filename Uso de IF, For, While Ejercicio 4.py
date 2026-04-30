## Ejercicio 4:
## Pide un número y determina si es par o impar.


for i in range(1):
    continuar = "s"

    while continuar == "s":
        numero = int(input("Ingrese un número: "))

        if numero % 2 == 0:
            print("Par")
        else:
            print("Impar")
