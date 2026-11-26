def cabecera():
    """Muestra la cabecera de la aplicación en consola."""
    # Texto raw (r""") para evitar que caracteres como '\' se interpreten como escapes
    titulo = r"""
  ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮                                                                                                                                                                                                                                                                        
"""
    # Imprime el banner inicial del programa
    print(titulo)


def crear_tag_basico(nombre):
    """Crea un gamertag básico usando las primeras 4 letras del nombre.

    Args:
        nombre (str): Nombre del usuario.

    Returns:
        str: Gamertag básico con los primeros 4 caracteres.
    """
    # Corta desde el inicio (índice 0) hasta antes del índice 4
    tag = nombre[:4]
    return tag


def crear_tag_invertido(nombre):
    """Crea un gamertag invirtiendo todo el texto del nombre.

    Args:
        nombre (str): Nombre del usuario.

    Returns:
        str: Nombre escrito de atrás hacia adelante.
    """
    # El paso -1 recorre la cadena completa en orden inverso
    tag = nombre[::-1]
    return tag


def crear_tag_intercalado(nombre, apellido):
    """Imprime un gamertag combinando iniciales y restos de nombre y apellido.

    Args:
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
    """
    # Primera letra del nombre
    inicial_nombre = nombre[0]

    # Primera letra del apellido
    inicial_apellido = apellido[0]

    # Resto del nombre a partir del segundo carácter
    resto_nombre = nombre[1:]

    # Resto del apellido a partir del segundo carácter
    resto_apellido = apellido[1:]

    # sep="" une las partes sin espacios intermedios al imprimir
    print("3. TAG INTERCALADO: ", inicial_nombre, inicial_apellido, resto_nombre, resto_apellido, sep="")


def crear_tag_elite(nombre):
    """Imprime un gamertag usando las primeras 2 y últimas 2 letras del nombre.

    Args:
        nombre (str): Nombre del usuario.
    """
    # Primeras 2 letras del nombre
    inicio = nombre[:2]

    # Últimas 2 letras del nombre (índices negativos cuentan desde el final)
    final = nombre[-2:]

    # Imprime ambas partes pegadas sin espacios extras
    print("4. TAG ELITE: ", inicio, final, sep="")


def crear_tag_numero(nombre, numero_favorito):
    """Imprime un gamertag con las primeras 5 letras del nombre y un número.

    Args:
        nombre (str): Nombre del usuario.
        numero_favorito (str | int): Número favorito del usuario.
    """
    # Toma hasta 5 letras del nombre y concatena el número favorito
    print("5. TAG CON NUMERO : ", nombre[:5], numero_favorito, sep="")


def mostrar_estadisticas(nombre):
    """Muestra en consola la longitud, primera y última letra del nombre.

    Args:
        nombre (str): Nombre del usuario.
    """
    # Calcula cuántos caracteres tiene el nombre
    longitud_nombre = len(nombre)

    print("\n📊 ESTADÍSTICAS DE TU NOMBRE:")
    print(f"Nombre completo: {nombre}")
    print(f"Longitud del Nombre: {longitud_nombre}")
    # nombre[0] obtiene el primer carácter y nombre[-1] obtiene el último
    print(f"Primera letra: {nombre[0]}")
    print(f"Ultima letra: {nombre[-1]}")


def generar_todas_opciones(nombre, apellido, numero):
    """Genera y muestra todas las opciones de gamertags disponibles.

    Args:
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        numero (str | int): Número favorito del usuario.
    """
    print("\n====================================")
    print("🎯 TUS OPCIONES DE GAMERTAG:")
    print("====================================")

    # Guarda el resultado de crear_tag_basico en una variable antes de imprimirlo
    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BÁSICO:", tag_basico)

    # Llama directo a crear_tag_invertido dentro del print
    print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))

    # Estas tres funciones ya imprimen su propio resultado en consola
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_numero(nombre, numero)

    print("\n====================================")


# ====================
# Aplicacion principal
# ====================
# Mostrar cabecera de bienvenida
cabecera()

# Solicitar datos básicos al usuario por consola (input siempre devuelve str)
nombre = input("\n 👤Introduce tu nombre: ")
apellido = input("\n 📝Introduce tu apellido: ")
numero = input("\n 🔢Introduce tu numero favorito: ")

# Mostrar estadísticas del nombre ingresado
mostrar_estadisticas(nombre)

# Generar y mostrar todas las opciones de gamertag
generar_todas_opciones(nombre, apellido, numero)

print("\n ✨ ¡Elige tu favorito y conquista el mundo gamer! ✨ ")