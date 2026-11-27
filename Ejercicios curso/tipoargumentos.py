# Define la función organizar_fiesta con un parámetro obligatorio (invitados)
# y dos parámetros con valor por defecto (tema y lugar)
def organizar_fiesta(invitados, tema="Python", lugar="aula de informática"):
    # Imprime el número de invitados usando una f-string
    print(f"Preparando una fiesta para {invitados} invitados.")
    # Imprime el tema de la fiesta (usará "Python" si no se indica otro)
    print(f"Tema de la fiesta: {tema}")
    # Imprime el lugar de la celebración (usará "aula de informática" si no se indica otro)
    print(f"Lugar de la celebración:{lugar}")

# Llama a la función pasando solo el argumento obligatorio (10); tema y lugar toman sus valores por defecto
organizar_fiesta(10)