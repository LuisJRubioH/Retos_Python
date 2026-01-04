"""#5 ÁREA DE UN POLÍGONO
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""
def calcular_area(poligono:str,base:float, altura: float) -> float:
    """calcula el área de un polígono dado
    Args:
        polígono (str): Triángulo, Cuadrado y Rectángulo
        base (float): valor de la base
        altura (float): Valor de la altura

    Returns:
            Retorna el cálculo del área del polígono dado Triángulo, Cuadrado o Rectángulo
    """
    poligono = poligono.lower()

    if base <= 0 or altura <= 0:
        raise ValueError("Los valores de las longitudes de los lados deben ser positivos y mayores que cero")

    if poligono == "cuadrado" and base != altura:
        raise ValueError("En un cuadrado, base y altura deben ser iguales")

    if poligono == "triangulo":
        area = (base *  altura) / 2
        print(f"El área del {poligono} es A = ({(base)} *  {(altura)}) / 2 = {area} unidades cuadradas")
        return area

    elif poligono == "cuadrado" or poligono == "rectangulo" :
        area = (base * altura)
        print(f"El área del {poligono} es A = ({(base)} *  {(altura)}) = {area} unidades cuadradas")
        return area
    else:
        raise ValueError("Polígono no soportado")


calcular_area("triangulo", 5.6, 8)
calcular_area("cuadrado", 6.5, 6.5)
calcular_area("rectangulo", 7.3, 4.5)

