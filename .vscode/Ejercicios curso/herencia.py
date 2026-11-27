# Define la clase base Animal con atributos y comportamiento común
class Animal:
    """
    Clase padre que contiene la información compartida por los distintos
    tipos de animales.
    """

    def __init__(self, nombre, especie, edad, habitat):
        """
        Inicializa los atributos protegidos de un animal.

        Args:
            nombre (str): Nombre del animal.
            especie (str): Especie a la que pertenece el animal.
            edad (int): Edad del animal en años.
            habitat (Habitat): Instancia de Habitat asociada al animal.
        """
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        # Composición: almacena un objeto de tipo Habitat
        self._habitat = habitat

    def mostrar_info(self):
        """
        Muestra en consola los datos del animal y los atributos de su hábitat.

        Returns:
            None: Imprime la información en consola y no retorna un valor.
        """
        print(
            f"--> Nombre: {self._nombre}\n"
            f"Especie: {self._especie}\n"
            f"Edad: {self._edad}\n"
            f"Hábitat: {self._habitat._tipo_habitat}, {self._habitat._temperatura}"
        )


# Define la clase Habitat para representar el entorno de un animal
class Habitat:
    """Contiene la información del hábitat del animal."""

    def __init__(self, tipo_habitat, temperatura):
        """
        Inicializa los atributos del hábitat.

        Args:
            tipo_habitat (str): Tipo de entorno (por ejemplo, "Sabana" o "Bosque").
            temperatura (str): Condición térmica del hábitat (por ejemplo, "Cálido").
        """
        self._tipo_habitat = tipo_habitat
        self._temperatura = temperatura


# Define la subclase Mamifero que hereda de Animal
class Mamifero(Animal):
    """
    Representa un mamífero heredando los atributos de Animal y agregando
    el tipo de pelaje.
    """

    def __init__(self, nombre, especie, edad, habitat, tipo_pelaje):
        """
        Inicializa un mamífero invocando al constructor de Animal.

        Args:
            nombre (str): Nombre del mamífero.
            especie (str): Especie del mamífero.
            edad (int): Edad del mamífero en años.
            habitat (Habitat): Instancia de Habitat del mamífero.
            tipo_pelaje (str): Tipo de pelaje (por ejemplo, "Corto").
        """
        super().__init__(nombre, especie, edad, habitat)
        self._tipo_pelaje = tipo_pelaje

    def mostrar_info(self):
        """
        Muestra la información general del animal y añade el tipo de pelaje.

        Returns:
            None: Imprime la información en consola y no retorna un valor.
        """
        super().mostrar_info()
        print(f"Tipo de pelaje: {self._tipo_pelaje}")


# Define la subclase Ave que hereda de Animal
class Ave(Animal):
    """
    Representa un ave heredando los atributos de Animal y agregando
    el tipo de plumaje.
    """

    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        """
        Inicializa un ave invocando al constructor de Animal.

        Args:
            nombre (str): Nombre del ave.
            especie (str): Especie del ave.
            edad (int): Edad del ave en años.
            habitat (Habitat): Instancia de Habitat del ave.
            tipo_plumaje (str): Tipo de plumaje (por ejemplo, "Suave").
        """
        super().__init__(nombre, especie, edad, habitat)
        self._tipo_plumaje = tipo_plumaje

    def mostrar_info(self):
        """
        Muestra la información general del animal y añade el tipo de plumaje.

        Returns:
            None: Imprime la información en consola y no retorna un valor.
        """
        super().mostrar_info()
        print(f"Tipo de plumaje: {self._tipo_plumaje}")


# Define la clase Zoologico para administrar una colección de animales
class Zoologico:
    """Almacena y muestra la información de los animales del zoológico."""

    def __init__(self, nombre):
        """
        Inicializa el zoológico con su nombre y una lista vacía de animales.

        Args:
            nombre (str): Nombre del zoológico.
        """
        self._nombre = nombre
        self._animales = []

    def añadir_animal(self, animal):
        """
        Agrega un animal a la lista del zoológico mediante un bucle for.

        Args:
            animal (Animal): Instancia de Animal (o subclase) a agregar.

        Returns:
            None: Actualiza la lista interna de animales.
        """
        for nuevo in [animal]:
            self._animales += [nuevo]

    def mostrar_animales(self):
        """
        Muestra el nombre del zoológico y la información de cada animal registrado.

        Returns:
            None: Imprime el listado completo en consola.
        """
        print(f"Animales en {self._nombre}:")
        for animal in self._animales:
            animal.mostrar_info()


# Flujo principal de prueba
zoologico = Zoologico("ZooFantástico")
habitat1 = Habitat("Sabana", "Cálido")
habitat2 = Habitat("Bosque", "Templado")

mamifero = Mamifero("Simba", "León", 5, habitat1, "Corto")
ave = Ave("Piolín", "Canario", 2, habitat2, "Suave")

zoologico.añadir_animal(mamifero)
zoologico.añadir_animal(ave)
zoologico.mostrar_animales()