## Ejercicio 6:
## Pide un número del 1 al 7 y muestra el día de la semana correspondiente.
## Si no está en el rango, muestra un mensaje de error.

for i in range(1):
    continuar = "s"

    while continuar == "s":
        dia = int(input("Número (1-7): "))

        if dia == 1:
            print("Lunes")
        elif dia == 2:
            print("Martes")
        elif dia == 3:
            print("Miércoles")
        elif dia == 4:
            print("Jueves")
        elif dia == 5:
            print("Viernes")
        elif dia == 6:
            print("Sábado")
        elif dia == 7:
            print("Domingo")
        else:
            print("Error")
