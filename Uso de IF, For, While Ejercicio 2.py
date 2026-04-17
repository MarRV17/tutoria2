## Ejercicio 2:
## Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).


for i in range(1):
    continuar = "s"

    while continuar == "s":
        edad = int(input("Ingrese su edad: "))

        if edad < 18:
            print("Menor de edad")
        elif edad < 60:
            print("Mayor de edad")
        else:
            print("Adulto mayor")
