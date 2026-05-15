## 4. Elaborar un programa que llene un arreglo
# con 8 números ingresados por el usuario y,
# mediante una función, determine cuál es el número mayor.


def mayor_numero(lista):
    mayor = lista[0]

    for num in lista:
        if num > mayor:
            mayor = num

    return mayor


numeros = []

for i in range(8):
    numeros.append(int(input("Ingrese número: ")))

print("Mayor:", mayor_numero(numeros))
