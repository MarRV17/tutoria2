## 3. Crear una función que reciba un arreglo de notas
#  y devuelva el promedio. Además, usando if,
#  indicar si el grupo aprueba o reprueba.


def promedio(notas):
    suma = 0

    for n in notas:
        suma += n

    prom = suma / len(notas)

    if prom >= 6:
        print("aprobados")
    else:
        print("reprobados")

    return prom


notas = list(map(float, input("Ingrese notas: ").split()))
print("Promedio:", promedio(notas))
