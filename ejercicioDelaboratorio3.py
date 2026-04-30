## Ejercicio de laboratio 3
## Sistema de empleados:
## for lista, if salario, while menú, select case cargo.

# Sistema de empleados para una empresa de ingenieros en sistema.

empleados = []

## WHILE MENÚ
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        salario = float(input("Ingrese salario: "))

        print("Seleccione cargo:")
        print("1. Gerente")
        print("2. Supervisor")
        print("3. Operario")
        print("4. Director")
        print("5. Técnico")

        cargo_op = input("Opción: ")

        ## SELECT CASE CARGO (simulado con if-elif)
        if cargo_op == "1":
            cargo = "Gerente"
        elif cargo_op == "2":
            cargo = "Supervisor"
        elif cargo_op == "3":
            cargo = "Operario"
        elif cargo_op == "4":
            cargo = "Director"
        elif cargo_op == "5":
            cargo = "Técnico"
        else:
            cargo == "Desconocido"

        empleados.append([nombre, salario, cargo])
        print("Empleado agregado correctamente")

    elif opcion == "2":
        print("\n--- LISTA DE EMPLEADOS ---")

        ## FOR LISTA
        for emp in empleados:
            nombre, salario, cargo = emp

            print(f"Nombre: {nombre} | Cargo: {cargo} | Salario: {salario}")

            ## IF SALARIO
            if salario > 18000:
                print("-> Salario alto")
            else:
                print("-> Salario bajo")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
