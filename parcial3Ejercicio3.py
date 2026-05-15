temps = []

for i in range(5):
    t = int(input("Ingresa temperatura: "))
    temps.append(t)

for t in temps:
    match t:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
            print(estado)
