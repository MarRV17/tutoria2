## 7. Promedio de notas
## •	Con while, permite ingresar notas hasta que el usuario escriba -1.
## •	Usa if para ignorar notas inválidas (menores a 0 o mayores a 10).
## •	Luego usa for para recorrer las notas válidas y calcular el promedio.

notas = []

while True:
    nota = float(input("Ingrese nota (-1 para terminar): "))

    if nota == -1:
        break

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida")

suma = 0

for n in notas:
    suma += n

if len(notas) > 0:
    print("Promedio:", suma / len(notas))
else:
    print("No hay notas válidas")
