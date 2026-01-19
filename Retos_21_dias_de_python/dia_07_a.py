"""DÍA # 7-A  Encuentra palabras con dos vocales
En este desafío, debes crear la lógica de la función find_words_with_two_vowels
que encuentre las palabras que contienen exactamente dos vocales en una lista de palabras.
Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva
 lista que contenga todas las palabras de la lista original que cumplan con la condición mencionada anteriormente.
 En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:
Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])
Output: ["hello", "platzi"]

Ejemplo 2:
Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: []
"""

def find_words_with_two_vowels(lista:list[str]) -> list[str]:
    """Encuentra las palabras con exactamente dos vocales en una lista de palabras
    Args:
        lista: list[str]

    Returns:
        Lista de palabras con exactamente dos vocales o lista vacía en caso contrario

    """
    vocales = {"a","e","i","o","u","A","E","I","O","U"}
    lista_palabras_dos_vocales = []
    for palabra in lista:
        total_vocales = 0
        for char in palabra:
            if char in vocales:
                total_vocales += 1
        if total_vocales == 2:
            lista_palabras_dos_vocales.append(palabra)

    return lista_palabras_dos_vocales

print(find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
]))

print(find_words_with_two_vowels(
    ["text",
     "test",
     "python",
     "example"]))

print(find_words_with_two_vowels([
    "cooper",
    "aarea",
    "Apel",
    "apel"]))