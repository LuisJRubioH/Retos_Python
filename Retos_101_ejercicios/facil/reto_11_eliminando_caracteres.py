"""#22 ELIMINANDO CARACTERES
/*
 * Crea una función que reciba dos cadenas como parámetro (str2, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""
def eliminar_caracteres_str1(str1, str2):
    """Elimina caracteres de una cadena si estos están presentes en otra cadena dada
    Args:
        str1[str]: cadena 1
        str2[str]: cadena 2

    Returns:
            out1[str]: cadena con los caracteres de la cadena 1 que no están en la cadena 2
    """

    out = ""
    for char in str1:
        if char not in str2:
            out += char
    return out

def eliminar_caracteres_str2(str1, str2):
    """Elimina caracteres de una cadena si estos están presentes en otra cadena dada
    Args:
        str1[str]: cadena 1
        str2[str]: cadena 2

    Returns:
            out2[str]: cadena con los caracteres de la cadena 2 que no están en la cadena 1
    """
    out2 = ""
    for _ in str2:
        if _ not in str1:
            out2 += _
    return out2

def retornar_cadenas_formateadas(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("str1 y str2 deben ser cadenas")

    return f"out1 = {eliminar_caracteres_str1(str1, str2)}\nout2 = {eliminar_caracteres_str2(str1, str2)}"

print(retornar_cadenas_formateadas("Hola mundo estoy en python", "programar en python es genial"))
print(retornar_cadenas_formateadas("", ""))
print(retornar_cadenas_formateadas("Hola mundo estoy en python", ""))
print(retornar_cadenas_formateadas("", "programar en python es genial"))
print(retornar_cadenas_formateadas(4, "programar en python es genial"))