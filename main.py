
import time
import random

# Inicio de la simulación para medir el tiempo
inicio = time.time()


precio_matricula = 14
total_atendidos = []
tiempo = 0

# Inicializar materias
materias_habilitadas = ['Fisica', 'Programacion', 'Redes', 'Base de datos', 'Inteligencia Artificial',
                        'Calculo 1', 'Calculo 2', 'Ingles 1', 'Ingles 2', 'Algebra 1', 'Algebra 2', 'Telefonia IP', 'Programacion WEB']


class AgenteEstudiante(object):
    def __init__(self, nombre, carrera, matricula, dinero, materias):
        self.nombre = nombre
        self.carrera = carrera
        self.materias = materias
        self.matricula = matricula
        self.dinero = dinero
        self.boleta = ''
        self.pagado = False

    def solicitar_inscripcion(self):
        global tiempo
        if not self.pagado:
            return
        materias = self.materias
        # Lógica para solicitar la inscripción del estudiante en las materias
        time.sleep(random.randint(1, 2))
        print('Agente Estudiante: '+self.nombre +
              ' esta solicitando inscribirse a las materias.....')
        time.sleep(random.randint(1, 2))
        print(materias)
        tiempo += 5
        print("tiempo transcurrido: ",tiempo)

    def pagar(self):
        global tiempo
        # Lógica para realizar el pago de la matrícula por parte del estudiante
        time.sleep(random.randint(1, 2))
        print('Agente Estudiante: Realizando pago de matrícula.....')
        if (estudiante.dinero < precio_matricula):
            time.sleep(random.randint(1, 2))
            print('El monto pagado es menor al precio de la matrícula......')
            tiempo += 2
            print("tiempo transcurrido: ",tiempo)
            return
        if (estudiante.dinero == precio_matricula):
            self.pagado = True
            total_atendidos.append(estudiante)
            time.sleep(random.randint(1, 2))
            print('Agente Estudiante: Pagando matricula.....')
            tiempo += 2
            print("tiempo transcurrido: ",tiempo)

        elif (estudiante.dinero > precio_matricula):
            self.pagado = True
            total_atendidos.append(estudiante)
            time.sleep(random.randint(1, 2))
            print('Agente Estudiante: Pagando matricula.....')
            tiempo += 2
            print("tiempo transcurrido: ",tiempo)
        

    def obtener_boleta(self):
        global tiempo
        # Lógica para obtener la boleta de pago del estudiante
        time.sleep(random.randint(1, 2))
        print('Agente Estudiante: Obteniendo boleta de pago del estudiante ' + self.nombre)
        print('Boleta: '+self.boleta)
        tiempo += 2
        print("tiempo transcurrido: ",tiempo)


class AgenteCajero(object):
    def __init__(self):

        self.boleta = 0.0

    def cobrar_matricula(self, estudiante):
        global tiempo
        # Verificar que el estudiante haya realizado el pago
        if not estudiante.pagado:
            time.sleep(random.randint(1, 2))
            print(
                'Agente Cajero: El estudiante no ha realizado el pago de la matrícula.....')
            return

        # Lógica para cobrar la matrícula y obtener la boleta del estudiante
        time.sleep(random.randint(1, 2))
        print('Agente Cajero: Recibiendo pago de matrícula del estudiante.....')
        estudiante.boleta = random.randint(10000, 99999)
        self.boleta = estudiante.boleta
        cambio = estudiante.dinero - precio_matricula
        time.sleep(random.randint(1, 2))
        print('Agente Cajero:Pago con billete de: '+str(estudiante.dinero) +
              ' su cambio es: ' + str(cambio))

        time.sleep(random.randint(1, 2))
        print('Agente Cajero: Pago de matrícula recibido. Generando boleta de pago.....')
        print('La boleta de pago es: '+str(self.boleta))
        tiempo += 8
        print("tiempo transcurrido: ",tiempo)
        return self.boleta


class AgenteResponsable(object):
    def __init__(self):

        self.materias = []

    def habilitar_materias(self, materias):
        global tiempo
        # Lógica para habilitar las materias seleccionadas

        time.sleep(random.randint(1, 2))
        print('Agente Responsable: Habilitando materias......')
        self.materias
        # Imprimir materias
        time.sleep(random.randint(1, 2))
        print(materias)
        time.sleep(random.randint(1, 2))
        print('Agente Responsable: Materias habilitadas con éxito.....')
        tiempo += 5
        print("tiempo transcurrido: ",tiempo)

class AgenteDirector(object):
    def __init__(self):

        self.materias_inscritas_totales = []

    def inscribir_estudiante(self, estudiante):
        global tiempo
       # Verificar que el estudiante haya realizado el pago
        if not estudiante.pagado:
            time.sleep(random.randint(1, 2))
            print(
                'Agente Director: El estudiante no ha realizado el pago de la matrícula por lo tanto no puede inscribirse....')
            return
        materias = estudiante.materias
        # Lógica para inscribir al estudiante en las materias seleccionadas

        if set(materias).issubset(set(materias_habilitadas)):

            # Lógica para inscribir al estudiante en las materias seleccionadas
            time.sleep(random.randint(1, 2))
            print('Agente Director: Inscribiendo al estudiante ' +
                  estudiante.nombre + ' en las materias seleccionadas.....')
            self.materias_inscritas_totales.extend(materias)
            time.sleep(random.randint(1, 2))
            print('Agente Director: Inscripción del estudiante ' +
                  estudiante.nombre + ' completada con éxito en las materias:')
            time.sleep(random.randint(1, 2))
            print(materias)
        else:
            time.sleep(random.randint(1, 2))
            print(
                'Agente Director: Las materias seleccionadas no se encuentran habilitadas.....')
        tiempo += 10
        print("tiempo transcurrido: ",tiempo)

# Interaccion de los agentes


# Crear un responsable
responsable = AgenteResponsable()

# Crear un cajero
cajero = AgenteCajero()

# Crear un director
director = AgenteDirector()

# Habilitar materias
responsable.habilitar_materias(materias_habilitadas)

# Crear estudiantes
estudiante1 = AgenteEstudiante(
    'Juan', 'Ingeniería de Sistemas', 12345, 20, ['Fisica', 'Programacion', 'Calculo 1'])

estudiante2 = AgenteEstudiante(
    'Luis', 'Ingeniería de Sistemas', 45678, 12, ['Algebra 1', 'Programacion WEB', 'Base de datos'])

estudiante3 = AgenteEstudiante(
    'Raul', 'Ingeniería de Sistemas', 98765, 60, ['Inteligencia Artificial', 'Telefonia IP', 'Programacion WEB'])

estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in estudiantes:

    # El estudiante paga
    estudiante.pagar()

# El cajero cobra
    cajero.cobrar_matricula(estudiante)

# El estudiante solicita inscribirse en las materias
    estudiante.solicitar_inscripcion()

# Inscribir al estudiante en el semestre
    director.inscribir_estudiante(estudiante)
    time.sleep(random.randint(1, 2))
    print('-------------------------------------------------------------------------')


# Total recaudado
print('Total recaudado: ' + str(total_atendidos.__len__()*precio_matricula))

# Fin del tiempo de ejecucion
fin = time.time()

# Tiempo de ejecucion total
print('Se tardo ', tiempo, ' minutos en atender a ',
      estudiantes.__len__(), ' estudiantes')
