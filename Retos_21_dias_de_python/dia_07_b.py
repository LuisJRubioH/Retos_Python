""""DÍA # 7-B  Calcula la longitud de las palabras
En este desafío, debes crear una función llamada count_words_by_length que recibe una
lista de palabras y devuelve un diccionario que mapea la longitud de las palabras a
la cantidad de palabras que tienen esa longitud.

Ejemplo 1:
Input:
count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

Output:
{5: 1, 6: 2, 10: 1, 4: 2}

Ejemplo 2:
Input:
count_words_by_length([
  "apple",
  "banana",
  "orange"
])
Output:
{5: 1, 6: 2}
"""
def count_words_by_length(words:list[str]) -> dict[int, int]:
    """Cuenta la cantidad de palabras con una longitud determinada
    Args:
        words: list[str]
    Returns:
            diccionario cuya clave es un entero que representa la longitud de una
            palabra y cuyo valor es la cantidad de palabras en la lista dada,con esa longitud
    """
    words_length:dict[int, int] = {}

    for word in words:
        words_length[len(word)] = words_length.get(len(word), 0) + 1

    return words_length

print(count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
]))
print(count_words_by_length([
  "apple",
  "banana",
  "orange"
]))
