#Ejercicio Nro2 - Llenar una lista con los números del 1 al 10, luego modificar los elementos de la lista multiplicándolos por un valor que el usuario digite:

lista = list(range(1, 11))
print(lista)

num = int(input("Ingrese el número con el que desea multiplicar los elementos de la lista: "))
lista.clear()
for i in range(11):
    resultado = i * num
    lista.append(resultado)

print(lista)