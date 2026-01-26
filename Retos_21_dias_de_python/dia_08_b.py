"""DIA 8-B Crea tu propio método map
En este desafío, deberás implementar una función personalizada que emule el comportamiento
del método map utilizando funciones de orden superior.

La función recibirá dos parámetros: una lista y una función (func).
 La lista contendrá un conjunto de elementos (números, objetos, cadenas, etc.), y
 la función se utilizará para realizar una acción específica en cada elemento de la lista.
 El objetivo es retornar una nueva lista con los resultados obtenidos de aplicar la función a cada elemento,
 de manera similar a como lo haría el método map.

Ejemplo 1:
Input: my_map([1, 2, 3, 4], lambda num: num * 2)
Output: [2, 4, 6, 8]

Ejemplo 2:
Input: my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"])
Output: ["michi", "firulais"]
"""
from collections.abc import Iterable
def my_map(lista, func):
    """Aplica una función específica sobre cada elemento de la lista dada
    Args:
        lista: iterable
        func: función invocable
    Returns:
            list: lista de elementos resultantes al aplicar la función func sobre la lista dada
    """
    if not isinstance(lista, Iterable):
        raise TypeError("La lista debe ser iterable")
    if not callable(func):
        raise TypeError("la función debe ser invocable")
    return [func(elemento) for elemento in lista ]



print(my_map([1, 2, 3, 4], lambda num: num * 2))
print(my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"]))