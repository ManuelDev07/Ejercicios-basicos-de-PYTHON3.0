#Ejercicio Nro4 - Hacer un programa para sumar números pares dentro de un rango.

lista = []

inicio = int(input('Determine de donde inicia el rango: '))
fin = int(input('Determine el final del rango: '))
suma = 0

for i in range(inicio, fin + 1, 2):
    lista.append(i)
    if i % 2 == 0:
        suma += i

print(f'Lista original: {lista}')
print(f'El resultado de la suma es: {suma}') 
