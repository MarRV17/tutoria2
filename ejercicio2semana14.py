## 2. Desarrollar un programa que permita
#  ingresar 10 nombres en un arreglo y luego,
#  mediante una función,
# muestre solo los nombres que tengan más de 5 caracteres.


def nombres_largos(nombres):
    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)


nombres = []

for i in range(10):
    nombres.append(input("Ingrese nombre: "))

print("Nombres con más de 5 caracteres:")
nombres_largos(nombres)
