## 1. Crear una función que reciba una lista de números
#  y retorne la cantidad de números pares e impares
# utilizando un bucle y estructuras condicionales.


def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


numeros = list(map(int, input("Ingrese números: ").split()))
pares, impares = contar_pares_impares(numeros)

numeros = list(map(int, input("Ingrese números: ").split()))
pares, impares = contar_pares_impares(numeros)

print("Pares:", pares)
print("Impares:", impares)
