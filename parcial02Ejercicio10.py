## Ejercicio 10
## 1. Toma la cadena "Python2026".
## 2. Verifica si el texto es estrictamente alfanumérico (solo letras y números, sin espacios ni símbolos).
## 3. Si lo es, convierte el texto a minúsculas y luego separa la palabra de los números reemplazando "2026" por una cadena vacia "".

texto = "Python2026"

if texto.isalnum():
    minusculas = texto.lower()
    separado = minusculas.replace("2026", "")
    print(separado)
else:
    print("No es alfanumérico")
