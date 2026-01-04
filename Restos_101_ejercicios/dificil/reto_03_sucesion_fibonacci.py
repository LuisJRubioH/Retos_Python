"""#3 LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""

def fibonacci_dp(n: int):
    F = [0, 1]
    for k in range(2, n):
        F.append(F[k-1] + F[k-2])
    return F[:n]

print(fibonacci_dp(50))

