"""" Definir una función que tome como argumentos dos números y devuelva el mayor de ellos
No usar funciones predetermindas de python con max()
"""

def max_calculator(n1:int, n2:int):

    """Dados dos números enteros de entrada, retorna el máximo ¿ 

    Args:
        nq (int): primer núemro a comparar
        n2 (int): segundo núemro a comparar

    Return: mayot de ambos
    """

    if n1 > n2:
        return f"El valor máximo es {n1}"
    elif n2 > n1:
        return f"El valor máximo es {n2}"
    elif n1 == n2:
        raise Exception("Los numeros no deben ser iguales")
    raise Exception ("Algo salió mal")

print(max_calculator(3,7))
print(max_calculator(-2,-6))
print(max_calculator(5,5))