import tensorflow as tf
import time

# Inicio de la simulación para medir el tiempo
inicio = time.time()


precio_matricula = 14
total_atendidos = []

# Inicializar materias
materias_habilitadas = ["Fisica", "Programacion", "Redes", "Base de datos", "Inteligencia Artificial",
                        "Calculo 1", "Calculo 2", "Ingles 1", "Ingles 2", "Algebra 1", "Algebra 2", "Telefonia IP", "Programacion WEB"]


class AgenteEstudiante(object):
    def __init__(self, nombre, carrera, matricula, dinero, materias):
        # Inicializar los atributos nombre y carrera y las variables de Tensorflow necesarias para el agente
        self.nombre = nombre
        self.carrera = carrera
        self.materias = materias
        self.matricula = matricula
        self.dinero = dinero
        self.boleta = tf.Variable("", dtype=tf.string)
        self.pagado = tf.Variable(False, dtype=tf.bool)

    def solicitar_inscripcion(self):

        materias = self.materias
        # Lógica para solicitar la inscripción del estudiante en las materias
        time.sleep(1)
        print("Agente Estudiante: "+self.nombre +
              " esta solicitando inscribirsea las materias.....")
        time.sleep(1)
        print(materias)

    def pagar(self):
        # Lógica para realizar el pago de la matrícula por parte del estudiante
        time.sleep(1)
        print("Agente Estudiante: Realizando pago de matrícula.....")
        if (estudiante.dinero < precio_matricula):
            time.sleep(1)
            print("El monto pagado es menor al precio de la matrícula......")
            return
        if (estudiante.dinero == precio_matricula):
            self.pagado.assign(True)
            total_atendidos.append(estudiante)
            time.sleep(1)
            print("Agente Estudiante: Pagando matricula.....")

        elif (estudiante.dinero > precio_matricula):
            self.pagado.assign(True)
            total_atendidos.append(estudiante)
            time.sleep(1)
            print("Agente Estudiante: Pagando matricula.....")
            cambio = estudiante.dinero - precio_matricula
            time.sleep(1)
            print("Pago con billete de: "+str(estudiante.dinero) +
                  " su cambio es: " + str(cambio))

    def obtener_boleta(self):
        # Lógica para obtener la boleta de pago del estudiante
        time.sleep(1)
        print("Agente Estudiante: Obteniendo boleta de pago del estudiante " + self.nombre)

        return self.boleta


class AgenteCajero(object):
    def __init__(self):
        # Inicializar la variable de Tensorflow necesaria para el agente
        self.boleta = tf.Variable(0.0, dtype=tf.float32)

    def cobrar_matricula(self, estudiante):
        # Verificar que el estudiante haya realizado el pago
        if not estudiante.pagado.numpy():
            time.sleep(1)
            print(
                "Agente Cajero: El estudiante no ha realizado el pago de la matrícula.....")
            return

        # Lógica para cobrar la matrícula y obtener la boleta del estudiante
        time.sleep(1)
        print("Agente Cajero: Recibiendo pago de matrícula del estudiante.....")
        self.boleta.assign(estudiante.matricula)
        time.sleep(1)
        print("Agente Cajero: Pago de matrícula recibido. Generando boleta de pago.....")
        return self.boleta.numpy()


class AgenteDirector(object):
    def __init__(self):
        # Inicializar las variables de Tensorflow necesarias para el agente
        self.materias = tf.Variable([], dtype=tf.string, shape=(None,))

    def inscribir_estudiante(self, estudiante):
        materias = estudiante.materias
        # Lógica para inscribir al estudiante en las materias seleccionadas
        # Verificar que el estudiante haya realizado el pago
        if not estudiante.pagado.numpy():
            time.sleep(1)
            print(
                "Agente Director: El estudiante no ha realizado el pago de la matrícula por lo tanto no puede inscribirse....")
            return
        if materias in materias_habilitadas:

            # Lógica para inscribir al estudiante en las materias seleccionadas
            time.sleep(1)
            print("Agente Director: Inscribiendo al estudiante " +
                  estudiante.nombre + " en las materias seleccionadas.....")
            self.materias.assign(materias)
            time.sleep(1)
            print("Agente Director: Inscripción del estudiante " +
                  estudiante.nombre + " completada con éxito en las materias:")
            time.sleep(1)
            print(materias)
        else:
            time.sleep(1)
            print(
                "Agente Director: Las materias seleccionadas no se encuentran habilitadas.....")


