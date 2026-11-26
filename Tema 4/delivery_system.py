

"""
Sistema de Pedidos de Restaurante con Delivery.
"""

# ===== BASE DE DATOS DEL RESTAURANTE =====

# Diccionario anidado con el menú por categoría; cada platillo guarda precio, tiempo (min) y puntos
menu = {
    "entradas": {
        "Nachos": {"precio": 8.50, "tiempo": 10, "puntos": 50},
        "Alitas BBQ": {"precio": 12.00, "tiempo": 15, "puntos": 80},
        "Ensalada César": {"precio": 9.00, "tiempo": 8, "puntos": 60},
        "Croquetas": {"precio": 7.50, "tiempo": 12, "puntos": 45},
    },
    "principales": {
        "Pizza Margherita": {"precio": 15.00, "tiempo": 20, "puntos": 100},
        "Pizza Pepperoni": {"precio": 16.50, "tiempo": 20, "puntos": 110},
        "Hamburguesa Clásica": {"precio": 13.50, "tiempo": 18, "puntos": 90},
        "Hamburguesa BBQ": {"precio": 14.50, "tiempo": 18, "puntos": 95},
        "Pasta Carbonara": {"precio": 14.00, "tiempo": 15, "puntos": 95},
        "Pasta Bolognesa": {"precio": 13.00, "tiempo": 15, "puntos": 85},
    },
    "postres": {
        "Helado": {"precio": 5.00, "tiempo": 2, "puntos": 30},
        "Tarta de Queso": {"precio": 6.50, "tiempo": 3, "puntos": 40},
        "Brownie": {"precio": 5.50, "tiempo": 3, "puntos": 35},
        "Flan": {"precio": 4.50, "tiempo": 2, "puntos": 25},
    },
    "bebidas": {
        "Refresco": {"precio": 3.00, "tiempo": 1, "puntos": 15},
        "Agua": {"precio": 2.00, "tiempo": 1, "puntos": 10},
        "Jugo Natural": {"precio": 4.50, "tiempo": 3, "puntos": 25},
        "Café": {"precio": 2.50, "tiempo": 2, "puntos": 15},
    },
}

# Diccionario de clientes VIP indexado por nombre en minúsculas con puntos y pedidos acumulados
clientes_vip = {
    "juan": {"puntos": 500, "pedidos": 12},
    "maria": {"puntos": 1200, "pedidos": 28},
    "pedro": {"puntos": 300, "pedidos": 7},
    "ana": {"puntos": 850, "pedidos": 19},
    "luis": {"puntos": 150, "pedidos": 3},
}

# Diccionario de promociones; cada combo usa un set de platillos requeridos y un porcentaje de descuento
combos_del_dia = {
    "Combo Italiano": {
        "items": {"Pizza Margherita", "Refresco"},
        "descuento": 15,  # Porcentaje de descuento
    },
    "Combo Burger": {
        "items": {"Hamburguesa Clásica", "Nachos", "Refresco"},
        "descuento": 20,
    },
    "Combo Light": {
        "items": {"Ensalada César", "Agua", "Flan"},
        "descuento": 10,
    },
}

# ===== FUNCIONES DEL SISTEMA =====


def mostrar_bienvenidad():
    """Muestra el mensaje de bienvenida del restaurante."""
    # Imprime el encabezado decorativo en consola
    print("=" * 60)
    print("=" * 15 + "🍕 ¡Bienvenido a Python Eats! 🍕")
    print("=" * 60)
    print()


