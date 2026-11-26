# ============================================
# ANALIZADOR DE RENTABILIDAD INMOBILIARIA
# ============================================

# Diccionario con las tasas de ITP (Impuesto de Transmisiones Patrimoniales) en porcentaje
tasas_itp = {
    "Baja california": 2.0,
    "Aguascalientes": 2.4,
    "Ciudad de México": 9.0,
    "Estado de México": 3.25,
    "Jalisco": 4.0,
    "Campeche": 2.0,
    "Oaxaca": 2.0,
    "Nuevo León": 3.0,
    "Guerrero": 2.0,
    "Sinaloa": 2.0,
}


def crear_propiedad(direccion, precio, metros, habitaciones, comunidad_autonoma, tipo_inmueble):
    """
    Crea un diccionario con toda la información de una propiedad.

    Parámetros:
        direccion (str): Dirección o ubicación del inmueble.
        precio (float): Precio de compra de la propiedad.
        metros (float): Superficie en metros cuadrados.
        habitaciones (int): Número de habitaciones.
        comunidad_autonoma (str): Región o comunidad seleccionada para consultar el ITP.
        tipo_inmueble (str): Tipo de inmueble (por ejemplo, "Urbano" o "Rústico").

    Retorna:
        dict: Diccionario con los datos de la propiedad y su precio por metro cuadrado.
    """
    # Calcula el costo por cada metro cuadrado a partir del precio total y la superficie
    precio_por_m2 = precio / metros

    # Diccionario principal que agrupa todos los atributos de la propiedad
    propiedad = {
        "direccion": direccion,
        "precio_compra": precio,
        "metros_cuadrados": metros,
        "habitaciones": habitaciones,
        "comunidad_autonoma": comunidad_autonoma,
        "tipo_inmueble": tipo_inmueble,
        "precio_por_m2": precio_por_m2,
    }
    return propiedad


def crear_financiamiento(entrada_porcentaje, tasa_anual, plazo_años, precio_total):
    """
    Crea un diccionario con la información y cuota mensual del financiamiento.

    Parámetros:
        entrada_porcentaje (float): Porcentaje del precio pagado como entrada inicial.
        tasa_anual (float): Tasa de interés anual en porcentaje.
        plazo_años (int): Duración del préstamo en años.
        precio_total (float): Precio total de compra de la propiedad.

    Retorna:
        dict: Diccionario con montos, cuota mensual y total a pagar del préstamo.
    """
    # Monto que se paga de entrada según el porcentaje indicado
    entrada_monto = precio_total * (entrada_porcentaje / 100)

    # Capital restante que se solicitará mediante financiamiento
    monto_financiado = precio_total - entrada_monto

    # Convierte la tasa anual (en porcentaje) a tasa mensual decimal
    tasa_mensual = (tasa_anual / 100) / 12

    # Cantidad total de cuotas mensuales durante todo el plazo
    num_pagos = plazo_años * 12

    # Fórmula francesa de amortización para calcular la cuota fija mensual
    cuota_mensual = (
        monto_financiado
        * (tasa_mensual * ((1 + tasa_mensual) ** num_pagos))
        / (((1 + tasa_mensual) ** num_pagos) - 1)
    )

    # Suma de todas las cuotas mensuales a lo largo del plazo
    total_a_pagar = cuota_mensual * num_pagos

    # Diccionario con el resumen completo del financiamiento
    financiamiento = {
        "entrada_porcentaje": entrada_porcentaje,
        "entrada_monto": entrada_monto,
        "monto_financiado": monto_financiado,
        "tasa_anual": tasa_anual,
        "plazo_años": plazo_años,
        "cuota_mensual": cuota_mensual,
        "total_a_pagar": total_a_pagar,
    }

    return financiamiento


