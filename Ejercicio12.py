#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
n = (input('Introduzca los numeros separados por comas: '))
n = n.split(',')
x = len(n)
for y in range(x):
    n[y] = int(n[y])
n = list(n)
suma = 0
suma2 = 0
for y in n:
    suma += y
    suma2 += y**2
media = suma / x
print(media)