def verificar_cliente():
    """
    Verifica si el cliente está registrado y retorna su información.

    Retorna:
        tuple: Tupla con (nombre_cliente, puntos_disponibles, es_vip).
    """
    # Guarda la respuesta del usuario sobre si ya está registrado
    es_cliente = ""

    # Repite la pregunta hasta recibir una respuesta válida
    while es_cliente not in ["s", "n", "si", "no"]:
        es_cliente = input("¿Eres cliente registrado? (s/n): ").strip().lower()
        if es_cliente not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' para si o 'n' para no.")

    if es_cliente in ["s", "si"]:
        # Nombre ingresado para buscarlo en clientes_vip
        nombre = input("Ingresa tu nombre: ").strip()

        # Busca en minúsculas para que funcione aunque escriban "Ana" o "ANA"
        if nombre.lower() in clientes_vip:
            # Puntos acumulados que tiene registrados el cliente VIP
            puntos = clientes_vip[nombre.lower()]["puntos"]
            print(f"\n✨ ¡Hola {nombre}! Tienes {puntos} puntos acumulados.")
            print(f"📊 Has realizado {clientes_vip[nombre.lower()]['pedidos']} pedidos con nosotros.")
            return nombre, puntos, True
        else:
            print(f"\n👋 Hola {nombre}! No estás registrado como cliente VIP.")
            print("Te registraremos automáticamente después de tu pedido.")
            return nombre, 0, False

    else:
        print("\n👋 ¡Bienvenido nuevo cliente!")
        # Nombre del nuevo cliente para identificar su sesión y registro posterior
        nombre = input("¿Cómo te llamas? ").strip()
        print(f"    Gracias {nombre}, te registraremos después del pedido.")
        return nombre, 0, False


def mostrar_menu_principal():
    """Muestra el menú principal de opciones."""
    # Imprime las opciones disponibles del sistema
    print("\n" + "=" * 40)
    print("     MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. 📖 Ver menú completo")
    print("2. 🛒 Realizar pedido")
    print("3. 🎁 Ver ofertas del día")
    print("4. ⭐ Canjear puntos")
    print("5. 🚪 Salir")
    print("=" * 40)


def mostrar_menu_completo():
    """Muestra todos los productos disponibles organizados por categoría."""
    print("\n" + "=" * 50)
    print("         MENÚ COMPLETO")
    print("=" * 50)

    # Recorre cada categoría (entradas, principales, postres, bebidas)
    for categoria in menu:
        print(f"\n🍴 {categoria}")
        print("-" * 30)

        # Numeración visual de los platillos dentro de cada categoría
        contador = 1
        # Diccionario de platillos de la categoría actual
        productos = menu[categoria]

        for nombre in productos:
            # Diccionario con precio, tiempo y puntos del platillo
            info = productos[nombre]
            precio = info["precio"]
            tiempo = info["tiempo"]
            puntos = info["puntos"]
            print(f"{contador}. {nombre}")
            print(f"     💵 ${precio:.2f} | ⏱️ {tiempo} min | ⭐ {puntos} pts")
            contador += 1

    print("\n" + "=" * 50)
    # Pausa la pantalla para que el usuario pueda leer el menú antes de volver
    input("\nPresiona Enter para continuar...")


def mostrar_ofertas():
    """Muestra los combos especiales del día."""
    print("\n" + "=" * 50)
    print("       🎁 OFERTAS DEL DÍA 🎁")
    print("=" * 50)

    # Contador para enumerar cada combo en pantalla
    contador = 1

    for nombre_combo in combos_del_dia:
        # Datos del combo: conjunto de platillos (items) y porcentaje de descuento
        info_combo = combos_del_dia[nombre_combo]
        # Acumula los nombres de los productos incluidos en el combo
        productos = ""
        for item in info_combo["items"]:
            productos += f"{item}, "
        print(f"\n{contador}. {nombre_combo}")
        # [:-2] quita la última coma y el espacio sobrante al final de la cadena
        print(f"   Incluye: {productos[:-2]}")
        print(f"   💥 {info_combo['descuento']}% de descuento")
        contador += 1

    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")


