# Define la función adivinar_palabra con los parámetros letra_prueba, palabra_adivinar y palabra_intento
def adivinar_palabra(letra_prueba, palabra_adivinar, palabra_intento):
    """
    Evalúa si una letra está en la palabra objetivo y si el intento coincide con ella.

    Args:
        letra_prueba (str): Letra a validar dentro de palabra_adivinar.
        palabra_adivinar (str): Palabra secreta o palabra a adivinar.
        palabra_intento (str): Palabra ingresada por el jugador como intento.

    Returns:
        tuple[bool, bool]: (letra_en_palabra, resultado_adivinanza).
    """
    # Verifica con el operador 'in' si letra_prueba aparece dentro de palabra_adivinar (True o False)
    letra_en_palabra = letra_prueba in palabra_adivinar

    # Compara si palabra_intento es exactamente igual a palabra_adivinar (True o False)
    resultado_adivinanza = palabra_intento == palabra_adivinar

    # Imprime si la letra está en la palabra usando una f-string
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
    # Imprime si el jugador adivinó la palabra completa
    print(f"El jugador gana:  {resultado_adivinanza}")

    # Retorna ambos resultados booleanos en una tupla
    return letra_en_palabra, resultado_adivinanza


# Palabra secreta que se debe adivinar
palabra_adivinar = "Corazon"

# Llama a la función pasando letra de prueba, palabra secreta e intento del jugador
adivinar_palabra("a", palabra_adivinar, "Mariposa")