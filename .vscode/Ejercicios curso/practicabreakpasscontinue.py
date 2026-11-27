# Define la función simulador_alarma que simula el estado de una alarma cada segundo
def simulador_alarma(tiempo_total):
    """
    Simula una alarma segundo a segundo hasta alcanzar el tiempo total,
    omitiendo la alerta en múltiplos de 10.

    Args:
        tiempo_total (int): Duración total de la simulación en segundos.

    Returns:
        None: Imprime el estado de la alarma en consola y no retorna un valor.
    """
    # Inicializa el contador de segundos en 0 antes de iniciar el bucle
    segundo_actual = 0

    # Bucle infinito controlado internamente con 'break' al llegar a tiempo_total
    while True:
        # 1. Incrementamos el contador en 1 en cada iteración
        segundo_actual += 1

        # 2. Si el segundo es múltiplo de 10, omitimos la alarma con 'continue'
        if segundo_actual % 10 == 0:
            print(f"Omitiendo alarma en segundo {segundo_actual}")

            # Si además este es el tiempo total, rompemos el bucle aquí mismo
            if segundo_actual == tiempo_total:
                break
            continue

        # 3. Si no es múltiplo de 10, la alarma está activada
        print(f"Alarma activada, segundo actual: {segundo_actual}")

        # 4. Usamos 'break' para terminar el bucle al alcanzar el tiempo total
        if segundo_actual == tiempo_total:
            break

    # 5. Mensaje final fuera del bucle
    print(f"Alarma desactivada a los {tiempo_total} segundos")


# Invocamos la función con 21 segundos de prueba
simulador_alarma(21)