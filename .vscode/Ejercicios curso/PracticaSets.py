# Colección de arte con elementos duplicados
coleccion = [
    "Mona Lisa",
    "El Grito",
    "Mona Lisa",
    "La Noche Estrellada",
    "Las Meninas",
    "Guernica",
    "La Última Cena",
    "La Creación de Adán",
    "La Persistencia de la Memoria",
    "La Libertad guiando al pueblo",
    "El Beso",
    "Nacimiento de Venus",
    "El Jardín de las Delicias",
    "La Joven de la Perla",
    "El David",
    "Los Girasoles",
    "La Gran Ola de Kanagawa",
    "La Ronda Nocturna",
    "American Gothic",
    "Los Jugadores de Cartas",
    "La Noche Estrellada",
    "La Última Cena",
    "Guernica",
    "Las Meninas",
    "La Persistencia de la Memoria",
    "Mona Lisa",
]


# Definimos la función que recibe la colección y devuelve una lista sin duplicados
def revisar_coleccion(coleccion):
    """
    Elimina las obras duplicadas convirtiendo la colección en un conjunto (set)
    y devuelve el resultado como una lista.

    Args:
        coleccion (list): Lista de nombres de obras de arte, posiblemente con duplicados.

    Returns:
        list: Nueva lista con las obras de arte únicas (sin orden garantizado).
    """
    # Convierte la lista en un set para descartar elementos repetidos automáticamente
    coleccion_set = set(coleccion)
    # Convierte el set de vuelta a una lista
    lista_set = list(coleccion_set)
    # Retorna la nueva lista sin duplicados
    return lista_set


# Llama a la función y guarda la lista resultante en coleccion_actualizada
coleccion_actualizada = revisar_coleccion(coleccion)

# Imprime los valores de la colección antes de la revisión
print(f"Colección antes de la revisión:\n{coleccion}")
# Imprime los valores de la colección después de la revisión
print(f"Colección después de la revisión:\n{coleccion_actualizada}")