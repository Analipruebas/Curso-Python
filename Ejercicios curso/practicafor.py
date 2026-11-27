def añadir_tarea(tarea):
    """
    Lee las tareas del archivo usando un bucle for, añade la nueva tarea
    y retorna la lista actualizada.
    """
    # Creamos una lista vacía donde guardaremos las tareas
    tareas = []
    
    # Abrimos el archivo y recorremos cada línea con un bucle for
    with open("tareas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # .strip() quita el salto de línea invisible al final de cada texto
            tareas += [linea.strip()]
            
    # Añadimos la nueva tarea sumándola como una lista de un solo elemento
    tareas += [tarea]
    
    return tareas

def gestionar_tareas(lista_tareas):
    """
    Recibe la lista de tareas, las imprime numeradas con un bucle for 
    e indica el total de tareas pendientes.
    """
    print("Tareas pendientes de realizar:")
    
    # Recorremos la lista usando un contador manual o enumerate si ya lo viste
    contador = 1
    for tarea in lista_tareas:
        print(f"{contador}. {tarea}")
        contador += 1
        
    # Calculamos el total contando con un bucle o usando len()
    total = 0
    for tarea in lista_tareas:
        total += 1
        
    print(f"Hay {total} tareas pendientes de realizar.")

# 1. Llamamos primero a la función 'añadir_tarea'
tareas_actualizadas = añadir_tarea("Pagar la factura del internet.")

# 2. Llamamos después a la función 'gestionar_tareas'
gestionar_tareas(tareas_actualizadas)