class AgenteResponsable(object):
    def __init__(self):
        # Inicializar la variable de Tensorflow necesaria para el agente
        self.materias = tf.Variable([], dtype=tf.string, shape=(None,))

    def habilitar_materias(self, materias):
        # Lógica para habilitar las materias seleccionadas
        time.sleep(1)
        print("Agente Responsable: Habilitando materias......")
        self.materias.assign(materias)
        # Imprimir materias
        time.sleep(1)
        print(materias)
        time.sleep(1)
        print("Agente Responsable: Materias habilitadas con éxito.....")


# Interaccion de los agentes


# Crear un responsable
responsable = AgenteResponsable()

# Crear un cajero
cajero = AgenteCajero()

# Crear un director
director = AgenteDirector()

# Habilitar materias
responsable.habilitar_materias(materias_habilitadas)
# Crear un estudiante
estudiante1 = AgenteEstudiante(
    "Juan", "Ingeniería de Sistemas", 12345, 20, ["Fisica", "Programacion", "Calculo 1"])

estudiante2 = AgenteEstudiante(
    "Luis", "Ingeniería de Sistemas", 45678, 12, ["Algebra 1", "Programacion WEB", "Base de datos"])

estudiante3 = AgenteEstudiante(
    "Raul", "Ingeniería de Sistemas", 98765, 60, ["Inteligencia artificial", "Telefonia IP", "Programacion WEB"])

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
    time.sleep(1)
    print("-------------------------------------------------------------------------")


# Total recaudado
print("Total recaudado: " + str(total_atendidos.__len__()*precio_matricula))

# Fin del tiempo de ejecucion
fin = time.time()

# Tiempo de ejecucion total
print("Se tardo ", (fin-inicio)/3, " minutos en atender a ",
      estudiantes.__len__(), " estudiantes")

# que tipo de agente se uso en la implementacion de la solucion del problema
""" En esta implementación se usan agentes reactivos simples. Los agentes reactivos simples se basan en la percepción del entorno actual y en la ejecución de acciones inmediatas en respuesta a esa percepción, sin tener en cuenta el estado del entorno en el futuro. Los agentes reactivos simples no tienen un modelo interno del entorno y no tienen objetivos a largo plazo.

En el caso de esta implementación, cada agente estudiante y cajero reacciona a las acciones realizadas por los otros agentes y realizan sus propias acciones en respuesta a esas acciones. Por ejemplo, cuando un agente cajero recibe un pago de matrícula de un agente estudiante, genera una boleta de pago inmediatamente en respuesta a esa acción. Sin embargo, los agentes no tienen un modelo interno del entorno y no tienen objetivos a largo plazo. """


# porque tensorflow es una herramienta adecuada para la implementacion de la solucion del problema
""" En esta implementación se utiliza Tensorflow para crear y manipular variables que contienen información relevante para los agentes,  el atributo pagado en la clase AgenteEstudiante es una variable de Tensorflow que se actualiza cuando el método pagar() es llamado. Esto permite a los métodos de las clases acceder a valores actualizados de las variables y realizar operaciones matemáticas en ellas, como en el caso de la clase AgenteCajero cuando se asigna el valor de la matrícula del estudiante a la variable boleta utilizando Tensorflow. Esto permite que los agentes puedan acceder y modificar esta información de manera sencilla y eficiente en tiempo de ejecución.

Los agentes utilizados en esta implementación son reactivos simples, ya que se basan en la información disponible en el momento y realizan acciones de manera inmediata en respuesta a esa información. """


# se utilizo la libreria time para medir el tiempo de ejecucion del programa
# se puso un retraso de 1 segundo antes de cada print para ver la interecccion de los agentes secuencialmente
# se dividio el total de tiempo entre 3 para simular una duracion mas realista de la interaccion de agentes
