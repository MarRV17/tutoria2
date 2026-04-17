## Ejercicio 3:
## Ingresa una nota del 0 al 10 y muestra:
## 9-10: Excelente
## 7-8: Bueno
## 6: Aprobado
## 0-5: Reprobado

for i in range(1):
    continuar = "s"

    while continuar == "s":
        nota = int(input("Ingrese nota (0-10): "))

        if nota >= 9:
            print("Excelente")
        elif nota >= 7:
            print("Bueno")
        elif nota == 6:
            print("Aprobado")
        else:
            print("Reprobado")
