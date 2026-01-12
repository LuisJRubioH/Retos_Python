"""DIA #4 - A Encuentra a los gatitos más famosos
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.
Recibirás una lista de diccionarios que incluirán las siguientes propiedades:
"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores.
 Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante,
manteniendo el orden en el que aparecen en la lista de entrada.

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:
Input: find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

Output: ["Luna"]

Ejemplo 2:
Input: find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

Output: ["Milo", "Gizmo"]
"""

def find_famous_cat(lista:list[dict]) -> list[str]:
    """Determina el o los gatos más famosos según la cantidad de seguidores
    Args:
        lista: list de diccionarios

    Returns:
        lista con el nombre del gato más famoso

    """

    total_followers = [sum(gato["followers"]) for gato in lista]

    max_followers = max(total_followers)

    most_famous = [lista[j]["name"] for j, total in enumerate(total_followers) if total == max_followers]

    return most_famous