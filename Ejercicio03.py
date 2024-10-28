#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
asig = ['DAPI', 'SIRC', 'SIHD', 'GPIT']
A = float(input('¿Que nota has sacado en DAPI?'))
B = float(input('¿Que nota has sacado en SIRC?'))
C = float(input('¿Que nota has sacado en SIHD?'))
D = float(input('¿Que nota has sacado en GPIT?'))
notas = [A, B, C, D]
range(len(asig))
range(len(notas))
for x in range(len(asig)):
    print('En', asig[x], 'he sacado', notas[x])    