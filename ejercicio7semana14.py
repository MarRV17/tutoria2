## 7. Desarrollar una función que reciba un arreglo de edades
#  y determine cuántas personas son mayores de edad utilizando if y un ciclo.


def contar_mayores(edades):
    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador


edades = list(map(int, input("Ingrese edades: ").split()))
print("Mayores de edad:", contar_mayores(edades))
