## Ejercicio 5:
## Solicita dos números y una operación (+, -, *, /) y realiza el cálculo usando if, elif y else.

for i in range(1):
    continuar = "s"

    while continuar == "s":
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        op = input("Operación (+, -, *, /): ")

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("No se puede dividir entre 0")
        else:
            print("Operación inválida")
