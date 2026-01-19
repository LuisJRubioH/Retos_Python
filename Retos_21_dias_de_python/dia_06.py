"""DÍA # 6 Encuentre la intersección de conjuntos

En este desafío, debes implementar la lógica de la función find_set_intersection que
 encuentre la intersección de conjuntos en una lista de conjuntos.
Recibirás un único parámetro: una lista de conjuntos. La función debe encontrar la intersección de todos
los conjuntos de la lista y devolver el resultado como un nuevo conjunto. Si la lista está vacía o no hay
intersección entre los conjuntos, la función debe devolver un conjunto vacío.

Ejemplo 1:
Input:
sets = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]
find_set_intersection(sets)
Output: {3, 4}

Ejemplo 2:
Input:
sets = [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]
find_set_intersection(sets)
Output: set()
"""

def find_set_intersection(sets:list[set]) -> set:
    """Calcula el conjunto intersección de una lista de conjuntos
    Args:
        sets: lista de conjuntos

    Returns:
            Intersección de los conjuntos o conjunto vacío
    """
    if len(sets) == 0:
        return set()

    intersec = sets[0]
    for i in range(1, len(sets)):
        intersec = intersec.intersection(sets[i])
    return  intersec

sets1 = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
sets2 = [{1, 2, 3, 4}, {2, 4, 6, 8},{3, 6, 9, 12}]
sets3 = [set(), {2, 4, 6, 8},{3, 6, 9, 12}]
sets4 = []

print(find_set_intersection(sets1))
print(find_set_intersection(sets2))
print(find_set_intersection(sets3))
print(find_set_intersection(sets4))