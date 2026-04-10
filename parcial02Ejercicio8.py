## Ejercicio 8
## 1. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
## 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
## 3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes.

texto = """En el silencio
canta el alma
y florece la vida"""

conteo_a = texto.count("a")
lineas = texto.splitlines()

print("Cantidad de 'a':", conteo_a)
print(lineas)
