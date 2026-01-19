"""#10 CÓDIGO MORSE
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 */
"""


def convertir_natural_morse(texto):
    dicc = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
        "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
        "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
        "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
        "$": "...-..-", "@": ".--.-.",
    }

    inv = {v: k for k, v in dicc.items()}

    # 1️⃣ Detección del tipo
    caracteres_morse = {'.', '-', ' '}
    es_morse = True

    for c in texto:
        if c not in caracteres_morse:
            es_morse = False
            break

    # 2️⃣ Conversión
    if not es_morse:
        # Natural → Morse
        texto = texto.upper()
        resultado = []

        for palabra in texto.split():
            letras = []
            for c in palabra:
                if c in dicc:
                    letras.append(dicc[c])
            resultado.append(" ".join(letras))

        return "  ".join(resultado)

    else:
        # Morse → Natural
        resultado = []

        for palabra in texto.split("  "):
            letras = []
            for simbolo in palabra.split():
                if simbolo in inv:
                    letras.append(inv[simbolo])
            resultado.append("".join(letras))

        return " ".join(resultado)


texto = "Hola mundo"
texto2 = "hola python"
texto3 = ".--. -.-- - .... --- -."
print(convertir_natural_morse(texto))
print(convertir_natural_morse(texto2))
print(convertir_natural_morse(texto3))

