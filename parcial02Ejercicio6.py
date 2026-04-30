## Ejercicio 6
## 1. Toma el texto "Su nombre".
## 2. Aplica el método de normalización fuerte (casefold) para prepararlo para una comparación ignorando mayúsculas.
## 3. Verifica si el texto resultante está compuesto únicamente por caracteres alfabéticos (letras) devolviendo un valor booleano.

texto = "Mario Antonio Portillo Rivera"
normalizado = texto.casefold()
es_alfabetico = normalizado.isalpha()

print(normalizado)
print(es_alfabetico)
