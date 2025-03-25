class Persona:
    tipo = "Mamifero"
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

    # Setters
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    def asignarCedula(self, cedula):
        self.__cedula = cedula
    def asignarGenero(self, genero):
        self.__genero = genero

    # Getters
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero

class Paciente(Persona):
    def __init__(self):
        super().__init__()
        self.__servicio = ""
    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio

class SistemaPacientes:
    def __init__(self):
        self.pacientes = {}

    def ingresar_paciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        cedula = input("Ingrese la cédula del paciente: ")
        genero = input("Ingrese el género del paciente: ")
        servicio = input("Ingrese el servicio donde está alojado el paciente: ")

        if cedula in self.pacientes:
            print("Error: Ya existe un paciente con esa cédula.")
            return

        paciente = Paciente()
        paciente.asignarNombre(nombre)
        paciente.asignarCedula(cedula)
        paciente.asignarGenero(genero)
        paciente.asignarServicio(servicio)

        self.pacientes[cedula] = paciente
        print("Paciente agregado correctamente.")

    def ver_datos_paciente(self):
        cedula = input("Ingrese la cédula del paciente a buscar: ")
        if cedula in self.pacientes:
            paciente = self.pacientes[cedula]
            print("\n--- Datos del Paciente ---")
            print(f"Nombre: {paciente.verNombre()}")
            print(f"Cédula: {paciente.verCedula()}")
            print(f"Género: {paciente.verGenero()}")
            print(f"Servicio: {paciente.verServicio()}")
        else:
            print("Paciente no encontrado.")

    def ver_numero_pacientes(self):
        print(f"Actualmente hay {len(self.pacientes)} pacientes registrados.") 

    def ejecutar(self):
        while True:
            print("\nMenú del Sistema de Pacientes")
            print("1. Ingresar un paciente nuevo")
            print("2. Ver todos los datos de un paciente existente")
            print("3. Ver número de pacientes en el sistema")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ingresar_paciente()
            elif opcion == "2":
                self.ver_datos_paciente()
            elif opcion == "3":
                self.ver_numero_pacientes()
            elif opcion == "4":
                print("Saliendo del sistema...") 
                break
            else:
                print("Opción no válida, intente de nuevo.")

sistema = SistemaPacientes()
sistema.ejecutar()