def calcular_ibi(precio_compra, tipo_inmueble):
    """
    Calcula el IBI anual de forma estimada según el tipo de inmueble.

    Parámetros:
        precio_compra (float): Precio de compra de la vivienda.
        tipo_inmueble (str): Tipo de inmueble ("Urbano" o "Rústico").

    Retorna:
        float: IBI anual estimado.
    """
    # Selecciona la tasa según el tipo usando booleanos (True=1, False=0)
    tasa_ibi = 0.00428 * (tipo_inmueble == "Urbano") + 0.00567 * (tipo_inmueble == "Rústico")

    # Estima el valor catastral como el 70% del precio de compra (corregido: antes usaba * 70)
    valor_catastral = precio_compra * 0.70

    # Multiplica el valor catastral por la tasa correspondiente para obtener el IBI anual
    ibi_anual = valor_catastral * tasa_ibi

    return ibi_anual


def calcular_total_lista(lista_gastos):
    """
    Suma los montos de los tres primeros gastos de una lista de tuplas.

    Parámetros:
        lista_gastos (list): Lista de tuplas con formato (concepto, monto).

    Retorna:
        float: Total sumado de los gastos.
    """
    # Acumulador que irá sumando cada gasto
    total = 0

    # En cada tupla (concepto, monto), el índice [1] corresponde al monto numérico
    total += lista_gastos[0][1]  # Primer gasto mensual
    total += lista_gastos[1][1]  # Segundo gasto mensual
    total += lista_gastos[2][1]  # Tercer gasto mensual

    return total


def crear_ingresos_alquiler(renta_mensual, meses_ocupados):
    """
    Crea un diccionario con la proyección de ingresos por alquiler.

    Parámetros:
        renta_mensual (float): Renta esperada por mes.
        meses_ocupados (int): Cantidad de meses al año en que estará alquilada (0 a 12).

    Retorna:
        dict: Diccionario con renta mensual, meses ocupados, ingreso anual y tasa de ocupación.
    """
    # Ingreso total proyectado en el año según los meses ocupados
    ingreso_anual = renta_mensual * meses_ocupados

    # Porcentaje del año en que la propiedad genera ingresos por alquiler
    tasa_ocupacion = (meses_ocupados / 12) * 100

    # Diccionario con los datos de ingresos del alquiler
    ingresos = {
        "renta_mensual": renta_mensual,
        "meses_ocupados": meses_ocupados,
        "ingreso_anual": ingreso_anual,
        "tasa_ocupacion": tasa_ocupacion,
    }

    return ingresos


def calcular_gastos_compra_iniciales(precio, comunidad_autonoma):
    """
    Calcula los gastos iniciales asociados a la compra según la comunidad autónoma.

    Parámetros:
        precio (float): Precio de compra de la propiedad.
        comunidad_autonoma (str): Clave de la comunidad en tasas_itp.

    Retorna:
        tuple: Tupla con (impuesto_itp, notaria_registro, total).
    """
    # Busca la tasa porcentual de ITP correspondiente a la comunidad elegida
    tasa = tasas_itp[comunidad_autonoma]

    # Calcula el impuesto de transmisiones aplicando el porcentaje sobre el precio
    impuesto = precio * (tasa / 100)

    # Estima gastos de notaría y registro como el 1.5% del precio de compra
    notaria = precio * 0.015

    # Suma ambos conceptos para obtener el total de gastos iniciales de compra
    total = impuesto + notaria

    return (impuesto, notaria, total)


