#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abc = 'abcdefghijklmnñopqrstuvwxyz'
abc = list(abc)
for x in range(len(abc), 1, -1):
    if x % 3 == 0:
        abc.pop(x -1)
print(abc)