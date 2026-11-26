def cabecera():
    """Muestra la cabecera de la aplicacion"""
    titulo = r"""
  ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮                                                                                                                                                                                                                                                                        
"""
    print(titulo)

def crear_tag_basico(nombre):
    """
    Crea un gamertag basico usando las primeras 4 letras.
    Parametro:
    nombre(str) El nombre del usuario

    Retorna:
    str: Gamertag Basico
    """

    tag = nombre[:4]
    return tag


def crear_tag_invertido(nombre):
    
    """
    Crear un gamertag invirtiendo e nombre completo
    Parametro:
    nombre(str) El nombre del usuario
    
    Retorna:
    str: Gamertag Invertido
    """
    tag = nombre[::-1]
    return tag

def crear_tag_intercalado(nombre, apellido):
    """
    Crear un gamertag intercalado de la inciiales del nombre y apellido
    y seguidas del resto de cada uno
        Parametro:
        nombre(str) El nombre del usuario
        apellido(str) El apellido del usuario
        
        Retorna:
        str: Gamertag Intercalado
    """
   #Primera letra del nombre
    inicial_nombre = nombre[0]
   #Primera letra del apellido
    inicial_apellido =  apellido[0]
    #Resto del nombre
    resto_noombre = nombre[1:]
    #Resto apellido
    resto_apellido = apellido[1:]
    print("3. TAG INTERCALADO: ", inicial_nombre, inicial_apellido, resto_noombre, resto_apellido, sep="")


def crear_tag_elite(nombre):
     """
        Crear un gamertag elite del nombre las primeras dos letras y ultimas dos letras
    
            Parametro:
            nombre(str) El nombre del usuario
            
            Retorna:
            str: Gamertag Elite
        """
     #Primeras 2 letras
     inicio= nombre[:2] 
     #Ultimas 2 letras
     final = nombre [-2:]
     print("4. TAG ELITE: ", inicio, final, sep="")
     
def crear_tag_numero(nombre, numero_favorito):
     """
        Crear un gamertag del nombre con las primeras 5 letras
          y el numero favorito
    
            Parametro:
            nombre(str) El nombre del usuario
            numero_favorito(int) El numero favorito del usuario
            
            Retorna:
            str: Gamertag numero favorito
    """
     print("5. TAG CON NUMERO : ", nombre[:5],numero_favorito, sep="")
     
def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
    
    Parámetro:
    nombre (str): El nombre del usuario
    
    Retorna:
    str: Estadistica
    """
    longitud_nombre = len (nombre)

    print("\n📊 ESTADÍSTICAS DE TU NOMBRE:")
    print(f"Nombre completo: {nombre}")
    print(f"Longitud del Nombre: {longitud_nombre}")
    print(f"Primera letra: {nombre[0]}")
    print(f"Ultima letra: {nombre[-1]}")

    

def generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags.
    
    Parámetros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (int): Número favorito
    
    Retorna:
    None (imprime directamente)
    """
    print("\n====================================")
    print("🎯 TUS OPCIONES DE GAMERTAG:")
    print("====================================")

    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BÁSICO:", tag_basico)
    print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_numero(nombre, numero)

    print("\n====================================")

# ====================
# Aplicacion principal
# ====================
# Mostrar Cabecera

cabecera()

#Solicitar datos al usuario

nombre = input("\n 👤Introduce tu nombre: ")
apellido = input("\n 📝Introduce tu apellido ")
numero = input("\n 🔢Introduce tu nmero favorito: ")

#Mostrar estadisticas del nombre

mostrar_estadisticas(nombre)

# Generar y mostrar todas las opciones de gamertag
generar_todas_opciones(nombre, apellido, numero)

print("\n ✨ ¡Elige tu favorito y conquista el mundo gamer! ✨ ")