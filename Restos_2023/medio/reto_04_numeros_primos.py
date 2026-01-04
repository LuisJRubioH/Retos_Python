"""#4 ¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""

def es_primo(n:int) -> bool:
    """
    Determina si un número entero n es o no un número primo.
    Un número primo es un entero mayor o igual que 2 divisible únicamente por 1 y por sí mismo.
    Es importante señalar que la definición de número primo es aplicada a enteros n mayores o iguales a 2
    Args:
        n (int): número entero a determinar si es o no primo.


    Returns:
            bool: True si el número es primo, False en caso contrario.

    """
    if n <= 1:
        return False

    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return  False
    return True

def listar_primos() -> list[int]:
    """
    Retorna una lista con todos los números primos que se encuentran el rango de 2 a 100
    """
    primos = [ ]
    for n in range(2,101):
        if es_primo(n) == True:
            primos.append(n)
    return primos

print(listar_primos())