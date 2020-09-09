def e_cuadratica(n):

	serieEuler = 0

	for i in range(0, n+1):
		factorial = 1
		aux = 1

		while aux <= i:
			if i != 0 and i != 1:
				factorial = factorial * aux
			aux = aux + 1

		serieEuler = serieEuler + (1/factorial)

	return serieEuler


def e_lineal(n):

	serieEuler = 0
	factorial = 1

	for i in range(0,n+1):
		if i != 0 and i != 1:
			factorial = factorial * i
		serieEuler = serieEuler + (1/factorial)

	return serieEuler