"""" "DIA #5 -
En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.
Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista,
la función debe devolver None. Si hay más de un palíndromo con la misma longitud máxima,
debes devolver el primer palíndromo encontrado en la lista.

Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

Ejemplo 1:
Input: find_largest_palindrome(["racecar", "level", "world", "hello"])
Output: "racecar"

Ejemplo 2:
Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])
Output: None
"""

def is_palindrome(word:str):
    """Determina si una palabra es o no un palíndromo
    Args:
        word: str
    Returns:
        bool: True si es palíndromo y false en caso contrario
    """
    if word == word[::-1]:
        return True
    return False

def find_largest_palindrome(list_words):
    """
    Encuentra el la palabra más larga en una lista si esta es un palíndromo
    Args:
        list_words: list[str]

    Returns:
        str: Palíndromo de máxima longitud o None si no hay ningún en la lista.

    """
    max_long  = 0
    for word in list_words:
        if is_palindrome(word) and len(word) > max_long:
                max_long = len(word)

    for word in list_words:
        if is_palindrome(word) and len(word) == max_long:
            return  word

    return None



lista1 =  ["level", "racecar", "world", "hello"]
lista2 = ["Platzi", "Python", "django", "flask"]
lista3 = ["sometemos","reconocer","anitalatina","rotavator"]


print(find_largest_palindrome(lista1))
print(find_largest_palindrome(lista2))
print(find_largest_palindrome(lista3))