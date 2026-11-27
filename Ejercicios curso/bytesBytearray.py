# Define la función crear_codigo_secreto que recibe un mensaje en formato bytes
def crear_codigo_secreto(mensaje):
    """
    Crea un código secreto a partir de los bytes en posiciones pares de un mensaje.

    Args:
        mensaje (bytes): Secuencia de bytes original a codificar.

    Returns:
        str: Cadena resultante de concatenar la representación hexadecimal,
        la representación en bytes extraída, el binario del primer byte y
        el binario del último byte seleccionado.
    """
    # Toma los bytes en índices pares (0, 2, 4, ...) mediante rebanado (slicing)
    repr_hex = mensaje[0::2]
    # Convierte esos bytes seleccionados a una cadena hexadecimal en minúsculas
    repr_hex = repr_hex.hex()

    # Extrae nuevamente los bytes en índices pares para obtener su representación binaria
    repr_bin = mensaje[0::2]
    # Obtiene el valor entero del primer byte (repr_bin[0]) y lo convierte a texto binario ('0b...')
    repr_bin_primero = bin(repr_bin[0])
    # Obtiene el valor entero del último byte (repr_bin[-1]) y lo convierte a texto binario ('0b...')
    repr_bin_ultimo = bin(repr_bin[-1])

    # Une todas las partes en una sola cadena de texto usando una f-string
    concatenacion = f"{repr_hex}{str(repr_bin)}{repr_bin_primero}{repr_bin_ultimo}"

    # Devuelve el código secreto generado
    return concatenacion


# Define el mensaje original como literal de bytes (prefijo b)
mensaje = b"Este es un mensaje secreto"
# Llama a la función y guarda la cadena codificada en resultado
resultado = crear_codigo_secreto(mensaje)

# Muestra el mensaje original y el código secreto generado
print(f"Mensaje original: {mensaje}")
print(f"Mensaje codificado: {resultado}")