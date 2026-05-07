## 6. Crear un programa que genere 10 números aleatorios,
# los guarde en un arreglo y
#  mediante una función indique cuántos son mayores a 50.

import random


def contar_mayores_50(lista):
    contador = 0

    for num in lista:
        if num > 50:
            contador += 1

    return contador


numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Números:", numeros)
print("Mayores a 50:", contar_mayores_50(numeros))
