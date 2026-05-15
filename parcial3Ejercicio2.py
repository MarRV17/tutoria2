from decimal import Decimal

total = Decimal("0")

while True:
    try:

        precio = input("Ingrese el precio del producto: ")

        precio_decimal = Decimal(precio)

        if precio_decimal == 0:
            break

        total += precio_decimal

    except ValueError:
        print("Advertencia: Debe ingresar un número válido.")

    except:
        print("Error: Entrada no válida.")

print(f"El total acumulado es: ${total}")
