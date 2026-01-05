"""#7INVIRTIENDO CADENAS
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def invertir_cadena(cadena:str) -> str:
    """Invierte una cadena de texto
        Args:
            cadena (str): cadena tipo string.
        Returns:
            Cadena con las posiciones de cada letra invertida
    """

    cadena_invertida = ""

    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    return cadena_invertida

print(invertir_cadena("Hola mundo"))
print(invertir_cadena("Python es un lenguaje de programación"))
