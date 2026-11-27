# Define la clase Libro para representar un ejemplar dentro de una biblioteca
class Libro:
    """Contendrá los detalles básicos de un libro en una biblioteca."""

    # Método constructor que inicializa los atributos de cada instancia de Libro
    def __init__(self, titulo, autor, isbn):
        """
        Inicializa los atributos del libro y lo marca como disponible.

        Args:
            titulo (str): Título del libro.
            autor (str): Nombre del autor del libro.
            isbn (str): Código ISBN identificador del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        # Todo libro nuevo inicia disponible para préstamo
        self.disponible = True

    # Método para mostrar en consola los datos actuales del libro
    def informacion(self):
        """
        Muestra por pantalla los detalles del libro.

        Returns:
            None: Imprime la información en consola y no retorna un valor.
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponible: {self.disponible}")

    # Método para marcar el libro como prestado si está disponible
    def prestar_libro(self):
        """
        Cambia disponible a False cuando se presta el libro.

        Returns:
            None: Actualiza el estado del libro y muestra un mensaje en consola.
        """
        # Si ya está prestado (disponible es False), informa y sale sin modificar nada
        if not self.disponible:
            print("Este libro ya está prestado")
            return

        # Cambia el estado a no disponible y muestra los detalles actualizados
        self.disponible = False
        print(f'El libro "{self.titulo}" ha sido prestado.')
        print(f"--> Información del libro: {self.titulo}")
        self.informacion()

    # Método para marcar el libro como devuelto si actualmente estaba prestado
    def devolver_libro(self):
        """
        Cambia disponible a True cuando se devuelve el libro.

        Returns:
            None: Actualiza el estado del libro y muestra un mensaje en consola.
        """
        # Si ya está disponible (disponible es True), informa que ya está en la biblioteca
        if self.disponible:
            print("Este libro ya está en la biblioteca")
            return

        # Restaura la disponibilidad a True y muestra los detalles actualizados
        self.disponible = True
        print(f'El libro "{self.titulo}" ha sido devuelto a la biblioteca.')
        print(f"--> Información del libro: {self.titulo}")
        self.informacion()


# Instancias de prueba fuera de la clase
libro_hp = Libro(
    "Harry Potter y la piedra filosofal", "J.K. Rowling", "978-0747532743"
)
libro_1984 = Libro("1984", "George Orwell", "978-0451524935")

# Pruebas de préstamo y devolución
libro_hp.prestar_libro()
libro_hp.devolver_libro()
libro_1984.prestar_libro()
libro_1984.prestar_libro()