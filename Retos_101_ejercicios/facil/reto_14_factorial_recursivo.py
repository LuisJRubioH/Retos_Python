"""#14FACTORIAL RECURSIVO
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def calcular_factorial(n):
    """calcula de manera recursiva el factorial de un número entero mayor o igual a cero
    Args:
        n: int
    Returns:
        int: factorial del número n
    """

    if not isinstance(n, int):
        raise TypeError("n debe ser un número entero mayor o igual que cero")
    if n < 0:
        raise ValueError("n debe ser un número entero mayor o igual que cero")
    if n == 0:
        return 1

    return n * calcular_factorial(n-1)


print(calcular_factorial(0))
print(calcular_factorial(1))
print(calcular_factorial(7))
print(calcular_factorial("4"))