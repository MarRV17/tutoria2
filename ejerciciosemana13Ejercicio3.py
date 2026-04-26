## 3. Tabla de multiplicar filtrada
## •	Pide un número.
## •	Con for, genera su tabla del 1 al 10.
## •	Usa if para mostrar solo resultados mayores a 20.
## •	Repite con while hasta que el usuario escriba -1.

while True:
    num = int(input("Ingrese un número (-1 para salir): "))

    if num == -1:
        break

    for i in range(1, 10):
        resultado = num * i
        if resultado > 20:
            print(f"{num} x {i} = {resultado}")
