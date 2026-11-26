# ===========================================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ===========================================================


def calcular_IMC(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en metros.

    Fórmula: IMC = peso (kg) / (altura (m))^2

    Parámetros:
        peso_kg (float): Peso en kilogramos.
        altura_m (float): Altura en metros.

    Retorna:
        float: El IMC calculado.
    """
    # Calcula el IMC dividiendo el peso entre la altura elevada al cuadrado
    imc = peso_kg / (altura_m**2)
    return imc


def es_peso_saludable(imc):
    """
    Determina si el IMC está dentro del rango saludable.

    Rango saludable: 18.5 <= IMC < 24.9

    Parámetros:
        imc (float): Índice de Masa Corporal.

    Retorna:
        bool: True si el IMC está en el rango saludable, False de lo contrario.
    """
    # Evalúa con operadores lógicos si el IMC cae dentro del rango establecido
    return imc >= 18.5 and imc <= 24.9


def tiene_sobrepeso(imc):
    """
    Determina si una persona tiene sobrepeso según su IMC.

    Criterio médico: Se considera sobrepeso cuando el IMC es mayor o igual a 25.

    Parámetros:
        imc (float): Índice de Masa Corporal calculado.

    Retorna:
        bool: True si hay sobrepeso (IMC >= 25), False si no hay sobrepeso (IMC < 25).
    """
    # Devuelve True cuando el IMC alcanza o supera el umbral de 25
    return imc >= 25


def tiene_bajo_peso(imc):
    """
    Determina si una persona tiene bajo peso según su IMC.

    Criterio médico: Se considera bajo peso cuando el IMC es menor a 18.5.

    Parámetros:
        imc (float): Índice de Masa Corporal calculado.

    Retorna:
        bool: True si hay bajo peso (IMC < 18.5), False si no hay bajo peso (IMC >= 18.5).
    """
    # Devuelve True cuando el IMC está por debajo de 18.5
    return imc < 18.5


def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando la fórmula de Harris-Benedict.

    Fórmula:
        - Para hombres: 88.362 + (13.397 * peso en kg) + (4.799 * altura en cm) - (5.677 * edad)
        - Para mujeres: 447.593 + (9.247 * peso en kg) + (3.098 * altura en cm) - (4.330 * edad)

    Parámetros:
        peso_kg (float): Peso en kilogramos.
        altura_cm (float): Altura en centímetros.
        edad (int): Edad en años.
        es_hombre (bool): True si es hombre, False si es mujer.

    Retorna:
        float: Las calorías diarias calculadas según el sexo.
    """
    # Variable local con la estimación calórica base para hombre
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)

    # Variable local con la estimación calórica base para mujer
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)

    # En Python True equivale a 1 y False a 0, así que selecciona una fórmula u otra sin if/else
    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer


def calcular_agua_diaria(peso_kg):
    """
    Calcula los litros de agua recomendados por día.

    Recomendación médica: Se recomienda beber 35 mililitros de agua por cada kilogramo de peso corporal.

    Parámetros:
        peso_kg (float): Peso en kilogramos.

    Retorna:
        float: Litros de agua recomendados.
    """
    # Cantidad total en mililitros según el peso corporal
    militros_agua = peso_kg * 35

    # Convierte los mililitros a litros dividiendo entre 1000
    litros_agua = militros_agua / 1000
    return litros_agua


def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo recomendado durante el ejercicio.

    Fórmula médica: 220 - edad

    Parámetros:
        edad (int): Edad en años.

    Retorna:
        int: Pulsaciones por minuto máximas recomendadas.
    """
    # Estima la frecuencia cardíaca máxima restando la edad a 220
    return 220 - edad


def generar_reporte_completo(nombre, peso_kg, altura_m, edad, es_hombre):
    """
    Genera un reporte completo de salud y fitness en consola.

    Parámetros:
        nombre (str): Nombre de la persona.
        peso_kg (float): Peso en kilogramos.
        altura_m (float): Altura en metros.
        edad (int): Edad en años.
        es_hombre (bool): True si es hombre, False si es mujer.
    """
    # Línea decorativa superior del reporte (corregido: antes tenías "=*60" como texto literal)
    print("=" * 60)
    print(f"📊 REPORTE DE FITNESS Y SALUD - {nombre}")
    print("=" * 60)

    # Variables que almacenan los resultados calculados a partir de los datos recibidos
    imc = calcular_IMC(peso_kg, altura_m)
    calorias_diarias = calcular_calorias_diarias(peso_kg, altura_m * 100, edad, es_hombre)
    agua_diaria = calcular_agua_diaria(peso_kg)
    fc_maximo = calcular_ritmo_cardiaco_maximo(edad)

    # Información básica ingresada por el usuario
    print("\n👤 Datos Personales:")
    print(f"    Peso: {peso_kg} kg")
    print(f"    Altura: {altura_m} m")
    print(f"    Edad: {edad} años")
    print(f"    ¿Hombre?: {es_hombre}")

    # IMC y evaluación de rangos
    print("\n💪 Índice de Masa Corporal (IMC):")
    print(f"  Tu IMC es: {imc:.2f}")
    print(f"  ¿Peso saludable?: {es_peso_saludable(imc)}")
    print(f"  ¿Sobrepeso?: {tiene_sobrepeso(imc)}")
    print(f"  ¿Bajo peso?: {tiene_bajo_peso(imc)}")

    # Calorías e hidratación diaria
    print("\n🍽️ Nutrición:")
    print(f"  Calorías diarias recomendadas: {round(calorias_diarias, 0)} kcal")
    print(f"  Agua diaria recomendada: {round(agua_diaria, 2)} litros")

    # Zona cardíaca recomendada para cardio (60% a 80% de la FC máxima)
    print("\n❤️ Zona Cardíaca:")
    print(f"  Frecuencia cardíaca máxima: {fc_maximo} bpm")
    print(f"  Zona de cardio óptima: {round(fc_maximo * 0.6, 0)} - {round(fc_maximo * 0.8, 0)} bpm")

    print("\n" + "=" * 60)


# ============================
# PROGRAMA PRINCIPAL
# ============================

# Banner inicial del programa en consola
cabecera = """
╔════════════════════════════════════════════════════════════╗
║     💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪         ║
║                                                            ║
║        ¡Descubre tus métricas de salud óptimas!            ║
╚════════════════════════════════════════════════════════════╝
"""

print(cabecera)

# Variables que guardan los datos capturados desde la terminal y convertidos al tipo adecuado
nombre = input("\n👤 ¿Cuál es tu nombre?: ")
peso = float(input("⚖️ ¿Cuánto pesas? (kg): "))
altura = float(input("📏 ¿Cuánto mides? (metros, ej: 1.75): "))
edad = int(input("🎂 ¿Cuántos años tienes?: "))
sexo = input("⚤ ¿Eres hombre o mujer? (H/M): ")

# Convierte la respuesta de texto a booleano (corregido: antes tenías `sexo == "h" == "hombre"`, que siempre era False)
es_hombre = sexo.strip().lower() in ("h", "hombre")

# Ejecuta el reporte final con todos los valores recopilados
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n✨ ¡Cuida tu salud! ✨")