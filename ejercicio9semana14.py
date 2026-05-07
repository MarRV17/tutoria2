## 9. Elaborar una función que reciba un arreglo de números
#  y devuelva la suma total, pero solo sumando los números pares.


def suma_pares(lista):
    suma = 0

    for num in lista:
        if num % 2 == 0:
            suma += num

    return suma


numeros = list(map(int, input("Ingrese números: ").split()))
print("Suma de pares:", suma_pares(numeros))
