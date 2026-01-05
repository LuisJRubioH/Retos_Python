"""
En este desafío encontrarás una función llamada solution que recibe un parámetro llamado valor.
Debes encontrar el tipo de dato del parámetro valor y retornarlo desde la función found_type.
Recuerda que el parámetro valor será distinto por cada distinta forma en que ejecutemos la función found_type.

Input:
found_type(1)
found_type("Dieguillo")
found_type(True)

Output:
"number"
"string"
"boolean"
"""

def found_type(value):
    """Determina el tipo de valor de un valor dado
    Args:
        value: puede ser número, cadena, booleano.
    Returns:
        tipo de valor del valor ingresado
    """
    if isinstance(value,bool):
        return "boolean"
    elif isinstance(value, int) or isinstance(value, float):
        return "number"
    elif isinstance(value, str):
        return "string"
    else:
        return  "desconocido"


print(found_type(1))
print(found_type("Dieguillo"))
print(found_type(True))
