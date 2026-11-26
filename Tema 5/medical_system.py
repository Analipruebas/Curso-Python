""" 
Sistema de Gestion de Citas Médicas
"""

# ============== Clase Paciente ================

class Paciente:
    """ 
    Representa un paciente del consultorio médico
    
    Atributos de clase:
        contador_pacientes (int): Lleva el conteo total de pacientes registrados.

    Atributos de instancia:
        id (str): Identificador único generado automáticamente (ej. 'PAC1').
        nombre (str): Nombre completo del paciente.
        edad (int): Edad del paciente en años.
        telefono (str): Número telefónico de contacto.
        email (str): Correo electrónico del paciente.
    """
    contador_pacientes = 0
class Paciente:
    """Representa un paciente dentro del consultorio médico."""

    # Variable de la clase: lleva el conteo total de pacientes creados
    contador_pacientes = 0

    def __init__(self, nombre, edad, telefono, email):
        """Crea un paciente nuevo y le asigna un ID automático.

        Args:
            nombre (str): Nombre completo del paciente.
            edad (int): Edad del paciente en años.
            telefono (str): Teléfono de contacto del paciente.
            email (str): Correo electrónico del paciente.
        """
        # Suma 1 al contador general cada vez que se crea un paciente
        Paciente.contador_pacientes += 1

        # Genera un ID único con formato de 4 dígitos (ej. PAC0001)
        self.id = f"PAC{Paciente.contador_pacientes:04d}"

        # Guarda los datos recibidos en los atributos del paciente
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email

        # Crea una lista vacía para ir guardando las citas del paciente
        self.historial_citas = []

    def agregar_cita(self, cita):
        """Agrega una cita nueva al historial del paciente.

        Args:
            cita: Información o registro de la cita médica a guardar.
        """
        # Añade la cita al final de la lista de citas del paciente
        #  .append() agrega un elemento nuevo al final de la lista (modifica la lista en su lugar)

        self.historial_citas.append(cita)

    def mostrar_info(self):
        """Muestra en consola los datos generales y el total de citas del paciente."""
        
        # Dibuja una línea superior de 50 signos '=' para separar visualmente la salida
        print (f"\n{'='*50}")
       
       # Imprime los datos principales y el número total de citas usando len()
        print(f"ID: {self.id} | Nombre: {self.nombre} | Edad: {self.edad} años")
        print(f"Teléfono: {self.telefono} | Email: {self.email}")
        print(f"Total de citas: {len(self.historial_citas)}")

        # Cierra el bloque visual con otra línea de 50 signos '='
        print (f"{'='*50}")

    def __str__(self):
        """Devuelve una representación en texto breve y legible del paciente.

        Returns:
            str: Cadena con el ID, nombre y edad del paciente.
        """
       # Construye y regresa un texto corto para mostrar al imprimir el objeto directamente
        return f"{self.id} - {self.nombre} ({self.edad} años)"


