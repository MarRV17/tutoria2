## Ejercicio 11
## 1. Toma la cadena "  el nido matinal  ".
## 2. Limpia los espacios en blanco de los extremos y haz que la primera letra de cada palabra pase a ser mayuscula.
## 3. Toma ese texto procesado y centralo en un espacio total de 30 caracteres, rellenando los espacios a los lados con guiones medios ("-").

texto = "  el nido matinal  "
limpio = texto.strip().title()
centrado = limpio.center(30, "-")

print(centrado)
