#Ejercicio Nro5 - Hacer un programa para calcular el factorial de un numero positivo:

num = int(input("Ingrese un numero: "))

while num < 0:
    print('ERROR! el numero debe ser positivo')
    num = int(input("Ingrese un numero: "))

a = 1
for i in range(1, num + 1):
    a *= i

print(f'El factorial de {num} es: {a}')  