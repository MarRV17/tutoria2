## 10. Suma acumulativa con límite
## •	Con while, pide números hasta que la suma supere 100.
## •	Usa if para ignorar números negativos.
## •	Luego usa for para mostrar todos los números válidos ingresados.

suma = 0
numeros_validos = []

while suma <= 100:
    num = int(input("Ingrese un número: "))

    if num >= 0:
        suma += num
        numeros_validos.append(num)
    else:
        print("Número ignorado")

print("Suma total:", suma)

for n in numeros_validos:
    print("Número válido:", n)
