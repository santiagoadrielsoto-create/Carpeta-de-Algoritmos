"""
2-
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def cargar():
    alumnos={}
    for i in range(3):
        dni=int(input(F"Ingrese el DNI del alumno {i+1}"))
        continuar="si"
        lista=[]
        while continuar=="si":
            mat=input(F"Ingrese el nombre de la materia:")
            nota=int(input(F"Ingrese la nota del alumno con DNI - {dni} - en la materia {mat}:"))
            lista.append((mat,nota))
            continuar=input("Desea ingresar otra materia para el alumno con DNI - {dni} - ? [si/no]")
        alumnos[dni]=lista
    return alumnos

def imprimir(alumnos):
    print("Listado completo de todos los alumnos, con sus materias y respectivas notas:")

    for dni in alumnos:
        print(F"Para el dni - {dni} - ")
        for mat,nota in alumnos[dni]:
            print(F"En la materia {mat} se saco un {nota}")

def consulta(alumnos):
    doc=input(F"Ingrese el DNI que quiera consultar:")
    for doc in alumnos:
        for mat,nota in alumnos[doc]:
            print(F"En la materia {mat} se saco un {nota}")
alumnos=cargar()
imprimir(alumnos)
consulta(alumnos)
