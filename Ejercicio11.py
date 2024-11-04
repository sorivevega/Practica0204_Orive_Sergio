#Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
A = [(1, 2, 3), (4, 5, 6)]
B = [(-1, 0, 1), (0, 1, 1)]
W = (A[0][0] * B[0][0]) + (A[0][1] * B[0][1]) + (A[0][2] * B[0][2])
X = (A[0][0] * B[1][0]) + (A[0][1] * B[1][1]) + (A[0][2] * B[1][2])
Y = (A[1][0] * B[0][0]) + (A[1][1] * B[0][1]) + (A[1][2] * B[0][2])
Z = (A[1][0] * B[1][0]) + (A[1][1] * B[1][1]) + (A[1][2] * B[1][2])
print('La matriz resultante es: ', [(W, X), (Y, Z)])