def calcular_precio_con_puntos(total, puntos_disponibles):
    """
    Pregunta si el cliente quiere usar sus puntos y calcula el descuento.

    Argumentos:
        total (float): Total actual del pedido.
        puntos_disponibles (int): Puntos disponibles del cliente.

    Retorna:
        tuple: Tupla con (nuevo_total, puntos_usados).
    """
    if puntos_disponibles == 0:
        return total, 0

    # Conversión de puntos a dinero: 100 puntos equivalen a $1.00
    descuento_maximo = puntos_disponibles / 100

    print(f"\n💰 Tienes {puntos_disponibles} puntos disponibles")
    print(f"   Equivalen a un descuento de hasta ${descuento_maximo:.2f}")

    # Guarda la decisión del cliente sobre aplicar o no sus puntos
    usar = ""
    while usar not in ["s", "n", "si", "no"]:
        usar = input("¿Deseas usar tus puntos? (s/n): ").strip().lower()
        if usar not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' o 'n'")

    if usar in ["s", "si"]:
        # Cantidad de puntos que el cliente desea canjear en este pedido
        puntos_a_usar = 0
        while True:
            entrada = input(f"¿Cuántos puntos quieres usar? (máx {puntos_disponibles}): ").strip()

            # Revisa carácter por carácter que la entrada sea un número entero positivo
            es_numero = True
            for char in entrada:
                if char not in "0123456789":
                    es_numero = False
                    break

            if es_numero and entrada != "":
                puntos_a_usar = int(entrada)
                if 0 <= puntos_a_usar <= puntos_disponibles:
                    # Convierte los puntos elegidos a su valor en dinero
                    descuento = puntos_a_usar / 100
                    if descuento <= total:
                        return total - descuento, puntos_a_usar
                    else:
                        print(f"❌ El descuento (${descuento:.2f}) es mayor que el total")
                else:
                    print(f"❌ Debes ingresar un número entre 0 y {puntos_disponibles}")
            else:
                print("❌ Por favor, ingresa un número válido")

    return total, 0


def verificar_combo(items_pedido):
    """
    Verifica si los ítems del pedido forman algún combo del día.

    Argumentos:
        items_pedido (list): Lista de nombres de productos incluidos en el pedido.

    Retorna:
        tuple: Tupla con (nombre_combo, descuento) o (None, 0) si no aplica ninguno.
    """
    for nombre_combo in combos_del_dia:
        info_combo = combos_del_dia[nombre_combo]

        # all() devuelve True solo si cada producto requerido del combo está en items_pedido
        if all(item in items_pedido for item in info_combo["items"]):
            return nombre_combo, info_combo["descuento"]

    return None, 0


def realizar_pedido(nombre_cliente, puntos_disponibles):
    """
    Gestiona el armado del carrito y procesa el pedido final del cliente.

    Argumentos:
        nombre_cliente (str): Nombre del cliente.
        puntos_disponibles (int): Puntos disponibles del cliente.

    Retorna:
        tuple: Tupla con (total_final, puntos_ganados, puntos_usados).
    """
    # Lista donde se guardan las tuplas (nombre, cantidad, precio, tiempo, puntos)
    carrito = []

    # Bandera que mantiene abierto el submenú de compra hasta finalizar
    continuar = True

    while continuar:
        print("\n" + "=" * 40)
        print("       REALIZAR PEDIDO")
        print("=" * 40)
        print("1. Entradas")
        print("2. Platos Principales")
        print("3. Postres")
        print("4. Bebidas")
        print("5. Ver carrito")
        print("6. Finalizar pedido")
        print("=" * 40)

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            agregar_producto(carrito, "entradas")
        elif opcion == "2":
            agregar_producto(carrito, "principales")
        elif opcion == "3":
            agregar_producto(carrito, "postres")
        elif opcion == "4":
            agregar_producto(carrito, "bebidas")
        elif opcion == "5":
            mostrar_carrito(carrito)
        elif opcion == "6":
            if len(carrito) > 0:
                continuar = False
            else:
                print("\n❌ El carrito está vacío. Agrega productos antes de finalizar.")
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")

    # Calcula totales, descuentos, puntos y confirma la orden
    return procesar_pedido(carrito, nombre_cliente, puntos_disponibles)


