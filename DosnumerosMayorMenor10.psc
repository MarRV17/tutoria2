Algoritmo DosnumerosMayorMenor
	Escribir "Ingrese dos números:"
	Leer numero1, numero2
	Si numero1 > numero2 Entonces
		Escribir numero1, " es mayor y ", numero2, " es menor."
	Sino
		Si numero1 < numero2 Entonces
			Escribir numero2, " es mayor y ", numero1, " es menor."
		Sino
			Escribir "Ambos números son iguales."
		FinSi
	FinSi
FinAlgoritmo

// 10. Solicitar dos números y mostrar cuál es mayor
// y cuál es menor usando comparaciones (>, <, =). SI