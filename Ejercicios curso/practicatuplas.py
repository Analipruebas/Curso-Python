# Importa la clase datetime desde el módulo datetime para trabajar con fechas y años
from datetime import datetime


# Define la función gestionar_informacion que recibe una tupla con datos personales
def gestionar_informacion(datos_personales):
    """
    Crearemos una funcion de tupla sobre los datos peersonales que contendra nombre, edad y ciudad
    Realizaremos una modificaicon de la tupla donde llevara el nacimento
    argumentos:
    datos_personales tupla para nombre, edad y ciudad
    datos_modificados tupla para nombre, nacimeinto y ciudad
    retorna:
    los valores de las tuplas
    """
    # Desempaqueta la tupla en tres variables individuales en el mismo orden
    nombre, edad, ciudad = datos_personales
    # Línea comentada: obtiene el año actual del sistema (no se ejecuta por tener '#')
    # año_actual = datetime.now().year
    # Calcula el año de nacimiento restando la edad al año fijo 2025
    nacimiento = 2025 - edad
    # Crea una nueva tupla con el nombre, el año de nacimiento calculado y la ciudad
    datos_modificados = (nombre, nacimiento, ciudad)

    # Retorna ambas tuplas (la original sin cambios y la nueva modificada)
    return datos_personales, datos_modificados


# Crea la tupla inicial con nombre, edad y ciudad
tupla_original = ("Ana", 30, "Madrid")
# Llama a la función y desempaqueta las dos tuplas devueltas en 'original' y 'modificada'
original, modificada = gestionar_informacion(tupla_original)
# Imprime la tupla original usando una f-string
print(f"Tupla original:{original}")
# Imprime la tupla modificada usando una f-string
print(f"Tupla modificada:{modificada}")