def calcular_metricas_rentabilidad(
    ingresos_anuales,
    gastos_anuales_operativos,
    gastos_anuales_totales,
    precio_propiedad,
    inversion_inicial,
):
    """
    Calcula indicadores clave de rentabilidad y retorno de la inversión.

    Parámetros:
        ingresos_anuales (float): Ingresos totales por alquiler en un año.
        gastos_anuales_operativos (float): Gastos operativos anuales sin contar la hipoteca.
        gastos_anuales_totales (float): Gastos anuales totales (incluyendo hipoteca).
        precio_propiedad (float): Precio de compra del inmueble.
        inversion_inicial (float): Desembolso inicial total (entrada más gastos de compra).

    Retorna:
        tuple: Tupla con (rentabilidad_bruta, rentabilidad_neta, cap_rate, roi_años).
    """
    # Rentabilidad bruta: ingresos anuales frente al precio de compra
    rentabilidad_bruta = (ingresos_anuales / precio_propiedad) * 100

    # Beneficio neto anual tras restar todos los gastos (operativos + hipoteca)
    beneficio_neto = ingresos_anuales - gastos_anuales_totales

    # Rentabilidad neta sobre el capital inicial invertido
    rentabilidad_neta = (beneficio_neto / inversion_inicial) * 100

    # NOI (Net Operating Income): ingresos anuales menos gastos operativos sin hipoteca
    noi = ingresos_anuales - gastos_anuales_operativos

    # Cap Rate: rendimiento operativo anual respecto al precio de compra
    cap_rate = (noi / precio_propiedad) * 100

    # Años estimados para recuperar la inversión inicial con el beneficio neto anual
    roi = inversion_inicial / beneficio_neto if beneficio_neto != 0 else float("inf")

    return (rentabilidad_bruta, rentabilidad_neta, cap_rate, roi)


def calcular_flujo_caja(ingresos_dict, gastos_mensuales_lista, cuota_hipoteca):
    """
    Calcula el flujo de caja mensual y anual de la inversión.

    Parámetros:
        ingresos_dict (dict): Diccionario con la información de ingresos por alquiler.
        gastos_mensuales_lista (list): Lista de tuplas con los gastos mensuales.
        cuota_hipoteca (float): Cuota mensual del préstamo hipotecario.

    Retorna:
        tuple: Tupla con (flujo_mensual, flujo_anual).
    """
    # Obtiene la renta mensual esperada desde el diccionario de ingresos
    renta = ingresos_dict["renta_mensual"]

    # Suma los gastos fijos mensuales de la propiedad
    gastos_mes = calcular_total_lista(gastos_mensuales_lista)

    # Flujo mensual: lo que entra por renta menos hipoteca y gastos mensuales
    flujo_mensual = renta - cuota_hipoteca - gastos_mes

    # Proyecta el flujo mensual a 12 meses
    flujo_anual = flujo_mensual * 12

    return (flujo_mensual, flujo_anual)


def evaluar_inversion(rentabilidad_neta, cap_rate, flujo_mensual):
    """
    Evalúa la inversión con un puntaje de 0 a 100, recomendación y semáforo.

    Parámetros:
        rentabilidad_neta (float): Porcentaje de rentabilidad neta calculado.
        cap_rate (float): Porcentaje de CAP Rate calculado.
        flujo_mensual (float): Flujo de caja mensual en dinero.

    Retorna:
        tuple: Tupla con (puntuacion, recomendacion, semaforo).
    """
    # Puntaje acumulado según criterios de rentabilidad y flujo de caja
    puntuacion = 0
    puntuacion += 40 * (rentabilidad_neta >= 6)
    puntuacion += 30 * (cap_rate >= 5)
    puntuacion += 30 * (flujo_mensual > 0)

    # Asigna el texto de recomendación según el rango de puntuación obtenido
    recomendacion = (
        "Excelente Inversión" * (puntuacion >= 80)
        + "Buena Inversion" * (60 <= puntuacion < 80)
        + "Inversion Moderada" * (40 <= puntuacion < 60)
        + "Inversion Arriesgada" * (puntuacion < 40)
    )

    # Define el ícono de semáforo según el nivel de puntuación
    semaforo = (
        "🟢" * (puntuacion >= 70)
        + "🟡" * (40 <= puntuacion < 70)
        + "🔴" * (puntuacion < 40)
    )

    return (puntuacion, recomendacion, semaforo)


