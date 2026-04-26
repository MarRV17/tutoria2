## 2. Contador de positivos y negativos
## •	Con while, permite ingresar números hasta que el usuario escriba 0.
## •	Dentro, usa if para contar cuántos son positivos y negativos.
## •	Al final, usa un for para mostrar un resumen de resultados.

positivos = 0
negativos = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))

    if num == 0:
        break

    if num > 0:
        positivos += 1
    else:
        negativos += 1

for i in range(1):
    print("Positivos:", positivos)
    print("Negativos:", negativos)
