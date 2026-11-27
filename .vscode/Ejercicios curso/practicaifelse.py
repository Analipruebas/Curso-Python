# Define la función recomendar_pelicula que evalúa género y edad para devolver una recomendación
def recomendar_pelicula(genero, edad):
    """
    Recomienda una película según el género preferido y la edad del usuario.

    Args:
        genero (str): Género cinematográfico preferido (por ejemplo, "acción" o "comedia").
        edad (int): Edad del usuario en años.

    Returns:
        str: Título de la película recomendada o mensaje para explorar otros géneros.
    """
    # Si el género es "acción" y la edad es de 13 años o más, recomienda "Deadpool"
    if genero == "acción" and edad >= 13:
        pelicula = "Deadpool"
    # Si el género es "acción" pero la edad es menor a 13 años, recomienda "Regreso al futuro"
    elif genero == "acción" and edad < 13:
        pelicula = "Regreso al futuro"
    # Si el género es "comedia", recomienda "Aterriza como puedas"
    elif genero == "comedia":
        pelicula = "Aterriza como puedas"
    # Para cualquier otro género, sugiere explorar otras opciones
    else:
        pelicula = "Explorar otros géneros"

    # Devuelve la recomendación elegida
    return pelicula


# Define los datos de prueba del usuario
user_genero = "acción"
user_edad = 26

# Llama a la función y guarda la película recomendada en resultado
resultado = recomendar_pelicula(user_genero, user_edad)

# Imprime el mensaje final con los datos del usuario y la recomendación obtenida
print(
    f"Teniendo en cuenta tu edad({user_edad}) y tu genero favorito ({user_genero}), "
    f"te recomiendo la siguiente película: {resultado}"
)