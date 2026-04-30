## Ejercicio 7
## 1. Toma el texto numérico "42".
## 2. Rellenalo con ceros a la izquierda hasta que alcance una longitud total de 5 caracteres.
## 3. Verifica mediante un método booleano si esa nueva cadena generada termina con el número "2".

numero = "42"
relleno = numero.zfill(5)
termina_en_2 = relleno.endswith("2")

print(relleno)
print(termina_en_2)
