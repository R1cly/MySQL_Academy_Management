# Importamos la libreria MySQL.Connector para conectarnos al Workbench
import mysql.connector
import sys


"""""

Academy Database Manager.

Metodos de la libreria mysql.connector que vamos a utilizar

myDatabase = mysql.connector.connect(credenciales)
myCursor = myDatabase.cursor()
myDatabase.commit()
myDatabase.close()

"""


def imprimirDatos():

    myCursor.execute("USE academia_db")

    print("[1] Alumnos")
    print("[2] Empleados")
    print("[3] Profesores")

    print("")
    seleccionarTabla = int(input("Selecciona la tabla que quieres ver\n"))


    # Busqueda de alumnos

    if seleccionarTabla == 1:

        print("Introduce el curso")
        print("[1] 2 Grado Medio:")
        print("[2] 2 Grado Superior")
        print("[3] Todos los alumnos del centro")
        seleccionarCurso = int(input(""))

        if seleccionarCurso == 1:
            myCursor.execute("SELECT * FROM alumnos WHERE cursoAlumno = '2GM'")
            print("ID  |  NOMBRE  |  APELLIDOS  |  DIRECCION  |TELEFONO  |  DNI  |  CURSO\n")
            for alumno in myCursor:
                print(alumno)

        elif seleccionarCurso == 2:
            print("ID  |  NOMBRE  |  APELLIDOS  |  DIRECCION  |TELEFONO  |  DNI  |  CURSO\n")
            myCursor.execute("SELECT * FROM alumnos WHERE cursoAlumno = '2GS'")

            for alumno in myCursor:
                print(alumno)

        elif seleccionarCurso == 3:
            print("ID  |  NOMBRE  |  APELLIDOS  |  DIRECCION  |  TELEFONO  |  DNI  |  CURSO\n")
            myCursor.execute("SELECT * FROM alumnos")

            for alumno in myCursor:
                print(alumno)

        else:
            print("No has seleccionado un numero valido")
            sys.exit()

    # Busqueda de empleados.

    elif seleccionarTabla == 2:
        print("ID  |  NOMBRE  |  APELLIDOS  |  DIRECCION  |  TELEFONO  |  DNI  |  PUESTO\n")
        myCursor.execute("SELECT * FROM empleados")

        for empleado in myCursor:
            print(empleado)

    # Busqueda de profesores

    elif seleccionarTabla == 3:
        print("ID  |  NOMBRE  |  APELLIDOS  |  DIRECCION  |TELEFONO  |  DNI\n")
        myCursor.execute("SELECT * FROM profesores")

        for profesor in myCursor:
            print(profesor)

    else:
        print("No has introducido un valor correcto")




def introducirDatos():

    myCursor.execute("USE academia_db")

    print("¿Qué quieres introducir?")
    print("[1] Alumno")
    print("[2] Empleados")
    print("[3] Profesores\n")
    seleccionarAlumno = int(input(""))

    if seleccionarAlumno == 1:

        print("Vamos a crear un alumno \n")

        print("Nombre del alumno [*]")
        nombreAlumno = input("")

        print("Apellido del alumno [*]")
        apellidoAlumno = input("")

        print("Direccion del alumno [*]")
        direccionAlumno = input("")

        print("Telefono del alumno")
        telefonoAlumno = input("")

        print("DNI del alumno")
        dniAlumno = input("")

        print("Curso del alumno [*]\n")

        print("[1] 2 Grado Medio")
        print("[2] 2 Grado Superior")
        seleccionarCurso = int(input(""))

        if seleccionarCurso == 1:
            cursoAlumno = "2GM"

        elif seleccionarCurso == 2:
            cursoAlumno = "2GS"

        else:
            print("Error al crear el alumno")
            sys.exit()

        sql = "INSERT INTO alumnos (nombreAlumno,apellidoAlumno,direccionAlumno,telefonoAlumno,dniAlumno,cursoAlumno) VALUES (%s,%s,%s,%s,%s,%s)"

        valores =(nombreAlumno,apellidoAlumno,direccionAlumno,telefonoAlumno,dniAlumno,cursoAlumno)
        myCursor.execute(sql,valores)
        myDatabase.commit()

        print("Alumno creado correctamente!")

    elif seleccionarAlumno == 2:
        print("Vamos a crear a un empleado!\n")

        print("Nombre del empleado [*]")
        nombreEmpleado = input("")

        print("Apellido del empleado [*]")
        apellidoEmpleado = input("")

        print("Direccion del empleado [*]")
        direccionEmpleado = input("")

        print("Telefono del empleado")
        telefonoEmpleado = input("")

        print("DNI del empleado")
        dniEmpleado = input("")

        print("Puesto del empleado [*]\n")

        puestoEmpleado = input("")

        sql = "INSERT INTO empleados (nombreEmpleado,apellidoEmpleado,direccionEmpleado,telefonoEmpleado,dniEmpleado,puestoEmpleado) VALUES (%s,%s,%s,%s,%s,%s)"

        valores =(nombreEmpleado,apellidoEmpleado,direccionEmpleado,telefonoEmpleado,dniEmpleado,puestoEmpleado)
        myCursor.execute(sql,valores)
        myDatabase.commit()

        print("Empleado creado correctamente")



    elif seleccionarAlumno == 3:
        print("Vamos a crear a un profesor!\n")

        print("Nombre del profesor [*]")
        nombreProfesor = input("")

        print("Apellido del profesor [*]")
        apellidoProfesor = input("")

        print("Direccion del profesor [*]")
        direccionProfesor = input("")

        print("Telefono del profesor")
        telefonoProfesor = input("")

        print("DNI del profesor")
        dniProfesor = input("")

        sql = "INSERT INTO profesores (nombreProfesor,apellidoProfesor,direccionProfesor,dniProfesor,telefonoProfesor) VALUES (%s,%s,%s,%s,%s)"

        valores =(nombreProfesor,apellidoProfesor,direccionProfesor,dniProfesor,telefonoProfesor)
        myCursor.execute(sql,valores)
        myDatabase.commit()

        print("Profesor creado correctamente\n")


# Funcion MAIN en la que ejecutaremos las funciones para ingresar datos.

if __name__ == '__main__':


    # Intentamos realizar la conexión a la base de datos
    # Si la conexión falla ponemos una exepcion.

    try:
        myDatabase = mysql.connector.connect(host="localhost",
                                passwd = "noseaquien",
                                user="root")

        myCursor = myDatabase.cursor()

        print("Conexión a la base de datos realizada\n")

    except:
        print("Error al entrar al conectar a la base de datos! \n")
        print("Revisa los credenciales")


    print("¿Que quieres hacer?")
    print("[1] Imprimir datos")
    print("[2] Introducir datos")

    seleccionarQueHacer = int(input(""))

    if seleccionarQueHacer == 1:
        imprimirDatos()

    elif seleccionarQueHacer == 2:
        introducirDatos()

    else:
        print("ERROR!")
        sys.exit()