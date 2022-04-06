"""

#Ejercicio Nro1 - Llenar una lista con los números del 1 al 50, luego mostrar la lista
con un bucle for, los elementos deben mostrarse de la siguiente forma:

1-2-3-4-...-50

"""

lista = []
var = 0

while var <= 50:
    lista.append(var)
    var += 1

for i in lista:
    print (i, end="-")