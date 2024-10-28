#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
number = []
for i in range(6):
    x  = int(input('Introduzca los numeros de la loteria: '))
    number.append(x)
    number.sort()
print(number)