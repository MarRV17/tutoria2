## 10. Diseñar un programa que permita ingresar 6 números
#  en un arreglo y mediante una función ordenarlos de menor a mayor
#  usando ciclos e instrucciones condicionales.


def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


numeros = []

for i in range(6):
    numeros.append(int(input("Ingrese número: ")))

print("Ordenados:", ordenar(numeros))
