Algoritmo UnnumeroNegativo
	Suma = 0
	Repetir
		Escribir "Ingrese un número (negativo para salir):"
		Leer num
		Si num >= 0 Entonces
			Suma = Suma + num
		FinSi
	Hasta Que num < 0
	Escribir "La suma de los números positivos es: ", Suma
FinAlgoritmo

// 2. Crear un programa que permita ingresar números continuamente hasta que se ingrese un
//número negativo, y luego muestre la suma de todos los números positivos ingresados,
//utilizando la estructura repetir (Hacer o hacer mientras).
