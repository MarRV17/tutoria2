## 4. Suma de números impares
## •	Con while, pide números hasta que se ingrese 0.
## •	Usa if para sumar solo los números impares.
## •	Luego usa for para imprimir cada número impar ingresado.

numeros_impares = []
suma = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))

    if num == 0:
        break

    if num % 2 != 0:
        suma += num
        numeros_impares.append(num)

print("Suma de impares:", suma)

for i in numeros_impares:
    print("Impar ingresado:", i)