class Doctor:
    """
    Representa a un médico del consultorio con
    su información personal, especialidad y
    todas las citas que tiene programadas.

    Atributos de clase:
        contador_doctores (int): Lleva la cuenta del total de doctores registrados en el sistema.

    Atributos de instancia:
        id (str): Identificador único del doctor (ej: "DOC0001").
        nombre (str): Nombre completo del doctor.
        especialidad (str): Especialidad médica (ej: "Cardiología", "Pediatría").
        telefono (str): Número de teléfono de contacto.
        citas_programadas (list): Lista de objetos Cita asignados al doctor.
    """

    # Variable de clase: lleva el conteo total de doctores registrados
    contador_doctores = 0

    def __init__(self, nombre, especialidad, telefono):
        """
        Constructor de la clase Doctor.

        Args:
            nombre (str): Nombre del doctor.
            especialidad (str): Especialidad médica.
            telefono (str): Teléfono de contacto.
        """
        # Incrementa el contador general cada vez que se crea un doctor
        Doctor.contador_doctores += 1

        # Genera el ID consecutivo con formato DOC0001, DOC0002, etc.
        self.id = f"DOC{Doctor.contador_doctores:04d}"

        # Guarda los datos principales recibidos al crear el objeto
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono

        # Lista vacía para almacenar los objetos Cita asignados al doctor
        self.citas_programadas = []

    

 
    def agregar_cita(self, cita):
        """
        Agrega una cita a la lista de citas programadas.
        
        Args:
            cita (Cita): Objeto de tipo Cita a agregar
        """
        # Agrega el objeto cita al final de la lista de citas programadas
        self.citas_programadas.append(cita)


    def verificar_disponibilidad(self, fecha, hora):
        """
        Verifica si el doctor está disponible en una fecha y hora.
        
        Args:
            fecha (str): Fecha a verificar
            hora (str): Hora a verificar
        
        Returns:
            bool: True si está disponible, False si no
        """
        # Recorre todas las citas asignadas al doctor para detectar posibles choques
        for cita in self.citas_programadas:
            # Comprueba si coincide fecha y hora, y si la cita sigue activa (no cancelada)
            if cita.fecha == fecha and cita.hora == hora and cita.estado != "Cancelada":
                return False

        # Si ninguna cita activa coincide con la fecha y hora solicitadas, está disponible
        return True
    
        
    def mostrar_info(self):
        """Muestra toda la información del doctor y su cantidad de citas activas."""
        # Cuenta solo las citas con estado "Programada" (activas)
        citas_activas = len([
            c for c in self.citas_programadas if c.estado == "Programada" 
            #list comprehension (comprensión de lista) que arma una nueva lista temporal solo con las citas que cumplieron la condición.
        ])

        # Línea superior de separación con 50 signos '='
        print(f"\n{'=' * 50}")
        print(f"ID: {self.id} | Dr(a): {self.nombre}")
        print(f"Especialidad: {self.especialidad} | Teléfono: {self.telefono}")
        print(f"Citas programadas: {citas_activas}")
        # Línea inferior de separación con 50 signos '-'
        print(f"{'=' * 50}")
   

 
    def __str__(self):
        """
        Retorna la representación en string del doctor.
        
        Returns:
            str: Representación del doctor
        """
        # Construye la cadena descriptiva usada al hacer print(doctor) o str(doctor)
        return f"{self.id} - Dr(a). {self.nombre} - {self.especialidad}"



# ================== HERENCIA: ESPECIALIDADES ================

# ========================= SUBCLASES DE DOCTOR =========================


class Cardiologo(Doctor):
    """Representa a un médico especialista en cardiología."""

    def __init__(self, nombre, telefono):
        """Inicializa un cardiólogo con su tarifa de consulta fija.

        Args:
            nombre (str): Nombre completo del cardiólogo.
            telefono (str): Número de teléfono de contacto.
        """
        # Llama al constructor de Doctor asignando la especialidad fija
        super().__init__(nombre, "Cardiología", telefono)

        # Costo de consulta específico para cardiología
        self.costo_consulta = 800


class Pediatra(Doctor):
    """Representa a un médico especialista en pediatría."""

    def __init__(self, nombre, telefono):
        """Inicializa un pediatra con su tarifa de consulta fija.

        Args:
            nombre (str): Nombre completo del pediatra.
            telefono (str): Número de teléfono de contacto.
        """
        # Llama al constructor de Doctor asignando la especialidad fija
        super().__init__(nombre, "Pediatría", telefono)

        # Costo de consulta específico para pediatría
        self.costo_consulta = 600


class Dermatologo(Doctor):
    """Representa a un médico especialista en dermatología."""

    def __init__(self, nombre, telefono):
        """Inicializa un dermatólogo con su tarifa de consulta fija.

        Args:
            nombre (str): Nombre completo del dermatólogo.
            telefono (str): Número de teléfono de contacto.
        """
        # Llama al constructor de Doctor asignando la especialidad fija
        super().__init__(nombre, "Dermatología", telefono)

        # Costo de consulta específico para dermatología
        self.costo_consulta = 700



# ============================ CLASE CITA ============================


