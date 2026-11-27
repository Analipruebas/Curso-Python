# Define el diccionario inicial con los datos y la lista de experiencias del perfil laboral
perfil_laboral = {
    "nombre": "Ana",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "experiencias": ["Ingeniera de software en XYZ Corp"],
}


# Define la función para añadir una experiencia laboral a la lista dentro del diccionario
def agregar_experiencia(perfil_laboral, nueva_experiencia):
    """
    Agrega una nueva experiencia laboral a la lista 'experiencias' del perfil.

    Args:
        perfil_laboral (dict): Diccionario con nombre, apellido, edad, ciudad y experiencias.
        nueva_experiencia (str): Descripción de la nueva experiencia laboral a añadir.

    Returns:
        dict: Diccionario del perfil laboral con la lista de experiencias actualizada.
    """
    # Añade el nuevo elemento al final de la lista asociada a la clave 'experiencias'
    perfil_laboral["experiencias"] += [nueva_experiencia]

    # Devuelve el diccionario actualizado
    return perfil_laboral


# Define la función para imprimir un resumen breve del currículum a partir del diccionario
def generar_cv_reducido(perfil_laboral):
    """
    Imprime en consola un resumen del perfil laboral a partir de sus datos.

    Args:
        perfil_laboral (dict): Diccionario con nombre, apellido, edad, ciudad y experiencias.

    Returns:
        None: Esta función muestra la información por pantalla y no retorna un valor.
    """
    # Imprime el encabezado con nombre y apellido
    print(f"CV de {perfil_laboral['nombre']} {perfil_laboral['apellido']}")
    # Imprime edad y ciudad en una sola línea
    print(f"Edad: {perfil_laboral['edad']}, Ciudad: {perfil_laboral['ciudad']}")
    # Imprime la lista de experiencias almacenada en el diccionario
    print(f"Experiencia: {perfil_laboral['experiencias']}")


# Define la nueva experiencia laboral a incorporar
nueva_experiencia = "Gerente de proyecto en ABC Inc"
# Actualiza el perfil llamando a agregar_experiencia y guarda el resultado
perfil_actualizado = agregar_experiencia(perfil_laboral, nueva_experiencia)
# Genera e imprime el resumen del CV con los datos actualizados
generar_cv_reducido(perfil_actualizado)