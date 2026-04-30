## 6. Números primos en rango
## •	Pide un número n.
## •	Usa for para recorrer del 1 a n.
## •	Dentro, usa otro for con if para verificar si cada número es primo.
## •	Repite con while hasta que el usuario ingrese 0.

while True:
    n = int(input("Ingrese un número (0 para salir): "))

    if n == 0:
        break

    for num in range(1, n + 1):
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False

            if es_primo:
                print(num)
