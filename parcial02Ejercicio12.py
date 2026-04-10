## Ejercicio 12
## 1. Toma el nombre de archivo "Sunombre.txt".
## 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
## 3. Toma el texto que quede limpio, convertido a minúsculas.

archivo = "Mario Antonio Portillo Rivera.txt"
sin_txt = archivo.removesuffix(".txt")
sin_prefijo = sin_txt.removeprefix("ING. ")
resultado = sin_prefijo.lower()

print(resultado)
