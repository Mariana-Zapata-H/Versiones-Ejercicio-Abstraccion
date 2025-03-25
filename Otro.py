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

    def obtener_paciente(self, identificador):
        """
        Permite buscar un paciente por cédula (exacta) o por nombre (parcial).
        Devuelve una lista de pacientes encontrados.
        """
        resultados = []

        # Si el identificador es un número, buscar por cédula
        if identificador.isdigit():
            cedula = int(identificador)
            if cedula in self.pacientes:
                resultados.append(self.pacientes[cedula])
        else:
            # Buscar por coincidencia en el nombre (inicio del nombre)
            for paciente in self.pacientes.values():
                if paciente.verNombre().lower().startswith(identificador.lower()):
                    resultados.append(paciente)

        return resultados

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
            if sistema.obtener_paciente(str(cedula)):
                print("Error: Ya existe un paciente con esta cédula.")
                continue

            genero = input("Ingrese el género del paciente: ").strip()
            servicio = input("Ingrese el servicio donde está alojado el paciente: ").strip()

            paciente = Paciente(nombre, cedula, genero, servicio)
            sistema.agregar_paciente(paciente)

        elif opcion == "2":
            identificador = input("Ingrese la cédula o el nombre del paciente a buscar: ").strip()
            pacientes_encontrados = sistema.obtener_paciente(identificador)

            if pacientes_encontrados:
                print("\nPacientes encontrados")
                for paciente in pacientes_encontrados:
                    print(f"\nNombre: {paciente.verNombre()}")
                    print(f"Cédula: {paciente.verCedula()}")
                    print(f"Género: {paciente.verGenero()}")
                    print(f"Servicio: {paciente.verServicio()}")
            else:
                print("No se encontró ningún paciente con ese criterio.")

        elif opcion == "3":
            sistema.ver_numero_pacientes()

        elif opcion == "4":
            print("Gracias por usar el sistema de pacientes. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, intente de nuevo.")


# Ejecutar el programa
main()
 