class Cita:
    """Representa una cita médica entre un paciente y un doctor."""

    # Variable de clase: lleva la cuenta total de citas creadas en el sistema
    contador_citas = 0

    def __init__(self, paciente, doctor, fecha, hora, motivo):
        """Inicializa una cita médica con estado programado y sin diagnóstico aún.

        Args:
            paciente (Paciente): Objeto paciente que solicita la cita.
            doctor (Doctor): Objeto doctor asignado a la consulta.
            fecha (str): Fecha de la cita (formato "DD/MM/YYYY").
            hora (str): Hora de la cita (formato "HH:MM").
            motivo (str): Motivo o síntoma principal de la consulta.
        """
        # Incrementa el contador general cada vez que se registra una cita
        Cita.contador_citas += 1

        # Genera el ID consecutivo con formato CIT0001, CIT0002, etc.
        self.id = f"CIT{Cita.contador_citas:04d}"

        # Guarda las referencias y datos principales de la cita
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

        # Estado inicial de la cita y diagnóstico vacío hasta que se atienda
        self.estado = "Programada"
        self.diagnostico = ""

    def cancelar(self):
        """Cambia el estado de la cita a 'Cancelada'."""
        # Marca la cita como cancelada para liberar el horario del doctor

        self.estado = "Cancelada"

    def completar(self,diagnostico):
        """
        Marca la cita como completada y guarda el diagnóstico médico.

        Args:
            diagnostico (str): Diagnóstico o indicaciones registradas tras la consulta.
        """
        # Actualiza el estado de la cita a completada
        self.estado = "Completada"

        # Guarda el diagnóstico proporcionado para la cita
        self.diagnostico = diagnostico

    
    def mostrar_info(self):
        """Muestra toda la información detallada de la cita médica."""
        # Imprime la línea superior de separación con 60 signos '='
        print(f"\n{'='*60}")
        # Muestra el ID de la cita y su estado actual
        print(f"ID Cita: {self.id} | Estado: {self.estado}")
        # Muestra el nombre y el ID del paciente
        print(f"Paciente: {self.paciente.nombre} | ID: {self.paciente.id}")        # Muestra el ID de la cita y su estado actual
        print(f"ID Cita: {self.id} | Estado: {self.estado}")
        # Muestra el nombre y la especialidad del doctor asignado
        print(f"Doctor: {self.doctor.nombre} - {self.doctor.especialidad}")
        # Muestra la fecha y la hora programadas
        print(f"Fecha: {self.fecha} | Hora: {self.hora}")
        # Muestra el motivo de la consulta
        print(f"Motivo: {self.motivo}")
        # Muestra el diagnóstico si ya fue registrado
        if self.diagnostico:
            print(f"Diagnostico: {self.diagnostico}")
        # Muestra el costo de consulta del doctor
        print(f"Costo: ${self.doctor.costo_consulta}")
        # Imprime la línea inferior de separación
        print(f"\n{'='*60}")

    


    def __str__(self):
        """
        Retorna la representación en string de la cita médica.

        Returns:
            str: Resumen de la cita con ID, paciente, doctor, fecha, hora y estado.
        """
        # Construye la cadena descriptiva para mostrar la cita en formato resumido
        return f"{self.id} - {self.paciente.nombre} con {self.doctor.nombre} ({self.fecha} {self.hora}) [{self.estado}]"