def agregar_producto(carrito, categoria):
    """
    Agrega un producto al carrito desde una categoría específica del menú.

    Argumentos:
        carrito (list): Lista del carrito de compras a modificar.
        categoria (str): Clave de la categoría dentro del diccionario menu.
    """
    print(f"\n--- {categoria} ---")

    productos = menu[categoria]

    # Lista auxiliar para relacionar el número elegido por el usuario con su platillo
    lista_productos = []
    contador = 1

    for nombre in productos:
        info = productos[nombre]
        print(f"{contador}. {nombre} - ${info['precio']:.2f}")
        lista_productos += [(nombre, info)]
        contador += 1

    print("0. Volver")

    seleccion = input("\n¿Qué deseas agregar? (0 para volver): ").strip()

    # Valida que la selección contenga solo dígitos
    es_numero = True
    for char in seleccion:
        if char not in "0123456789":
            es_numero = False
            break

    if not es_numero or seleccion == "":
        print("❌ Por favor, ingresa un número válido.")
        return

    seleccion = int(seleccion)

    if seleccion == 0:
        return
    elif 1 <= seleccion <= len(lista_productos):
        # Obtiene el nombre y diccionario de datos del platillo elegido (índice base 0)
        nombre_producto, info_producto = lista_productos[seleccion - 1]

        cantidad_str = input("¿Cuántas unidades?: ").strip()

        # Valida que la cantidad sea un número entero positivo
        es_numero = True
        for char in cantidad_str:
            if char not in "0123456789":
                es_numero = False
                break

        if es_numero and cantidad_str != "" and int(cantidad_str) > 0:
            cantidad = int(cantidad_str)

            # Agrega el registro completo del producto al carrito
            carrito += [
                (
                    nombre_producto,
                    cantidad,
                    info_producto["precio"],
                    info_producto["tiempo"],
                    info_producto["puntos"],
                )
            ]

            print(f"\n✅ {cantidad}x {nombre_producto} agregado al carrito")
        else:
            print("❌ Cantidad inválida.")
    else:
        print("❌ Selección inválida.")


def mostrar_carrito(carrito):
    """
    Muestra el contenido actual del carrito, subtotales, total y tiempo estimado.

    Argumentos:
        carrito (list): Lista de tuplas (nombre, cantidad, precio_unitario, tiempo_preparacion, puntos).
    """
    if len(carrito) == 0:
        print("\n🛒 El carrito está vacío.")
        input("\nPresiona Enter para continuar...")
        return

    print("\n" + "=" * 50)
    print("         🛒 TU CARRITO")
    print("=" * 50)

    # Acumulador del importe total del carrito
    total = 0
    # Tiempo estimado: se toma el mayor tiempo de preparación entre los platillos
    tiempo_total = 0

    for item in carrito:
        nombre, cantidad, precio, tiempo, puntos = item

        # Importe de esta línea según cantidad y precio unitario
        subtotal = cantidad * precio
        total += subtotal
        tiempo_total = max(tiempo_total, tiempo)

        print(f"{cantidad}x {nombre}")
        print(f"   ${precio:.2f} c/u = ${subtotal:.2f}")

    print("-" * 50)
    print(f"TOTAL: ${total:.2f}")
    print(f"Tiempo estimado: {tiempo_total} minutos")
    print("=" * 50)

    input("\nPresiona Enter para continuar...")


