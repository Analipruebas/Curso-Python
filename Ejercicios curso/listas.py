# Define la clase SistemaCalificaciones para gestionar notas de un curso
class SistemaCalificaciones:
    """
    Administra las calificaciones de los estudiantes en un curso.

    Atributos de instancia:
        calificaciones (list): Almacena las calificaciones de los estudiantes.
    """

    def __init__(self):
        """
        Inicializa el sistema con una lista vacía de calificaciones.

        Args:
            None.
        """
        # Lista que guardará las calificaciones registradas en el curso
        self.calificaciones = []

    def añadir_calificacion(self, calificacion):
        """
        Añade una nueva calificación a la lista de calificaciones.

        Args:
            calificacion (int | float): Calificación del estudiante a registrar.

        Returns:
            None: Agrega el elemento a la lista interna.
        """
        # Agrega la calificación al final de la lista de calificaciones
        self.calificaciones.append(calificacion)

    def mostrar_calificaciones(self):
        """
        Imprime todas las calificaciones almacenadas mediante un bucle for.

        Returns:
            None: Imprime cada calificación en consola.
        """
        # Recorre cada calificación registrada y la imprime en pantalla
        for calificacion in self.calificaciones:
            print(calificacion)

    def calificacion_promedio(self):
        """
        Calcula y retorna el promedio de las calificaciones registradas.

        Returns:
            float | int: Promedio de las calificaciones, o 0 si la lista está vacía.
        """
        # Verifica que la lista no esté vacía para evitar división entre cero
        if self.calificaciones:
            promedio = sum(self.calificaciones) / len(self.calificaciones)
            return promedio
        return 0

    def ordenar_calificaciones(self):
        """
        Ordena las calificaciones almacenadas de menor a mayor.

        Returns:
            None: Modifica la lista interna en su lugar.
        """
        # Ordena la lista original de forma ascendente
        self.calificaciones.sort()


def main():
    """
    Ejecuta el flujo de prueba de SistemaCalificaciones.

    Returns:
        None: Crea la instancia, registra notas y muestra los resultados.
    """
    # Crea el objeto y agrega las calificaciones indicadas
    sistema = SistemaCalificaciones()
    for nota in [8, 9.5, 7, 10]:
        sistema.añadir_calificacion(nota)

    # Muestra calificaciones originales
    print("Calificaciones originales:")
    sistema.mostrar_calificaciones()

    # Calcula e imprime el promedio
    print(f"Promedio: {sistema.calificacion_promedio()}")

    # Ordena las calificaciones y las vuelve a mostrar
    sistema.ordenar_calificaciones()
    print("Calificaciones ordenadas:")
    sistema.mostrar_calificaciones()


main()