class Persona():
    tipo= "Mamifero"
    def __init__(self ):
        self.__nombre =""
        self.__cedula =0
        self.__genero = ""
#Propiedades
    # Setters
    def asignarNombre(self,h):
        self.__nombre = h
    def asignarCedula(self,h):
        self.__cedula = h
    def asignarGenero(self,h):
        self.__genero = h

    # getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    #deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero
        
# Métodos adicionales segun la abstracción hecha 
    def caminar(self):        
        print(input("ingrese direccion: "))
    def comer(self):
        print(input("Ingrese la comida que desea: "))

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self, servicio):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno

    def verturno(self, turno):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        # Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self, rango):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = ''
    def verEspecialidad(self, especialidad):
        return self.__especialidad
    
listaPaciente = []
listaEnfermera = []
listaMedico = []

while True:
    menu = input('''Ingrese variable que desea ingresar:
(1) Paciente
(2) Enfermera
(3) Médico
(4) Salir
''')

    if menu == '1':
        paciente = Paciente()
        paciente.asignarNombre(input('Ingresa el nombre del paciente: '))
        paciente.asignarCedula(input('Ingresa la cédula del paciente: '))
        paciente.asignarGenero(input('Ingresa el género del paciente: '))
        paciente.asignarServicio(input('Ingresa el servicio del paciente: '))
        listaPaciente.append(paciente)
        for i in range(len(listaPaciente)):
            print(f'Paciente #{i+1}')
            print('Nombre:', listaPaciente[i].verNombre())
            print('Identificación:', listaPaciente[i].verCedula())
            print('Género:', listaPaciente[i].verGenero())
            print('Servicio:', listaPaciente[i].verServicio(), '\n')

    if menu == '2':
        enfermera = Enfermera()
        enfermera.asignarNombre(input('Ingresa el nombre del enfermero: '))
        enfermera.asignarCedula(input('Ingresa la cédula del enfermero: '))
        enfermera.asignarGenero(input('Ingresa el género del enfermero: '))
        enfermera.asignarRango(input('Ingresa el rango del enfermero: '))
        listaEnfermera.append(enfermera)
        for i in range(len(listaEnfermera)):
            print(f'Enfermera #{i+1}')
            print('Nombre:', listaEnfermera[i].verNombre())
            print('Identificación:', listaEnfermera[i].verCedula())
            print('Género:', listaEnfermera[i].verGenero())
            print('Rango:', listaEnfermera[i].verRango(), '\n')

    if menu == '3':
        medico = Medico()
        medico.asignarNombre(input('Ingresa el nombre del médico: '))
        medico.asignarCedula(input('Ingresa la cédula del médico: '))
        medico.asignarGenero(input('Ingresa el género del médico: '))
        medico.asignarTurno(input('Ingresa el turno del médico: '))
        medico.asignarEspecialidad(input('Ingresa la especialidad del médico: '))
        listaMedico.append(medico)
        for i in range(len(listaMedico)):
            print(f'Médico #{i+1}')
            print('Npmbre:', listaMedico[i].verNombre())
            print('Identificación:', listaMedico[i].verCedula())
            print('Género:', listaMedico[i].verGenero())
            print('Turno:', listaMedico[i].verTurno())
            print('Especialidad:', listaMedico[i].verEspecialidad(), '\n')

    elif menu == '4':
        break