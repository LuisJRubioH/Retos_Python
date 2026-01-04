" EL LENGUAJE HACKER "
""""
Escribe un programa que reciba un texto y transforme lenguaje natural a 
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)  con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

"""

def lenguaje_hacker(text: str):

    dic_hacker = {
        "A":"4", "B":"|3", "C":"[", "D":")", "E":"3",
        "F":r"|=", "G":"&","H":"#","I":"1", "J":r",_|",
        "K":">|", "L":"1", "M":"[V]", "N":r"^/", "O":"0",
        "P":r"|*","Q":r"(_,)", "R":"I2", "S":"5", "T":"7","U":r"(_)",
        "V":r"\/", "W":r"\/\/", "X":r"><", "Y":"j", "Z":"2"
    }

    nuevo_texto = ""
    for char in text.upper():
        nuevo_texto += dic_hacker.get(char,char)  # Usa el mismo carácter si no está en el diccionario

    return nuevo_texto

texto = "HOLA mundo"
texto_1 = "Hola mundo, estoy aprendiendo python"
print(lenguaje_hacker(texto))
print(lenguaje_hacker(texto_1))











