# Define la función generar_mensaje con el parámetro obligatorio 'nombre'
# y el parámetro opcional 'mensaje' con valor por defecto
def generar_mensaje(nombre, mensaje="Bienvenido al curso de Python"):
    """Esta funcion nos servira para generar mensaje
    keyword arguments:
    nombre -- primer argumento de la funcion (asignara nombre de la persona)
    mensaje -- segundo argumento de la funcion (por defecto "Bienvenido al curso de Python")
    """
    # Concatena (une) los textos para formar el saludo completo y lo guarda en 'var'
    var = "¡Hola, " + nombre + "! " + mensaje
    # Devuelve la cadena resultante a quien llamó a la función
    return var


# Llama a generar_mensaje("Santiago"), obtiene el texto retornado y lo imprime entre comillas dobles
print(f'"{generar_mensaje("Santiago")}"')