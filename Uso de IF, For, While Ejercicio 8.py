## Ejercicio 8:
## Pide tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

for i in range(1):
    continuar = "s"

    while continuar == "s":
        a = float(input("Lado 1: "))
        b = float(input("Lado 2: "))
        c = float(input("Lado 3: "))

        if a == b == c:
            print("Equilátero")
        elif a == b or a == c or b == c:
            print("Isósceles")
        else:
            print("Escaleno")
