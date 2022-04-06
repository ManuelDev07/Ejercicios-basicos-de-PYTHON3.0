#Ejercicio Nro 3 - Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor:

lista = []

num = int(input("Ingrese un numero a la lista: "))
while num != 0:
    lista.append(num)
    lista.sort()
    num = int(input("Ingrese un numero a la lista: "))

print(lista)
