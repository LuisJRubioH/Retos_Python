"""DIA #5 - A Calcula la cantidad de letras en una oración

En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de
cada letra en una cadena de texto y lo almacene en un diccionario.
Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir,
 las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:
Input: "Hola mundo"
Output: {
  'H': 1,
  'o': 2,
  'l': 1,
  'a': 1,
  ' ': 1,
  'M': 1,
  'u': 1,
  'n': 1,
  'd': 1
}
"""
def contar_caracter(texto:str) -> dict:
    """ Identifica todos los caracteres en el texto y cuenta cuántas veces aparecen cada una. Diferenciando entre mayúsculas y minúsculas.
    Args:
        texto: str
    Returns:
        diccionario con las letras y sus frecuencias
    """
    caracteres_frecuencia = {}
    for caracter in texto:
        if caracter not in caracteres_frecuencia:
            caracteres_frecuencia[caracter] = 1
        else:
            caracteres_frecuencia[caracter] += 1

    return caracteres_frecuencia

print(contar_caracter("Hola mundo"))
print(contar_caracter("Esto es Python. Python es muy importante"))
