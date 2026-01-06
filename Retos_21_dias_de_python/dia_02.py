"""DÍA #2 CALCULAR PROPINA
En este desafío tendrás que calcular la propina que deben dejar los clientes de un restaurante en función de su consumo.
La función calculate_tip recibirá dos parámetros, bill_amount que representa el costo total de lo que se haya consumido y
tip_percentage que representa el porcentaje de propina a dejar. Ambos valores serán de tipo float y siempre serán positivos,
incluyendo el 0. La función deberá devolver el valor de la propina como un número.

Recuerda que para redondear a dos decimales tendrás que hacer uso de round(numero, cantidad de decimales)
Tendrás inputs y outputs como los siguientes
Ejemplo 1:
Input: calculate_tip(100, 10);
Output: 10;

Ejemplo 2:
Input: calculate_tip(1524.33, 25);
Output: 381.08;
"""

def calculate_tip(bill_amount:float, tip_percentage:float) -> float:
    """Calcular la propina en función de su consumo.
    Args:
        bill_amount (float): valor de la factura a pagar
        tip_percentage (float): porcentaje de la propina

    Returns:
        propina redondeada a dos decimales
    """
    tip = (bill_amount * tip_percentage) / 100
    return round(tip, 2)



print(calculate_tip(100, 10))
print(calculate_tip(1524.33, 25))
print(calculate_tip(-33, 25))