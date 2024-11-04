#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input('Introduzca una palabra: ')
if palabra == palabra[::-1]:
    print('La palabra escrita es un palindromo')
else:
    print('La palabra escrita no es un palindromo')