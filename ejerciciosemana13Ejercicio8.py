## 8. Patrón de asteriscos
## •	Pide un número.
## •	Usa for para imprimir un triángulo de asteriscos.
## •	Usa if para que solo imprima filas impares.
## •	Repite con while hasta que el usuario ingrese 0.

while True:
    n = int(input("Ingrese un número (0 para salir): "))

    if n == 0:
        break

    for i in range(1, n + 1):
        if i % 2 != 0:
            print("*" * i)
