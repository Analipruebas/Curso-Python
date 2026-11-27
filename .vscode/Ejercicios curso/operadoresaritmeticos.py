# Define la función contar_caracteres que recibe un parámetro 'frase' (se espera de tipo str)
def contar_caracteres(frase: str):
    """Esta es una funcion para contar el numero de caracteres
    
    argumentos:
    frase 

    tipo:
    str -- hace referencia a que es un string

    variables:
    lon_msj-- usara len para calcular o contar los caracteres de la frase
    """
    # 1. Calculamos la longitud directamente de la frase que entra como argumento
    lon_msj = len(frase)

    # 2. La función IMPRIME directamente aquí adentro. 
    # Ponemos las comillas simples alrededor de {frase} para el diseño del mensaje.
    print(f"La frase '{frase}' tiene {lon_msj} caracteres.")


# 3. Llamamos a la función pasándole el texto exacto que pide el resultado esperado
contar_caracteres("Aprender Python es divertido")


# Define la función convertir_numero que recibe un parámetro 'numero' (se espera de tipo int)
def convertir_numero(numero: int):
    """Esta es una funcion que realizara la conversion del numero a string y float 
    y se usara la funcion para el tipo de dato
    argumento:
    numero -- que va a contener un numero entero
    type:
    int -- la funcion de conversion es entera
    funciones:
    str() -- convertira el numero entero a string
    float() -- convertira el numero entero a flotante (float)
    type() -- nos servira para ver que tipo o formato tiene la variable
    """
    # Para realizar la conversión del numero a Cadena y Flotante
    Con_cadena = str(numero)       # Convertirá el numero a una cadena (str)
    Con_Flotante = float(numero)   # Convertirá el numero a flotante (float)

    # Para sacar el tipo de formato de cada variable
    Ent = type(numero)         # Obtiene el tipo de dato original (int)
    Cad = type(Con_cadena)     # Obtiene el tipo de dato convertido a texto (str)
    Flo = type(Con_Flotante)   # Obtiene el tipo de dato convertido a decimal (float)

    # Imprimimos exactamente con el formato solicitado (sin espacios sobrantes al final)
    print(f"Entero: {numero}, Tipo: {Ent}")
    print(f"Cadena: {Con_cadena}, Tipo: {Cad}")
    print(f"Flotante: {Con_Flotante}, Tipo: {Flo}")


# Llamada a la función con el número entero 42
convertir_numero(42)