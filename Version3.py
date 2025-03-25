class Persona:
    tipo = "Mamifero"

    def __init__(self, nombre, cedula, genero):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero

    def verNombre(self):
        return self.__nombre

    def verCedula(self):
        return self.__cedula

    def verGenero(self):
        return self.__genero


class Paciente(Persona):
    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero)
        self.__servicio = servicio

    def verServicio(self):
        return self.__servicio


class SistemaPacientes:
    def __init__(self):
        self.pacientes = {}

    def agregar_paciente(self, paciente):
        """Verifica si la cédula ya existe antes de agregar el paciente."""
        cedula = paciente.verCedula()
        if cedula in self.pacientes:
            print("Error: Ya existe un paciente con esta cédula.")
        else:
            self.pacientes[cedula] = paciente
            print("Paciente agregado correctamente.")

    def obtener_paciente(self, cedula):
        """Devuelve el objeto Paciente asociado a la cédula o None si no existe."""
        return self.pacientes.get(cedula, None)

    def ver_numero_pacientes(self):
        print(f"Actualmente hay {len(self.pacientes)} pacientes registrados.")


def main():
    sistema = SistemaPacientes()

    while True:
        print("\nMenú del Sistema de Pacientes")
        print("1. Ingresar un paciente nuevo")
        print("2. Ver todos los datos de un paciente existente")
        print("3. Ver número de pacientes en el sistema")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ").strip()
            cedula = input("Ingrese la cédula del paciente (solo números): ").strip()

            if not cedula.isdigit():
                print("Error: La cédula debe contener solo números.")
                continue

            cedula = int(cedula)

            # Verificación de cédula duplicada antes de continuar
            if sistema.obtener_paciente(cedula):
                print("Error: Ya existe un paciente con esta cédula.")
                continue

            genero = input("Ingrese el género del paciente: ").strip()
            servicio = input("Ingrese el servicio donde está alojado el paciente: ").strip()

            paciente = Paciente(nombre, cedula, genero, servicio)
            sistema.agregar_paciente(paciente)

        elif opcion == "2":
            cedula = input("Ingrese la cédula del paciente a buscar: ").strip()

            if not cedula.isdigit():
                print("Error: La cédula debe contener solo números.")
                continue

            cedula = int(cedula)
            paciente = sistema.obtener_paciente(cedula)

            if paciente:
                print("\nDatos del Paciente")
                print(f"Nombre: {paciente.verNombre()}")
                print(f"Cédula: {paciente.verCedula()}")
                print(f"Género: {paciente.verGenero()}")
                print(f"Servicio: {paciente.verServicio()}")
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            sistema.ver_numero_pacientes()

        elif opcion == "4":
            print("Gracias por usar el sistema de pacientes.")
            break

        else:
            print("Opción no válida, intente de nuevo.")


# Ejecutar el programa
main()
