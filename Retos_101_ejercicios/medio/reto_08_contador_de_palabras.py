"""
#8 CONTANDO PALABRAS
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 */
"""
def limpiar_texto(text:str):
    text = text.lower().replace("\n"," ").replace("\t"," ")
    signs = [".", ",", ";", ":", "¿", "?", "¡", "!","(", ")","[", "]"
            ,"{", "}","—","-","…","«","»","“","”","‘","’"]

    for sign in signs:
        text = text.replace(sign,"")
    return text.split( )



def contar_palabras(lista:list):

    frecuencia_palabras = {}
    for palabra in lista:
        if palabra not in frecuencia_palabras:
            frecuencia_palabras[palabra] = 1
        else:
            frecuencia_palabras[palabra] += 1

    return frecuencia_palabras

text = """¡HOLA MUNDO,       ESTO ES PYTHON! PYTHON ES UN LENGUAJE DE PROGRAMACIÓN. PYTHON ES USADO PARA LA CIENCIA DE DATOS.
                    ES MUY UTILIZADO PARA CIENCIA DE DATOS, ANÁLISIS DE DATOS E INTELIGENCIA ARTIFICIAL,
        PYTHON ES EL ESTÁNDAR PARA EL DESARROLLO DE INTELIGENCIA ARTIFICIAL EN EL MUNDO ENTERO.
        python también es un lenguaje de programación orientado a objetos. En python todo es un objeto"""

print(contar_palabras(limpiar_texto(text)))