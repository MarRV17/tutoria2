## Ejercicio 10:
## Pide usuario y contraseña. Si ambos coinciden con valores predefinidos,
## muestra "Acceso permitido", de lo contrario "Acceso denegado".


for i in range(1):
    continuar = "s"

    while continuar == "s":
        user = input("Usuario: ")
        password = input("Contraseña: ")

        if user == "mariovx" and password == "dragones":
            print("Acceso permitido")
        else:
            print("Acceso denegado")
