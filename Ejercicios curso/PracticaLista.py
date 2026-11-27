# Define la función aumentar_biblioteca que recibe el título de un nuevo libro
def aumentar_biblioteca(nuevo_libro):
    """
    Añade un nuevo libro al final de la lista de libros leídos.

    Args:
        nuevo_libro (str): El título del libro a añadir a la lista.

    Returns:
        list: Lista actualizada de libros leídos, incluyendo el nuevo libro.
    """
    # Abre el archivo 'libros.txt' en modo lectura ("r")
    # Nota: ajusta la ruta si el archivo está en una subcarpeta (ej. "Tema_2/libros.txt")
    archivo = open("libros.txt", "r")
    # Lee todo el contenido y lo divide en una lista de líneas sin saltos de línea
    libros = archivo.read().splitlines()
    # Cierra el archivo para liberar recursos del sistema
    archivo.close()

    # Agrega el nuevo libro al final de la lista en memoria
    libros.append(nuevo_libro)
    # Devuelve la lista completa con el libro agregado
    return libros


# Define la función primer_libro_leido que recibe una lista de libros
def primer_libro_leido(libros):
    """
    Devuelve el título del primer libro leído de una lista de libros.

    Args:
        libros (list): Lista de libros leídos.

    Returns:
        str: Título del primer libro leído.
    """
    # Retorna el primer elemento de la lista (índice 0)
    return libros[0]


# Guarda el título del nuevo libro que se agregará a la lista
nuevo_libro = "Las Aventuras de Huckleberry Finn"

# Llama a aumentar_biblioteca y guarda la lista resultante en 'biblioteca'
biblioteca = aumentar_biblioteca(nuevo_libro)
# Muestra el encabezado y la lista completa de libros leídos
print("La biblioteca de libros leídos es:")
print(biblioteca)

# Obtiene el primer libro de la lista llamando a primer_libro_leido
primer_libro = primer_libro_leido(biblioteca)
# Imprime el primer libro con comillas dobles alrededor del título
print(f'El primer libro que he leído es: "{primer_libro}"')