# ======================== Clase consultorio ==================
class Consultorio:
    """
    Gestiona todo el sistema de citas médicas, pacientes y doctores.

    Atributos de instancia:
        nombre (str): Nombre del consultorio médico.
        pacientes (list): Lista de objetos Paciente registrados.
        doctores (list): Lista de objetos Doctor registrados.
        citas (list): Lista de objetos Cita agendadas en el sistema.
    """

    def __init__(self, nombre):
        """
        Inicializa el consultorio con sus listas vacías de registros.

        Args:
            nombre (str): Nombre del consultorio médico.
        """
        # Guarda el nombre del consultorio
        self.nombre = nombre

        # Inicializa las listas vacías para almacenar pacientes, doctores y citas
        self.pacientes = []
        self.doctores = []
        self.citas = []

    def registrar_paciente(self, nombre, edad, telefono, email):
        """
        Crea un nuevo paciente y lo agrega al registro del consultorio.

        Args:
            nombre (str): Nombre completo del paciente.
            edad (int): Edad del paciente en años.
            telefono (str): Teléfono de contacto.
            email (str): Correo electrónico del paciente.
        """
        # Instancia un nuevo objeto Paciente con los datos proporcionados
        paciente = Paciente(nombre, edad, telefono, email)

        # Agrega el paciente a la lista general del consultorio
        self.pacientes.append(paciente)

        # Confirma el registro mostrando el ID asignado automáticamente
        print(f"\n✓ Paciente registrado exitosamente con ID: {paciente.id}")

        # Retorna el objeto paciente para reutilizarlo o validarlo fácilmente
        return paciente

    def registra_doctor(self, tipo, nombre, telefono):
        """
        Registra un doctor según su especialidad y retorna la instancia creada.

        Args:
            tipo (str): Código de especialidad ("1" Cardiología, "2" Pediatría,
                "3" Dermatología).
            nombre (str): Nombre completo del doctor.
            telefono (str): Teléfono de contacto del doctor.

        Returns:
            Doctor | None: Instancia del doctor registrado o None si el tipo no es válido.
        """
        # Selecciona la subclase de Doctor según el código de especialidad indicado
        if tipo == "1":
            doctor = Cardiologo(nombre, telefono)
        elif tipo == "2":
            doctor = Pediatra(nombre, telefono)
        elif tipo == "3":
            doctor = Dermatologo(nombre, telefono)
        else:
            # Informa y sale sin registrar si el tipo no corresponde a una opción válida
            print("✗ Tipo de especialidad no válido")
            return None

        # Agrega el doctor a la lista general del consultorio
        self.doctores.append(doctor)

        # Confirma el registro mostrando el ID asignado automáticamente
        print(f"\n✓ Doctor registrado exitosamente con ID: {doctor.id}")

        # Retorna el objeto doctor creado
        return doctor
    def agendar_cita(self, id_paciente, id_doctor, fecha, hora, motivo):
        """
        Valida datos y agenda una nueva cita médica entre un paciente y un doctor.

        Args:
            id_paciente (str): Identificador del paciente (por ejemplo, "PAC0001").
            id_doctor (str): Identificador del doctor (por ejemplo, "DOC0001").
            fecha (str): Fecha solicitada para la cita (formato "DD/MM/YYYY").
            hora (str): Hora solicitada para la cita (formato "HH:MM").
            motivo (str): Motivo de la consulta médica.

        Returns:
            Cita | None: Instancia de Cita creada si se agenda correctamente, o None
                si faltan registros o el doctor no tiene disponibilidad.
        """
        # Busca al paciente y al doctor por su ID en el consultorio
        paciente = self.buscar_paciente(id_paciente)
        doctor = self.buscar_doctor(id_doctor)

        # Verifica que ambos existan antes de continuar
        if not paciente or not doctor:
            print("✗ Paciente o Doctor no encontrado")
            return None

        # Comprueba si el doctor está libre en la fecha y hora indicadas
        if not doctor.verificar_disponibilidad(fecha, hora):
            print("✗ El doctor no esta disponible en ese horario")
            return None

        # Crea la cita y la vincula con el consultorio, el paciente y el doctor
        cita = Cita(paciente,doctor,fecha,hora, motivo)
        self.citas.append(cita)
        paciente.agregar_cita(cita)
        doctor.agregar_cita(cita)

        # Confirma que la cita quedó agendada y muestra su ID
        print(f"\n✓ Cita agendada exitosamente con ID: {cita.id}")

        # Retorna el objeto cita creado
        return cita
        

    def buscar_paciente(self, id_paciente):
        """
        Busca un paciente registrado en el consultorio por su identificador.

        Args:
            id_paciente (str): Identificador único del paciente (por ejemplo, "PAC0001").

        Returns:
            Paciente | None: El objeto Paciente encontrado o None si no existe.
        """
        # Recorre los pacientes registrados para encontrar una coincidencia de ID
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente

        # Retorna None si ningún paciente coincide con el ID buscado
        return None

    def buscar_doctor(self, id_doctor):
        """
        Busca un doctor registrado en el consultorio por su identificador.

        Args:
            id_doctor (str): Identificador único del doctor (por ejemplo, "DOC0001").

        Returns:
            Doctor | None: El objeto Doctor encontrado o None si no existe.
        """
        # Recorre los doctores registrados para encontrar una coincidencia de ID
        for doctor in self.doctores:
            if doctor.id == id_doctor:
                return doctor

        # Retorna None si ningún doctor coincide con el ID buscado
        return None

    def buscar_cita(self, id_cita):
        """
        Busca una cita registrada en el consultorio por su identificador.

        Args:
            id_cita (str): Identificador único de la cita (por ejemplo, "CIT0001").

        Returns:
            Cita | None: El objeto Cita encontrado o None si no existe.
        """
        # Recorre las citas registradas para encontrar una coincidencia de ID
        for cita in self.citas:
            if cita.id == id_cita:
                return cita

        # Retorna None si ninguna cita coincide con el ID buscado
        return None

    
    def mostrar_pacientes(self):
        """Muestra en consola la lista de todos los pacientes registrados."""
        # Verifica si existen pacientes antes de imprimir el listado
        if not self.pacientes:
            print("✗ No hay pacientes registrados")
            return

        # Imprime el encabezado con el total de pacientes y cada registro usando __str__
        print(f"\n{'='*60}\nLISTADO DE PACIENTES ({len(self.pacientes)} total)\n{'='*60}")
        for paciente in self.pacientes:
            print(paciente)

    def mostrar_doctores(self):
        """Muestra en consola la lista de todos los doctores registrados."""
        # Verifica si existen doctores antes de imprimir el listado
        if not self.doctores:
           print("✗ No hay doctores registrados")
           return

        # Imprime el encabezado con el total de doctores y cada registro usando __str__
        print(f"\n{'='*60}\nLISTADO DE DOCTORES ({len(self.doctores)} total)\n{'='*60}")
        for doctor in self.doctores:
            print(doctor)

    def mostrar_citas(self, filtro="todas"):
        """
        Muestra las citas registradas en el consultorio según un filtro de estado.

        Args:
            filtro (str, optional): Criterio de filtrado de citas (por ejemplo,
                "todas", "Programada", "Completada" o "Cancelada").
        """
        # Verifica si existen citas registradas antes de aplicar el filtro
        if not self.citas:

           print("✗ No hay citas registradas")
           return
        # Filtra las citas programadas si se solicita ese criterio
        if filtro == "programadas":
            cita_filtradas = [c for c in self.citas if c.estado == "Programada"]
        # Filtra las citas completadas si se solicita ese criterio
        if filtro == "completadas":
                     cita_filtradas = [c for c in self.citas if c.estado == "Completada"]  
        # Filtra las citas canceladas o usa todas las citas por defecto
        if filtro == "canceladas":
                    cita_filtradas = [c for c in self.citas if c.estado == "Cancelada"]
        else:
            cita_filtradas = self.citas

        # Imprime el encabezado con el filtro en mayúsculas, el conteo y cada cita
        print(f"\n{'='*60}\nCITAS - {filtro.upper()} ({len(cita_filtradas)} total)\n{'='*60}")
        for cita in cita_filtradas:
            print(cita)

