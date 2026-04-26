## 5. Validación de contraseña
## •	Con while, pide una contraseña hasta que sea correcta.
## •	Usa if para verificar si coincide.
## •	Después, usa for para mostrar cuántos intentos fallidos hubo.

clave_correcta = "dragones"
intentos_fallidos = 0

while True:
    clave = input("Ingrese la contraseña: ")

    if clave == clave_correcta:
        print("Acceso correcto")
        break
    else:
        print("Incorrecta")
        intentos_fallidos += 1

for i in range(intentos_fallidos):
    print("Intento fallido", i + 1)
