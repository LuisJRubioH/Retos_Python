"""" Definir una función que tome como argumentos dos números
 y devuelva el mayor de ellos
No usar funciones predetermindas de python con max()
"""

def max_calculator(n1:int, n2:int):

    """Dados dos números enteros de entrada, retorna el máximo

    Args:
        n1 (int): primer núemro a comparar
        n2 (int): segundo núemro a comparar

    Return: mayor de ambos
    """

    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        raise Exception("Los numeros no deben ser iguales")
    raise Exception ("Algo salió mal")

print(max_calculator(3,7))
print(max_calculator(-2,-6))

"""" Definir una función que tome como argumentos dos números 
y devuelva el mayor de ellos
No usar funciones predetermindas de python con max()
"""

def max_entre_tres(n1:int, n2:int, n3:int):

    """ Dados tres núemros y retornamos el mayor
    Args:
        n1 (int): primer número a comparar
        n2 (int): segundo número a comparar
        n3 (int): tercer número a comparar
    Returns: mayor de los tres
    """
    n = max_calculator(n1,n2)
    n_max = max_calculator(n3,n)
    
    return n_max

print(max_entre_tres(2,5,3))
print(max_entre_tres(2,-5,1))
print(max_entre_tres(-6,0,-3))

print(max_calculator(5,5))
