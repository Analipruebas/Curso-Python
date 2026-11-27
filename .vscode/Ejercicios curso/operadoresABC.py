# Define la función comparar_longitud que recibe dos palabras (palabra1 y palabra2)
def comparar_longitud(palabra1, palabra2):
    """
    Realizaremos la comparación de longitud de dos palabras: asignación y booleanos.

    Args:
        palabra1 (str): Será la primera palabra a comparar.
        palabra2 (str): Será la segunda palabra a comparar.

    Returns:
        bool: Retorna True si ambas palabras tienen la misma longitud, o False si no la tienen.
    """
    # Calcula cuántos caracteres tiene palabra1 y lo guarda en longitud1
    longitud1 = len(palabra1)
    # Calcula cuántos caracteres tiene palabra2 y lo guarda en longitud2
    longitud2 = len(palabra2)

    # Compara ambas longitudes con '==' y guarda un booleano (True o False) en resultado
    resultado = longitud1 == longitud2

    # Devuelve el resultado booleano a quien llamó a la función
    return resultado


# Llama a la función con "gato" (4 letras) y "perro" (5 letras) e imprime el resultado en una nueva línea
print(f'¿Son "gato" y "perro" dos palabras con la misma longitud?\n{comparar_longitud("gato", "perro")}')