def procesar_pedido(carrito, nombre_cliente, puntos_disponibles):
    """
    Calcula subtotales, descuentos, puntos, solicita confirmación y registra el pedido.

    Argumentos:
        carrito (list): Lista de productos agregados al pedido.
        nombre_cliente (str): Nombre del cliente.
        puntos_disponibles (int): Puntos disponibles del cliente.

    Retorna:
        tuple: Tupla con (total_final, puntos_ganados, puntos_usados).
    """
    # Variables acumuladoras para armar el resumen del pedido
    subtotal = 0
    tiempo_max = 0
    puntos_ganados = 0
    items_pedido = []

    print("\n" + "=" * 60)
    print("         📋 RESUMEN DEL PEDIDO")
    print("=" * 60)

    for item in carrito:
        nombre, cantidad, precio, tiempo, puntos = item

        subtotal_item = cantidad * precio
        subtotal += subtotal_item
        puntos_ganados += puntos * cantidad
        tiempo_max = max(tiempo_max, tiempo)

        # Repite el nombre según la cantidad para evaluar combos completos
        for _ in range(cantidad):
            items_pedido += [nombre]

        print(f"{cantidad}x {nombre}: ${subtotal_item:.2f}")

    print("-" * 60)
    print(f"Subtotal: ${subtotal:.2f}")

    # Verifica si los productos comprados activan algún combo del día
    combo_aplicado, descuento_combo = verificar_combo(items_pedido)
    descuento_monto = 0

    if combo_aplicado:
        descuento_monto = subtotal * (descuento_combo / 100)
        print(f"\n🎉 ¡Combo {combo_aplicado} aplicado!")
        print(f"   Descuento del {descuento_combo}%: -${descuento_monto:.2f}")

    # Monto parcial tras aplicar el descuento de combo
    total = subtotal - descuento_monto

    # Puntos canjeados en este pedido
    puntos_usados = 0

    if puntos_disponibles > 0:
        total, puntos_usados = calcular_precio_con_puntos(total, puntos_disponibles)
        if puntos_usados > 0:
            print(f"⭐ Puntos usados: {puntos_usados} (-${puntos_usados / 100:.2f})")

    # Simulación de número de pedido del día para promociones especiales
    pedidos_del_dia = 47

    # Cada décimo pedido terminado en 7 recibe 10% adicional de Happy Hour
    if pedidos_del_dia % 10 == 7:
        descuento_happy = total * 0.10
        print(f"\n🍻 ¡HAPPY HOUR! 10% descuento adicional: -${descuento_happy:.2f}")
        total -= descuento_happy

    # Promoción especial para el pedido número 50 del día
    if pedidos_del_dia == 50:
        print("\n🎊 ¡FELICIDADES! ¡Eres nuestro cliente #50 del día!")
        print("   ¡Tu pedido es GRATIS! 🎁")
        total = 0

    print("\n" + "=" * 60)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print(f"Tiempo de entrega: {tiempo_max} minutos")
    print(f"Puntos ganados: {puntos_ganados}")
    print("=" * 60)

    confirmar = ""
    while confirmar not in ["s", "n", "si", "no"]:
        confirmar = input("\n¿Confirmar pedido? (s/n): ").strip().lower()
        if confirmar not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' o 'n'")

    if confirmar in ["s", "si"]:
        print("\n✅ ¡Pedido confirmado!")
        print(f"📍 Tu pedido llegará en {tiempo_max} minutos.")

        print("\n⭐ ¿Cómo calificarías tu experiencia? (1-5 estrellas)")
        calificacion = input("Calificación: ").strip()

        if calificacion in ["1", "2", "3", "4", "5"]:
            # Multiplica el emoji de estrella por la calificación numérica ingresada
            estrellas = "⭐" * int(calificacion)
            print(f"\n¡Gracias por tu calificación de {estrellas}!")

        # Registra como cliente VIP si aún no figuraba en la base de datos
        if nombre_cliente.lower() not in clientes_vip:
            clientes_vip[nombre_cliente.lower()] = {"puntos": puntos_ganados, "pedidos": 1}
            print("\n¡Has sido registrado como cliente VIP, accede con tu nombre!")

        return total, puntos_ganados, puntos_usados
    else:
        print("\n❌ Pedido cancelado.")
        return 0, 0, 0


