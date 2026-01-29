"""#13 ¿ES UN PALÍNDROMO?
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""

def es_palindromo(texto):
    texto = texto.lower().split()
    texto2 = texto[::-1]

    for palabra in texto:
        if palabra  in texto2:
            return True
    return False

print(es_palindromo("Ana lleva al oso la avellana"))
print(es_palindromo("Hola mundo"))