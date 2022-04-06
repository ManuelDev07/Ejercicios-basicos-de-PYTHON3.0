#Ejercicio Nro6 - Hacer un programa que pida un número y guarde en un lista su tabla de multiplicar hasta el 10:

lista = []

num = int(input("Ingrese un numero: "))
for i in range(1, 11):
    i *= num
    lista.append(i)

print(f"Su tabla de multiplicar es: {lista}")
    


