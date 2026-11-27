# Define la clase SimuladorPrestamo para calcular cuotas y pago total de una hipoteca
class SimuladorPrestamo:
    """
    Modela el proceso de calcular el pago total de un préstamo hipotecario,
    incluyendo el capital inicial y los intereses generados a lo largo del plazo.

    Atributos de instancia:
        detalles_prestamo (complex): Número complejo cuya parte real es la
            entrada y cuya parte imaginaria es el tipo de interés anual.
        años (int): Años del préstamo hipotecario.
        precio_vivienda (float): Precio de la vivienda.
        tasa_mensual (float): Tasa de interés mensual en formato decimal.
        numero_pagos (int): Número total de pagos mensuales.
        entrada (float): Monto de entrada proporcionado para la hipoteca.
        prestamo (float): Monto financiado (precio de la vivienda menos entrada).
        cuota_mensual (float): Cuota mensual calculada (inicialmente 0).
    """

    def __init__(self, detalles_prestamo, años=30, precio_vivienda=300000):
        """
        Inicializa los atributos del simulador de préstamo hipotecario.

        Args:
            detalles_prestamo (complex): Número complejo con entrada (parte real)
                y tipo de interés anual (parte imaginaria).
            años (int, optional): Años del préstamo hipotecario. Por defecto 30.
            precio_vivienda (float, optional): Precio de la vivienda. Por defecto 300000.
        """
        # Guarda los parámetros recibidos en la instancia
        self.detalles_prestamo = detalles_prestamo
        self.años = años
        self.precio_vivienda = precio_vivienda

        # Calcula la tasa mensual a partir de la parte imaginaria (anual / 12 / 100)
        self.tasa_mensual = (detalles_prestamo.imag / 12) / 100

        # Calcula el número total de pagos en meses
        self.numero_pagos = años * 12

        # Obtiene la entrada desde la parte real y calcula el monto del préstamo
        self.entrada = detalles_prestamo.real
        self.prestamo = precio_vivienda - self.entrada

        # Inicializa la cuota mensual en 0
        self.cuota_mensual = 0

    def calcular_pago_total(self):
        """
        Calcula la cuota mensual del préstamo hipotecario, actualiza el atributo
        `cuota_mensual` y devuelve el pago total a lo largo del plazo.

        Returns:
            float: Pago total acumulado (cuota mensual multiplicada por el
                número total de pagos).
        """
        # Si la tasa es 0 %, evita división entre cero dividiendo el préstamo en partes iguales
        if self.tasa_mensual == 0:
            self.cuota_mensual = self.prestamo / self.numero_pagos
        else:
            # Calcula la cuota mensual con la fórmula de amortización francesa
            factor = (1 + self.tasa_mensual) ** self.numero_pagos
            self.cuota_mensual = self.prestamo * (self.tasa_mensual * factor) / (factor - 1)

        # Calcula el pago total sumando todas las cuotas del préstamo
        pago_total = self.cuota_mensual * self.numero_pagos
        return pago_total

    def mostrar_resultados(self):
        """
        Imprime el resumen de la simulación hipotecaria con los datos del
        préstamo y la cuota mensual calculada.

        Returns:
            None: Imprime el resumen de la simulación en consola.
        """
        # Asegura que la cuota mensual esté calculada antes de imprimirla
        if self.cuota_mensual == 0 and self.prestamo > 0:
            self.calcular_pago_total()

        # Imprime el encabezado, los datos de la simulación, la cuota y el cierre
        print("----- Simulación Hipoteca -----")
        print(
            f"\nPara una vivienda de {self.precio_vivienda} euros, "
            f"aportando una entrada de {self.entrada} euros y "
            f"con una tasa de interés del {self.detalles_prestamo.imag}% anual "
            f"durante {self.años} años:"
        )
        print(f"\nCuota mensual a pagar: {self.cuota_mensual:.2f} euros")
        print("\n----- Fin de la Simulación -----")


def main():
    """
    Ejecuta una simulación de ejemplo de préstamo hipotecario.

    Returns:
        None: Instancia el simulador y muestra los resultados en consola.
    """
    # Instancia con entrada de 50000 y tasa anual de 2.5% usando un número complejo
    simulador = SimuladorPrestamo(50000 + 2.5j)
    simulador.calcular_pago_total()
    simulador.mostrar_resultados()


main()