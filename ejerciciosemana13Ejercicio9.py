## 9. Juego de adivinar número
## •	Genera un número secreto.
## •	Con while, permite intentos hasta acertar.
## •	Usa if para dar pistas (mayor o menor).
## •	Luego usa for para mostrar todos los intentos realizados.

import random

secreto = random.randint(1, 10)
intentos = []

while True:
    num = int(input("Adivina el número: "))
    intentos.append(num)

    if num == secreto:
        print("¡Correcto!")
        break
    elif num < secreto:
        print("Es mayor")
    else:
        print("Es menor")

for i in intentos:
    print("Intento:", i)
