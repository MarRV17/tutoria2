## 5. Diseñar una función que reciba un arreglo de números
# y retorne un nuevo arreglo solo con los números positivos
#  usando un bucle y condicionales.


def positivos(lista):
    resultado = []

    for num in lista:
        if num > 0:
            resultado.append(num)

    return resultado


numeros = list(map(int, input("Ingrese números: ").split()))
print("Positivos:", positivos(numeros))

numeros = list(map(int, input("Ingrese números: ").split()))
print("Positivos:", positivos(numeros))

numeros = list(map(int, input("Ingrese números: ").split()))
print("Positivos:", positivos(numeros))

numeros = list(map(int, input("Ingrese números: ").split()))
print("Positivos:", positivos(numeros))
