"""dia 3-A  Averigua si un año es bisiesto
Debes crear la lógica de la función is_leap_year, que determina si un año es bisiesto o no.
Un año es bisiesto si cumple con las siguientes condiciones:

Es divisible por 4, pero no por 100.
Si es divisible por 100 debe serlo por 400 también.
La función is_leap_year recibe un único parámetro: el año a evaluar.
Debe devolver True si el año es bisiesto o False en caso contrario.

Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos.

Ejemplo 1:
Input: 2000;
Output: true;

Ejemplo 2:
Input: -2024;
Output: false;

Ejemplo 3:
Input: 1984.25;
Output: false;
"""
def is_leap_year(year:int) -> bool:
    """Determina si un año es bisiesto.
    Un año es bisiesto si es divisible por 4 y no por 100,
    salvo que también sea divisible por 400.

    Args:
        year (int): año a evaluar.

    Returns:
        bool: True si el año es bisiesto; False si no lo es,
        si no es un entero o si es menor o igual a cero.
    """

    if not isinstance(year, int) or year <= 0:
        return False

    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)


print(is_leap_year(1700))
print(is_leap_year(2000))
print(is_leap_year(-2014))
print(is_leap_year(1984.25))