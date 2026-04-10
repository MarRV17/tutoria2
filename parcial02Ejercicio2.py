## Ejercicio 2
## 1. Toma la cadena de texto "Su nombre"".
## 2. Convierte el texto para que la primera letra de cada una de las palabras este en mayúscula.
## 3. Reemplaza la palabra "Su nombre" por "Su apellido" en el nuevo texto generado.

texto = "Mario Antonio Portillo Rivera"
capitalizado = texto.title()
nuevo_texto = capitalizado.replace("Mario Antonio", "Portillo Rivera")

print(nuevo_texto)
