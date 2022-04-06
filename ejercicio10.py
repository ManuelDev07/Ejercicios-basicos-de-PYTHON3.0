#Ejercicio Nro10 - Hacer in programa que pida una cadena, luego añadir c/u de los caracteres en una lista sin repetir caracteres:

lista = []

frase = input('Ingrese un texto: ')

for i in frase:
    lista.append(i)

conjunto = set(lista)
lista = list(conjunto)
print(lista)