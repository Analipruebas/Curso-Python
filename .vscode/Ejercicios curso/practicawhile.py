# Define la función mover_ascensor que simula el desplazamiento piso a piso hasta el destino
def mover_ascensor(piso_actual, piso_deseado):
    """
    Simula el movimiento de un ascensor piso por piso usando un bucle while
    hasta alcanzar el piso deseado.

    Args:
        piso_actual (int): Número del piso en el que inicia el ascensor.
        piso_deseado (int): Número del piso al que se desea llegar.

    Returns:
        None: Imprime el recorrido en consola y no retorna un valor.
    """
    # Repite el movimiento mientras el piso actual sea distinto del piso deseado
    while piso_actual != piso_deseado:
        # Si el piso actual está por debajo del destino, sube un piso
        if piso_actual < piso_deseado:
            print(f"Subiendo al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual += 1
        # En caso contrario (está por encima del destino), baja un piso
        else:
            print(f"Bajando al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual -= 1

    # Al salir del bucle, piso_actual ya coincide con piso_deseado
    print(f"Piso {piso_actual} alcanzado")


# Llama a la función partiendo del piso 2 hacia el piso 6
mover_ascensor(2, 6)