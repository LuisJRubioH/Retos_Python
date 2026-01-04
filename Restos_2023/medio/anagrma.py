"""#2 ¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """
def es_anagrama(word1:str, word2:str) -> bool:

    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ","")

    if word1 == word2 or len(word1) != len(word2):
        return False

    return sorted(word1) == sorted(word2)


print(es_anagrama("Tom Marvolo Riddle", "I am Lord Voldemort"))
print(es_anagrama("omar","ramo"))
print(es_anagrama("listen", "silent"))
print(es_anagrama("abc", "axx"))
print(es_anagrama("lidera", "delira"))
print(es_anagrama("aab", "abc"))