def mostrar_menu():
    """Muestra en consola el menú principal de opciones del sistema de citas."""
    # Imprime el encabezado principal centrado dentro de un marco de 60 caracteres
    print("\n" + "="*60)
    print(f"{'🏥 SISTEMA DE GESTIÓN DE CITAS MÉDICAS':^60}")
    print("="*60)

    # Muestra las opciones disponibles para registrar, consultar y gestionar citas
    print("1.  Registrar nuevo paciente")
    print("2.  Registrar nuevo doctor")
    print("3.  Agendar cita")
    print("4.  Ver información de paciente")
    print("5.  Ver información de doctor")
    print("6.  Ver información de cita")
    print("7.  Cancelar cita")
    print("8.  Completar cita (agregar diagnóstico)")
    print("9.  Listar todos los pacientes")
    print("10. Listar todos los doctores")
    print("11. Listar todas las citas")
    print("12. Listar citas programadas")
    print("0.  Salir")
    print("="*60)

def main():
    """Ejecuta el bucle principal interactivo del sistema de gestión de citas."""
    # Crea la instancia principal del consultorio
    consultorio = Consultorio("Centro Medico Salud Total")

    # Registra doctores iniciales de ejemplo para probar el sistema
    consultorio.registra_doctor("1","Ana García", "555-0101")
    consultorio.registra_doctor("2","Carlos Rodríguez", "555-0102")
    consultorio.registra_doctor("3","María López","555-0103")

    # Mantiene el menú activo hasta que el usuario elija salir con "0"
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            # Solicita datos y registra un nuevo paciente
            print("\n--- REGISTRAR NUEVO PACIENTE---")
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            telefono = input("Teléfono: ")
            email = input("Email: ")
            consultorio.registrar_paciente(nombre, edad, telefono, email)

        elif opcion == "2":
            # Solicita especialidad y datos para registrar un nuevo doctor
            print("\n --- REGISTRAR NUEVO DOCTOR ---")
            print("Especialidades: 1.Cardiologpia 2.Pediatria 3. Dermatología")
            tipo  = input("Seleccione especialidad: ")
            nombre = input("Nombre completo: ")
            telefono = input("Teléfono: ")
            consultorio.registra_doctor(tipo, nombre, telefono)

        elif opcion == "3":
            # Muestra listados de apoyo y agenda una nueva cita
            # .upper() convierte el texto ingresado a mayúsculas para coincidir con el formato del ID (ej. "pac0001" -> "PAC0001")
            print("\n ---AGENDAR CITA---")
            consultorio.mostrar_pacientes()
            id_paciente = input("\n ID del paciente: ").upper()
            consultorio.mostrar_doctores()
            id_doctor= input("\n ID del doctor: ").upper()
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input ("Hora (HH:00): ")
            motivo = input("Motivo de la consulta: ")
            consultorio.agendar_cita(id_paciente, id_doctor, fecha,hora, motivo)

        elif opcion == "4":
            # Busca un paciente por ID y muestra su información si existe
            # .upper() convierte las letras del ID ingresado a mayúsculas (ej. "pac0001" -> "PAC0001")
            id_paciente = input("\n ID del paciente: ").upper()
            paciente = consultorio.buscar_paciente(id_paciente)
            if paciente:
             paciente.mostrar_info()
            else:
                print("✗ Paciente no encontrado")

        elif opcion == "5":
            # Busca un doctor por ID y muestra su información si existe
            # .upper() convierte las letras del ID ingresado a mayúsculas (ej. "doc0001" -> "DOC0001")
            id_doctor = input("\n ID del doctor: ").upper()
            doctor = consultorio.buscar_doctor(id_doctor)
            if doctor:
                doctor.mostrar_info()
            else:
                print("✗ Doctor no encontrado")
        elif opcion == "6":
            # Busca y muestra la información detallada de una cita
            # .upper() convierte las letras del ID ingresado a mayúsculas (ej. "cit0001" -> "CIT0001")
            id_cita = input("\nID de la cita: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                cita.mostrar_info()
            else:
                print("✗ Cita no encontrada")
        elif opcion == "7":
            # Localiza una cita por ID y cambia su estado a cancelada
            # .upper() convierte las letras del ID ingresado a mayúsculas (ej. "cit0001" -> "CIT0001")
            id_cita = input("\nID de la cita a cancelar: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                cita.cancelar()
                print(f"\n✓ Cita cancelada exitosamente")
            else:
                print("✗ Cita no encontrada")
        elif opcion == "8":
            # Localiza una cita por ID, registra diagnóstico y la marca como completada
            # .upper() convierte las letras del ID ingresado a mayúsculas (ej. "cit0001" -> "CIT0001")
            id_cita = input("\nID de la cita: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                diagnostico = input("Diagnostico: ")
                cita.completar(diagnostico)
                print(f"\n✓ Cita cancelada exitosamente")
            else:
                print("✗ Cita no encontrada")

        elif opcion =="9":
            # Muestra todos los pacientes registrados
            consultorio.mostrar_pacientes()
        elif opcion =="10":
            # Muestra todos los doctores registrados
            consultorio.mostrar_doctores()
        elif opcion =="11":
            # Muestra todas las citas sin filtrar por estado
            consultorio.mostrar_citas("todas")
        elif opcion =="12":
            # Muestra únicamente las citas con estado programado
            consultorio.mostrar_citas("programadas")
        elif opcion == "0":
            # Cierra el ciclo principal y termina la ejecución del programa
             print("\n¡Gracias por usar el Sistema de Gestión de Citas Médicas!")
             print("¡Hasta pronto! 👋\n")
             break
                    
        else:
            # Informa cuando la opción ingresada no corresponde al menú
            print("\n✗ Opción no válida. Por favor, intente de nuevo.")
                    
        # Pausa breve para leer la salida antes de redibujar el menú
        input("\nPresione ENTER para continuar...")

    # ===== EJECUTAR EL PROGRAMA =====
# Llamar a la función principal
main()



        



        






    




      




