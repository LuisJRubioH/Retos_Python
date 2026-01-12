""""#9 DECIMAL A BINARIO
/*
 * Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

 EJEMPLOS
 | Decimal | Binario    |
| ------: | :--------- |
|       0 | 0          |
|       1 | 1          |
|       2 | 10         |
|       3 | 11         |
|       4 | 100        |
|       5 | 101        |
|       6 | 110        |
|       7 | 111        |
|       8 | 1000       |
|       9 | 1001       |
|      10 | 1010       |
|      11 | 1011       |
|      12 | 1100       |
|      13 | 1101       |
|      14 | 1110       |
|      15 | 1111       |
|      16 | 10000      |
|      17 | 10001      |
|      18 | 10010      |
|      19 | 10011      |
|      20 | 10100      |
|      25 | 11001      |
|      30 | 11110      |
|      32 | 100000     |
|      40 | 101000     |
|      50 | 110010     |
|      64 | 1000000    |
|     100 | 1100100    |
|     128 | 10000000   |
|     255 | 11111111   |
|     256 | 100000000  |
|     512 | 1000000000 |
|    1023 | 1111111111 |

Procedimiento paso a paso
    Sea N un entero decimal no negativo.
    - Paso 1: Divide  𝑁 entre 2.
    - Paso 2 Anota el residuo de la división (0 o 1).
    - Paso 3 Toma el cociente entero obtenido y vuelve al Paso 1.
    - Paso 4 Repite el proceso hasta que el cociente sea 0.
    - Paso 5 El número binario se obtiene leyendo los residuos de abajo hacia arriba (del último al primero).

 */"""

def convertir_decimal_a_binario(n) -> str:
    """
    Dado un número decimal entero n lo convierte en un número binario
    Args:
        n: int
    Returns (str):
            Representación binaria del numéro decimal entero n
    """
    if not isinstance(n,int) or n < 0:
        raise ValueError(f"El número n debe ser entero no negativo")

    if n == 0:
        return "0"

    cociente = n // 2
    residuos = str(n % 2)

    while cociente != 0:
        residuos = str(cociente % 2) + residuos
        cociente //= 2

    return residuos

print(convertir_decimal_a_binario(7))