def menu_canjear_puntos(puntos_disponibles):
    """
    Muestra el menú para canjear puntos acumulados por productos del menú.

    Argumentos:
        puntos_disponibles (int): Puntos disponibles del cliente.

    Retorna:
        int: Cantidad de puntos utilizados en el canje.
    """
    if puntos_disponibles < 100:
        print("\n❌ Necesitas al menos 100 puntos para canjear.")
        print(f"   Actualmente tienes: {puntos_disponibles} puntos")
        input("\nPresiona Enter para continuar...")
        return 0

    print("\n" + "=" * 50)
    print("       ⭐ CANJEAR PUNTOS ⭐")
    print("=" * 50)
    print(f"Puntos disponibles: {puntos_disponibles}")
    print("\nProductos disponibles para canje:")
    print("-" * 50)

    # Guarda los productos que el cliente sí puede canjear con su saldo actual
    productos_canjeables = []

    for categoria in menu:
        productos = menu[categoria]
        for nombre in productos:
            info = productos[nombre]
            # El costo del canje equivale al triple de los puntos que otorga el producto
            puntos_necesarios = info["puntos"] * 3
            if puntos_necesarios <= puntos_disponibles:
                productos_canjeables += [(nombre, puntos_necesarios, categoria)]

    if len(productos_canjeables) == 0:
        print("No hay productos disponibles con tus puntos actuales.")
        input("\nPresiona Enter para continuar...")
        return 0

    for i, (nombre, puntos, categoria) in enumerate(productos_canjeables, 1):
        print(f"{i}. {nombre} ({categoria}) - {puntos} puntos")
    print("0. Volver")

    seleccion = input("\n¿Qué deseas canjear? ").strip()

    # Valida que la opción ingresada sea numérica
    es_numero = True
    for char in seleccion:
        if char not in "0123456789":
            es_numero = False
            break

    if not es_numero or seleccion == "":
        print("❌ Selección inválida.")
        return 0

    seleccion = int(seleccion)

    if seleccion == 0:
        return 0
    elif 1 <= seleccion <= len(productos_canjeables):
        nombre, puntos_canje, categoria = productos_canjeables[seleccion - 1]
        print(f"\n✅ Has canjeado: {nombre}")
        print(f"   Puntos utilizados: {puntos_canje}")
        print(f"   ¡Tu pedido llegará en {menu[categoria][nombre]['tiempo']} minutos!")
        input("\nPresiona Enter para continuar...")
        return puntos_canje
    else:
        print("❌ Selección inválida.")
        return 0


def main():
    """Función principal que coordina el flujo general del sistema de pedidos."""
    # Llama a la función de bienvenida (corregido: antes faltaban los paréntesis ())
    mostrar_bienvenidad()

    # Obtiene los datos iniciales del cliente al iniciar la sesión
    nombre_cliente, puntos_disponibles, es_vip = verificar_cliente()

    # Variables de control del ciclo principal y del saldo de puntos en la sesión
    ejecutando = True
    puntos_totales_ganados = 0
    puntos_totales_usados = 0

    while ejecutando:
        mostrar_menu_principal()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            mostrar_menu_completo()

        elif opcion == "2":
            # Calcula el saldo vigente antes de realizar el pedido
            saldo_actual = puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
            total, puntos_ganados, puntos_usados = realizar_pedido(nombre_cliente, saldo_actual)
            puntos_totales_ganados += puntos_ganados
            puntos_totales_usados += puntos_usados
            # Si confirmó un pedido, queda habilitado como cliente VIP en la sesión
            if total > 0 or puntos_ganados > 0:
                es_vip = True

        elif opcion == "3":
            # Rama agregada para que funcione la opción 3 del menú principal
            mostrar_ofertas()

        elif opcion == "4":
            if es_vip:
                puntos_actual = puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
                puntos_canjeados = menu_canjear_puntos(puntos_actual)
                puntos_totales_usados += puntos_canjeados
            else:
                # Corregido: antes faltaba print() en la primera línea de este aviso
                print("\n❌ Necesitas ser cliente VIP para canjear puntos.")
                print("   Realiza tu primer pedido para registrarte.")
                input("\nPresiona Enter para continuar...")

        elif opcion == "5":
            print("\n" + "=" * 50)
            print("¡Gracias por visitarnos! 👋")
            print(f"Hasta pronto, {nombre_cliente}!")

            if puntos_totales_ganados > 0 or puntos_totales_usados > 0:
                print("\nResumen de tu sesión:")
                print(f"  Puntos ganados: {puntos_totales_ganados}")
                print(f"  Puntos usados: {puntos_totales_usados}")
                saldo_final = puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
                print(f"  Saldo de puntos: {saldo_final}")

            print("=" * 50)
            # Sale del bucle principal sin importar si hubo o no movimiento de puntos
            ejecutando = False

        else:
            print("\n❌ Opción inválida. Por favor, elige entre 1 y 5.")

    print("\n¡Programa finalizado!")


# ===== EJECUTAR EL PROGRAMA =====
# Punto de entrada del script cuando se ejecuta directamente
main()