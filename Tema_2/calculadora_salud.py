# ===========================================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ===========================================================

def calcular_IMC(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en metros.
    
    Formula: IMC = peso (kg) / (altura (m))^2

    Pametros:
    peso_kg (float): Peso en kilogramos.
    altura_m (float): Altura en metros.

    Retorna:
        float: El IMC calculado.
    """

  
    imc = peso_kg / (altura_m ** 2)
    return imc


def es_peso_saludable(imc):
    """
    Determina si el IMC está dentro del rango saludable.
    
    Rango saludable: 18.5 <= IMC < 24.9

    Parametros:
    imc (float): Índice de Masa Corporal.

    Retorna:
        bool: True si el IMC está en el rango saludable, False de lo contrario.
    """
    # Operadores de comparación y lógicos
    # para determinar si el IMC está en el rango saludable
    #es_saludable = imc >= 18.5 and imc <= 24.9
    #return es_saludable
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    """
    Descripción: Determina si una persona tiene sobrepeso segun su IMC.
    
    Criterio médico: Se considera sobrepeso cuando el IMC es mayor o igual a  25

    Parametros:
    imc (float): Índice de Masa Corporal calculado.

    Retorna:
        bool: True si hay sobrepeso (IMC >= 25), False si no hay sobrepeso (IMC < 25).
    """
    return imc >= 25 

def tiene_bajo_peso(imc):
    """
    Descripción: Determina si una persona tiene bajo peso según su IMC.

    Criterio médico: Se considera bajo peso cuando el IMC es menor a 18.5

    Parametros:
    imc (float): Índice de Masa Corporal calculado.

    Retorna:
        bool: True si hay bajo pesos (IMC < 18.5), False Si no hay bajo peso (IMC >= 18.5).
    """
    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Descripción: Calcula las calorías diarias recomendadas usando la fórmula de Harris-Benedict.
    
    Fórmula:
    - Para hombres: 88.362 + (13.397 * peso en kg) + (4.799 * altura en cm) - (5.677 * edad)
    - Para mujeres: 447.593 + (9.247 * peso en kg) + (3.098 * altura en cm) - (4.330 * edad)

    Parametros:
    peso_kg (float): Peso en kilogramos.
    altura_cm (float): Altura en centímetros.
    edad (int): Edad en años.
    es_hombre (bool): True si es hombre, False si es mujer.

    Retorna:
        float: Las calorías diarias calculadas segun el sexo.
    """
    
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)

    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    #Usa el hecho de que True=1 y False=0
    return es_hombre * calorias_hombre +(1 - es_hombre) * calorias_mujer

def calcular_agua_diaria(peso_kg):
    """
    Descripción: Calcula los litros de agua recomendados por día.
    Recomendación médica: Se recomienda beber 35 mililitros de agua por cada kilogramo de peso corporal.

    Parametros:
    peso_kg (float): Peso en kilogramos.

    Retorna:
        float: Litros de agua recomendados.
    """
    militros_agua =  peso_kg * 35
    litros_agua = militros_agua / 1000
    return litros_agua

def calcular_ritmo_cardiaco_maximo(edad):
    """
    Descripción: Calcula el ritmo cardíaco máximo recomendado durante el ejercicio.
    
    Fórmula medica: 220 - edad

    Parametros:
    edad (int): Edad en años.

    Retorna:
        int: Pulsaciones por minuto máximas recomendadas.
    """
    return 220 - edad

def generar_reporte_completo(nombre,peso_kg, altura_m, edad, es_hombre):
    """
    Descripción: Genera un reporte completo de salud y fitness.
    Parametros:
    peso_kg (float): Peso en kilogramos.
    altura_m (float): Altura en metros.
    edad (int): Edad en años.
    es_hombre (bool): True si es hombre, False si es mujer.

    """
    print("=*60")
    print(f"📊REPORTE DE FITNESSS Y SALUD- {nombre}")
    print("="*60)

    #Calculos

    imc = calcular_IMC(peso_kg, altura_m)
    calorias_diarias = calcular_calorias_diarias(peso_kg, altura_m*100, edad, es_hombre)
    agua_diaria = calcular_agua_diaria(peso_kg)
    fc_maximo = calcular_ritmo_cardiaco_maximo(edad)

    #Información basica
    print(f"\n👤 Datos Personales:")
    print(f"    Peso: {peso_kg} kg")
    print(f"    Altura: {altura_m} m")
    print(f"    Edad: {edad} años")
    print(f"    ¿Hombre?: {es_hombre}")

    #IMC y evaluación
    print(f"\n💪 Índice de Masa Corporal (IMC):")
    print(f"  Tu IMC es: {imc:.2f}")
    print(f"  ¿Peso saludable?: {es_peso_saludable(imc)}")
    print(f"  ¿Sobrepeso?: {tiene_sobrepeso(imc)}")
    print(f"  ¿Bajo peso?: {tiene_bajo_peso(imc)}")
    
    #Calorias
    print(f"\n🍽️ Nutrición:")
    print(f"  Calorías diarias recomendadas: {round(calorias_diarias,0)} kcal")
    print(f"  Agua diaria recomendada: {round(agua_diaria,2)} litros")

    #Cardio
    print(f"\n❤️ Zona Cardíaca:")
    print(f"  Frecuencia cardíaca máxima: {fc_maximo} bpm")
    print(f"  Zona de cardio óptima: {round(fc_maximo*0.6,0)} -{round(fc_maximo*0.8,0)} bpm")

    print("\n"+ "="*60)

# ============================
# PROGRAMA PRINCIPAL
# ===========================

cabecera ="""
╔════════════════════════════════════════════════════════════╗
║     💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪         ║
║                                                            ║
║        ¡Descubre tus métricas de salud óptimas!            ║
╚════════════════════════════════════════════════════════════╝
"""

print(cabecera)

#Solciitar datos al usuario

nombre = input("\n👤¿Cuál es tu nombre?: ")
peso = float(input("⚖️ ¿Cuanto pesas?(kg): "))
altura = float(input("📏 ¿Cuanto mides?(metros, ej: 1.75): "))
edad = int(input("🎂 ¿Cuantos años tienes?: "))
sexo = input("⚤  ¿Eres hombre o mujer? (H/M): ")

#Convertir el sexo a booleano
es_hombre = sexo == "H" or sexo == "h" == "hombre"

#Generar el reporte completo
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n✨ ¡Cuida tu salud! ✨")



   