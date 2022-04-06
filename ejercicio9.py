"""

#Ejercicio Nro9 - Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase pero sin sin espacios
en blanco y además un contador de cuántos caracteres tiene la frase (sin contar los espacios en blanco). Ejm:

Frase: Hola que tal?
Frase modificada: Holaquetal?
Caracteres: 11

"""

frase = input('Ingrese una frase: ')
mod = ''

for i in frase:
    if i != ' ':
        mod += i
    caracteres = len(mod)

print(f'Frase Original: {frase}') 
print(f'Frase Modificada: {mod}') 
print(f'Caracteres en total: {caracteres}')