def solicitar_datos_propiedad():
    """
    Solicita al usuario por consola todos los datos de la propiedad, financiamiento y gastos.

    Retorna:
        dict: Diccionario completo con toda la información recopilada y calculada.
    """
    print("\n" + "=" * 60)
    print("🏠 DATOS DE LA PROPIEDAD")
    print("=" * 60)

    # Variables con los datos básicos ingresados por el usuario
    direccion = input("\n📍 Dirección: ")
    precio = float(input("💰 Precio de compra ($): "))
    metros = float(input("📏 Metros cuadrados: "))
    habitaciones = int(input("🛏️  Número de habitaciones: "))
    tipo_inmueble = input("🏘️  Tipo de inmueble (Urbano/Rústico): ")

    # Muestra las comunidades disponibles tomadas de las claves de tasas_itp
    print("\n🗺️  COMUNIDADES AUTÓNOMAS:")
    comunidades_list = list(tasas_itp)

    print(f"   {comunidades_list[0]}, {comunidades_list[1]}, {comunidades_list[2]}")
    print(f"   {comunidades_list[3]}, {comunidades_list[4]}, {comunidades_list[5]}")
    print(f"   {comunidades_list[6]}, {comunidades_list[7]}, {comunidades_list[8]}")
    print("   (y más...)")

    comunidad = input("\n🏛️  Comunidad Autónoma: ")

    # Construye el diccionario de la propiedad con los datos capturados
    propiedad = crear_propiedad(direccion, precio, metros, habitaciones, comunidad, tipo_inmueble)

    print("\n" + "=" * 60)
    print("💳 FINANCIAMIENTO")
    print("=" * 60)

    # Variables con las condiciones del préstamo hipotecario
    entrada_pct = float(input("\n💵 Porcentaje de entrada (%): "))
    tasa = float(input("📈 Tasa de interés anual (%): "))
    plazo = int(input("📅 Plazo en años: "))

    # Calcula cuotas y montos del financiamiento
    financiamiento = crear_financiamiento(entrada_pct, tasa, plazo, precio)

    print("\n" + "=" * 60)
    print("🏦 INGRESOS ESPERADOS")
    print("=" * 60)

    # Variables para proyectar la renta y ocupación anual
    renta = float(input("\n💸 Renta mensual estimada ($): "))
    meses_ocup = int(input("📆 Meses ocupados al año (10-12): "))

    # Crea el diccionario de ingresos por alquiler
    ingresos = crear_ingresos_alquiler(renta, meses_ocup)

    print("\n" + "=" * 60)
    print("💸 GASTOS MENSUALES")
    print("=" * 60)

    # Gastos recurrentes de cada mes
    comunidad_gasto = float(input("\n🏢 Gastos de comunidad ($): "))
    seguro = float(input("🛡️  Seguro (mensual) ($): "))
    mantenimiento = float(input("🔧 Mantenimiento (mensual) ($): "))

    # Lista de tuplas (concepto, monto) para facilitar sumas y reportes
    gastos_mes = [
        ("Gastos de comunidad", comunidad_gasto),
        ("Seguro", seguro),
        ("Mantenimiento", mantenimiento),
    ]

    print("\n" + "=" * 60)
    print("💸 GASTOS ANUALES EXTRAS")
    print("=" * 60)

    # Calcula el IBI anual según el precio y el tipo de inmueble
    ibi = calcular_ibi(precio, tipo_inmueble)
    print(f"\n🏛️  IBI calculado automáticamente: {ibi:,.2f}$")

    # Gasto anual adicional previsto para reparaciones o imprevistos mayores
    mant_extra = float(input("🔨 Mantenimiento extraordinario (anual) ($): "))

    # Lista de gastos anuales extra en formato de tuplas
    gastos_anuales = [
        ("IBI (Impuesto Municipal)", ibi),
        ("Mantenimiento extraordinario", mant_extra),
    ]

    # Diccionario central que reúne todas las secciones del análisis
    analisis_completo = {
        "propiedad": propiedad,
        "financiamiento": financiamiento,
        "ingresos": ingresos,
        "gastos_mensuales": gastos_mes,
        "gastos_anuales": gastos_anuales,
        # Conjunto (set) sin duplicados con las categorías principales de gasto
        "categorias_gasto": {"Hipoteca", "Mantenimiento", "Impuestos", "Seguros", "Comunidad"},
        "comunidades_disponibles": tasas_itp,
    }

    return analisis_completo


