# Define la clase GeneradorNombresUsuario para construir y validar nombres de usuario
class GeneradorNombresUsuario:
    """
    Genera nombres de usuario únicos siguiendo un formato específico.

    Atributos de instancia:
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        año_nacimiento (int | str): Año de nacimiento del usuario.
    """

    def __init__(self, nombre, apellido, año_nacimiento):
        """
        Inicializa los datos base para generar el nombre de usuario.

        Args:
            nombre (str): Nombre del usuario.
            apellido (str): Apellido del usuario.
            año_nacimiento (int | str): Año de nacimiento del usuario.
        """
        # Guarda los datos recibidos como atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.año_nacimiento = año_nacimiento

    def generar_nombre_usuario(self):
        """
        Construye el nombre de usuario con el nombre en minúsculas, el apellido
        en mayúsculas, sin espacios entre ellos y el año al final.

        Returns:
            str: Nombre de usuario generado.
        """
        # Convierte el nombre a minúsculas y el apellido a mayúsculas
        nombre_minusculas = self.nombre.lower()
        apellido_mayusculas = self.apellido.upper()

        # Une nombre y apellido sin espacios y añade el año al final
        nombre_completo = "".join([nombre_minusculas, apellido_mayusculas])
        usuario_generado = f"{nombre_completo}{self.año_nacimiento}"
        return usuario_generado

    def validar_nombre_usuario(self, nombre_usuario=None):
        """
        Verifica que el nombre de usuario tenga al menos 8 caracteres y termine
        con 4 números.

        Args:
            nombre_usuario (str, optional): Nombre de usuario a validar. Si no se
                pasa, se genera automáticamente desde los datos de la instancia.

        Returns:
            bool: True si cumple ambos criterios, False en caso contrario.
        """
        # Si no se recibe un nombre explícito, genera uno con los datos actuales
        if nombre_usuario is None:
            nombre_usuario = self.generar_nombre_usuario()

        # Revisa longitud mínima de 8 caracteres y que los últimos 4 sean dígitos
        longitud_valida = len(nombre_usuario) >= 8
        ultimos_cuatro = nombre_usuario[-4:]
        cuatro_numeros_al_final = len(ultimos_cuatro) == 4 and ultimos_cuatro.isdigit()

        return longitud_valida and cuatro_numeros_al_final

    def mostrar_nombre_usuario(self):
        """
        Imprime el nombre de usuario generado si pasa la validación; de lo
        contrario, imprime un mensaje indicando que no cumple los criterios.

        Returns:
            None: Imprime el resultado en consola y no retorna un valor.
        """
        # Genera el nombre y comprueba si cumple con las reglas de validación
        usuario = self.generar_nombre_usuario()
        if self.validar_nombre_usuario(usuario):
            print(f"Nombre de usuario generado: {usuario}")
        else:
            print("El nombre de usuario no cumple con los criterios de validación.")


def main():
    """
    Ejecuta una prueba de generación y validación de nombre de usuario.

    Returns:
        None: Instancia el generador y muestra el resultado en consola.
    """
    # Crea el objeto y llama a generar_nombre_usuario y mostrar_nombre_usuario
    generador = GeneradorNombresUsuario("santiago", "hernandez", 1994)
    generador.generar_nombre_usuario()
    generador.mostrar_nombre_usuario()


main()