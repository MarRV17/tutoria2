nombre = input("Ingresa tu nombre completo (Nombre/Apellido): ")

lista = nombre.split()

lista_invertida = lista[::-1]

for palabra in lista_invertida:

    for i in range(len(palabra)):
        if i < len(palabra) - 1:
            print(palabra[i], end=".")
        else:
            print(palabra[i], end="")

    print()