def mostrar_reporte_completo(datos):
    """
    Genera e imprime en consola el reporte completo de rentabilidad inmobiliaria.

    Parámetros:
        datos (dict): Diccionario con toda la información del análisis.
    """
    # Extrae cada bloque desde el diccionario principal para trabajar más cómodamente
    propiedad = datos["propiedad"]
    financ = datos["financiamiento"]
    ingresos = datos["ingresos"]
    gastos_mes = datos["gastos_mensuales"]
    gastos_anuales = datos["gastos_anuales"]

    print("\n\n" + "=" * 70)
    print("📊 ANÁLISIS DE RENTABILIDAD INMOBILIARIA")
    print("=" * 70)

    # INFORMACIÓN BÁSICA
    print("\n🏠 PROPIEDAD")
    print(f"   📍 Dirección: {propiedad['direccion']}")
    print(f"   💰 Precio: {propiedad['precio_compra']:,.0f}$")
    print(f"   📏 Superficie: {propiedad['metros_cuadrados']}m²")
    print(f"   🛏️  Habitaciones: {propiedad['habitaciones']}")
    print(f"   🏘️  Tipo: {propiedad['tipo_inmueble']}")
    print(f"   🏛️  Comunidad: {propiedad['comunidad_autonoma']}")
    print(f"   📐 Precio/m²: {propiedad['precio_por_m2']:,.2f}$")

    # FINANCIAMIENTO
    print("\n💳 FINANCIAMIENTO")
    print(f"   Entrada ({financ['entrada_porcentaje']}%): {financ['entrada_monto']:,.0f}$")
    print(f"   Monto financiado: {financ['monto_financiado']:,.0f}$")
    print(f"   Tasa: {financ['tasa_anual']}% anual")
    print(f"   Plazo: {financ['plazo_años']} años")
    print(f"   Cuota mensual: {financ['cuota_mensual']:,.2f}$")
    print(f"   Total a pagar: {financ['total_a_pagar']:,.0f}$")

    # GASTOS DE COMPRA
    # Desempaqueta la tupla devuelta por calcular_gastos_compra_iniciales
    imp, not_reg, total_compra = calcular_gastos_compra_iniciales(
        propiedad["precio_compra"],
        propiedad["comunidad_autonoma"],
    )
    tasa_itp_propiedad = datos["comunidades_disponibles"][propiedad["comunidad_autonoma"]]

    print("\n📋 GASTOS INICIALES")
    print(f"   ITP ({tasa_itp_propiedad}%): {imp:,.0f}$")
    print(f"   Notaría y registro: {not_reg:,.0f}$")
    print(f"   Total gastos compra: {total_compra:,.0f}$")

    # Inversión inicial total: dinero de entrada más impuestos y gastos de compra
    inversion_inicial = financ["entrada_monto"] + total_compra
    print(f"\n💵 INVERSIÓN INICIAL TOTAL: {inversion_inicial:,.0f}$")

    # INGRESOS
    print("\n📈 INGRESOS PROYECTADOS")
    print(f"   Renta mensual: {ingresos['renta_mensual']:,.0f}$")
    print(f"   Meses ocupados: {ingresos['meses_ocupados']}/12")
    print(f"   Tasa ocupación: {ingresos['tasa_ocupacion']:.1f}%")
    print(f"   Ingreso anual: {ingresos['ingreso_anual']:,.0f}$")

    # GASTOS MENSUALES
    print("\n💸 GASTOS MENSUALES")
    print(f"   {gastos_mes[0][0]}: {gastos_mes[0][1]:,.0f}$")
    print(f"   {gastos_mes[1][0]}: {gastos_mes[1][1]:,.0f}$")
    print(f"   {gastos_mes[2][0]}: {gastos_mes[2][1]:,.0f}$")
    total_gastos_mes = calcular_total_lista(gastos_mes)
    print(f"   Subtotal mensual: {total_gastos_mes:,.0f}$")

    # GASTOS ANUALES
    print("\n💸 GASTOS ANUALES EXTRAS")
    print(f"   {gastos_anuales[0][0]}: {gastos_anuales[0][1]:,.0f}$")
    print(f"   {gastos_anuales[1][0]}: {gastos_anuales[1][1]:,.0f}$")

    # Suma los gastos anuales extraordinarios (IBI + mantenimiento extra)
    gastos_anuales_extra = gastos_anuales[0][1] + gastos_anuales[1][1]

    # Gastos anuales totales incluyendo los 12 meses de hipoteca
    total_gastos_anuales = (total_gastos_mes * 12) + gastos_anuales_extra + (financ["cuota_mensual"] * 12)

    # Gastos operativos anuales excluyendo la hipoteca (útil para calcular NOI y CAP Rate)
    total_gastos_anuales_operativos = (total_gastos_mes * 12) + gastos_anuales_extra

    print(f"   Total gastos anuales (con hipoteca): {total_gastos_anuales:,.0f}$")

    # CATEGORÍAS
    print("\n🏷️  CATEGORÍAS DE GASTOS")
    # Ordena alfabéticamente los elementos del set para mostrarlos de forma consistente
    categorias_lista = sorted(datos["categorias_gasto"])
    print(f"   {', '.join(categorias_lista)}")

    # FLUJO DE CAJA
    flujo_mes, flujo_año = calcular_flujo_caja(
        ingresos,
        gastos_mes,
        financ["cuota_mensual"],
    )
    print("\n💰 FLUJO DE CAJA")
    print(f"   Mensual: {flujo_mes:,.2f}$")
    print(f"   Anual: {flujo_año:,.2f}$")

    # RENTABILIDAD
    rent_bruta, rent_neta, cap, roi = calcular_metricas_rentabilidad(
        ingresos["ingreso_anual"],
        total_gastos_anuales_operativos,
        total_gastos_anuales,
        propiedad["precio_compra"],
        inversion_inicial,
    )

    print("\n📊 INDICADORES DE RENTABILIDAD")
    print(f"   Rentabilidad bruta: {rent_bruta:.2f}%")
    print(f"   Rentabilidad neta: {rent_neta:.2f}%")
    print(f"   CAP Rate: {cap:.2f}%")
    print(f"   Recuperación inversión: {abs(roi):.1f} años")

    # EVALUACIÓN
    puntos, recomendacion, semaforo = evaluar_inversion(rent_neta, cap, flujo_mes)

    print("\n🎯 EVALUACIÓN FINAL")
    print(f"   Puntuación: {puntos}/100")
    print(f"   {semaforo} {recomendacion}")

    print("\n" + "=" * 70)


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

# Banner inicial del programa en consola
cabecera = """
╔══════════════════════════════════════════════════════════════════╗
║          🏢 ANALIZADOR DE INVERSIÓN INMOBILIARIA 🏢              ║
║                                                                  ║
║              Análisis de rentabilidad para alquiler              ║
║                          España                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
print(cabecera)

print("\n💡 Bienvenido al analizador de inversión inmobiliaria")
print("    Este sistema te ayudará a evaluar si comprar una vivienda")
print("    para alquilarla es una buena inversión.\n")

# Solicita todos los datos y arma el diccionario completo del análisis
datos_completos = solicitar_datos_propiedad()

# Imprime en consola el reporte detallado con métricas y evaluación final
mostrar_reporte_completo(datos_completos)

# Notas finales de orientación
print("\n💡 NOTAS IMPORTANTES:")
print("   • Este análisis usa estimaciones generales")
print("   • Rentabilidad neta >6% = Excelente | 4-6% = Buena | <4% = Baja")
print("   • CAP Rate >5% = Recomendado para mercados estables")
print("\n✨ ¡Gracias por usar el Analizador! ✨\n")