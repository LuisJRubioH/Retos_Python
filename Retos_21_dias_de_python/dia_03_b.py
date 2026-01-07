"""DÍA 3-b Dibuja un triangulo usando bucles
En este desafío, debes dibujar un triángulo equilátero usando bucles.
Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y
el carácter con el que se debe construir el triángulo, respectivamente.
Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.
Tendrás inputs y outputs como los siguientes

Ejemplo 1:
Input: printTriangle(3, "*")
Output:
  *
 ***
*****

Ejemplo 2:
Input: printTriangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$ 1
"""

def print_triangle(size:int, character:str):
    triangle = character
    for i in range(1, size + 1):
        print(" " * (size - i) + triangle)
        triangle += character * 2


print_triangle(3, "*")
print_triangle(6, "$")
