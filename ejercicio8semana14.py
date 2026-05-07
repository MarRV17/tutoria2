## 8. Crear un programa que almacene 5 productos en un arreglo
# y mediante una función busque un producto específico ingresado por el usuario.


def buscar(productos, item):
    for p in productos:
        if p == item:
            return True
    return False


productos = []

for i in range(5):
    productos.append(input("Producto: "))

buscar_prod = input("Buscar producto: ")

if buscar(productos, buscar_prod):
    print("Encontrado")
else:
    print("No encontrado")
