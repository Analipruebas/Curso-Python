# Comentario que indica dónde se define la función (en este caso ya completada)
# Declaración de la función (debe completarlo el alumno)

# Define la función distancia_planeta que recibe dos parámetros: nombre_planeta y distancia_planeta
def distancia_planeta(nombre_planeta, distancia_planeta):
    # Imprime el nombre del planeta recibido usando una f-string
    print(f"Nombre del planeta: {nombre_planeta}")
    # Imprime la distancia en millones de kilómetros usando una f-string
    print(f"Distancia al planeta: {distancia_planeta} millones de km")

# Comentario que indica dónde se ejecuta o llama a la función
# Llamada a la función
# Llama a la función pasando "Marte" como argumento de nombre y 225 como argumento de distancia
distancia_planeta("Marte", 225)