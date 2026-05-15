codigo = input("Escriba la etiqueta de rastreo: ")

if codigo == "" or codigo is None:
    print("Error: entrada vacía")
    exit()

partes = codigo.split("-")
categoria = partes[1]
print("Categoría:", categoria)

pais = partes[2]

resultado = "Ruta Local" if pais == "SV" else "Ruta Internacional"
print(resultado)
