# Diccionario global con las cantidades iniciales de agua y alimento en el ecosistema
recursos_ecosistema = {"agua": 1000, "alimento": 800}


# Define la función que simula el consumo de recursos según el tipo de animal
def animal_interactua(
    tipo_animal: str, cantidad_alimentos: int, cantidad_agua: int | None = None
):
    """
    Simula cómo un animal consume recursos del ecosistema tras validar disponibilidad.

    Args:
        tipo_animal (str): Tipo de animal ("herbívoro" o "carnívoro").
        cantidad_alimentos (int): Unidades de alimento requeridas.
        cantidad_agua (int | None): Unidades de agua requeridas (opcional; por defecto None -> 0).

    Returns:
        None: Modifica el diccionario global y muestra el resultado en consola.
    """
    # Si no se indica cantidad_agua (None), se asigna 0 por defecto
    agua_consumida = 0 if cantidad_agua is None else cantidad_agua

    # Comprueba disponibilidad antes de modificar los recursos del ecosistema
    if tipo_animal == "herbívoro":
        if (
            recursos_ecosistema["agua"] < agua_consumida
            or recursos_ecosistema["alimento"] < cantidad_alimentos
        ):
            print("Recursos insuficientes en el ecosistema")
            return

        # Resta agua y alimento y muestra el mensaje correspondiente
        recursos_ecosistema["agua"] -= agua_consumida
        recursos_ecosistema["alimento"] -= cantidad_alimentos
        print(
            f"Un herbívoro ha consumido {agua_consumida} de agua y "
            f"{cantidad_alimentos} de alimento."
        )

    elif tipo_animal == "carnívoro":
        if recursos_ecosistema["alimento"] < cantidad_alimentos:
            print("Recursos insuficientes en el ecosistema")
            return

        # Resta únicamente alimento y muestra el mensaje correspondiente
        recursos_ecosistema["alimento"] -= cantidad_alimentos
        print(f"Un carnívoro ha consumido {cantidad_alimentos} de alimento.")

    else:
        print("Tipo de animal no reconocido")
        return

    # Muestra el estado actual del ecosistema tras un consumo válido
    print(f"Estado actual del ecosistema: {recursos_ecosistema}.")


# Define la función que incrementa el agua disponible en el ecosistema por lluvia
def lluvia(cantidad_agua: int):
    """
    Simula un evento de lluvia incrementando el agua en el ecosistema.

    Args:
        cantidad_agua (int): Unidades de agua que se añadirán al ecosistema.

    Returns:
        None: Actualiza el diccionario de recursos y muestra un mensaje en consola.
    """
    recursos_ecosistema["agua"] += cantidad_agua
    print(
        f"¡Ha llovido! Se añadieron {cantidad_agua} unidades de agua al ecosistema."
    )


# Flujo principal fuera de las funciones
print(f"Inicio del día en el ecosistema: {recursos_ecosistema}")

animal_interactua("herbívoro", 100, 200)
animal_interactua("carnívoro", 50)
lluvia(200)

print(f"Fin del día en el ecosistema: {recursos_ecosistema}")