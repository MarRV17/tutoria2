## Ejercicio 9:
## Solicita un año y determina si es bisiesto.


for i in range(1):
    continuar = "s"

    while continuar == "s":
        anio = int(input("Ingrese año: "))

        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print("Bisiesto")
        else:
            print("No bisiesto")
