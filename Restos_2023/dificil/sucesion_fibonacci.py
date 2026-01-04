"""#3 LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""

def n_esimo_fibo(n:int) -> int:

    if n == 0 :
        return 0
    if n == 1:
        return  1
    return  n_esimo_fibo(n-1) + n_esimo_fibo(n-2)

def sucesion_fibo(n):
    nums_fibo = []
    for i in range(0,n):
        nums_fibo.append(n_esimo_fibo(i))
    return nums_fibo


def fibonacci_dp(n: int):
    F = [0, 1]
    for k in range(2, n):
        F.append(F[k-1] + F[k-2])
    return F[:n]

print(fibonacci_dp(50))

