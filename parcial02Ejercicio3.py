## Ejercicio 3
## 1. Crea una variable con el texto "ING. Su nombre".
## 2. Remueve el prefijo "ING. " de la cadena.
## 3. Convierte el texto restante completamente a letras mayusculas.

texto = "ING. Mario Antonio Portillo Rivera"
sin_prefijo = texto.removeprefix("ING. ")
mayusculas = sin_prefijo.upper()

print(mayusculas)
