# Define el decorador que añade encabezado y cierre alrededor de la notificación
def formato_notificacion(func):
    """
    Envuelve un método de notificación para mostrar un encabezado y un pie
    indicando la plataforma del evento.

    Args:
        func (Callable): Método original a decorar.

    Returns:
        Callable: Función envolvente (wrapper) que ejecuta el formato y el método.
    """

    # Función interna que intercepta la llamada al método decorado
    def wrapper(self, plataforma):
        """
        Imprime el formato de inicio, ejecuta la notificación y muestra el cierre.

        Args:
            self (NotificadorRedSocial): Instancia del notificador.
            plataforma (str): Nombre de la red social de destino.

        Returns:
            None: Imprime el resultado formateado en consola.
        """
        print(f"***** NUEVO EVENTO en {plataforma} *****")
        # Ejecuta el método original notificar_evento
        func(self, plataforma)
        print(f"***** FIN DEL EVENTO en {plataforma} *****")

    return wrapper


# Define la clase encargada de notificar eventos según la red social
class NotificadorRedSocial:
    """Clase sistema de notificaciones para eventos en redes sociales."""

    # Constructor que almacena el evento por defecto o el recibido como argumento
    def __init__(self, evento="Lanzamiento de un nuevo libro"):
        """
        Almacena la descripción del evento.

        Args:
            evento (str): Descripción del evento a notificar.
        """
        self.evento = evento

    # Aplica el decorador formato_notificacion al método notificar_evento
    @formato_notificacion
    def notificar_evento(self, plataforma):
        """
        Muestra el mensaje del evento adaptado a la plataforma indicada.

        Args:
            plataforma (str): Red social ("Twitter", "Instagram", "Facebook", etc.).

        Returns:
            None: Imprime el mensaje correspondiente en consola.
        """
        if plataforma == "Twitter":
            print(f"Tweet: {self.evento}")
        elif plataforma == "Instagram":
            print(f"Instagram Story: {self.evento}")
        elif plataforma == "Facebook":
            print(f"Post en Facebook: {self.evento}")
        else:
            print("Plataforma no soportada")


# Simulación fuera de la clase
notificador = NotificadorRedSocial("Lanzamiento de un nuevo libro")
notificador.notificar_evento("Twitter")
notificador.notificar_evento("Instagram")
notificador.notificar_evento("Facebook")
notificador.notificar_evento("LinkedIn")