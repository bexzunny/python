print("---- Función con argumentos por nombre ----")

def imprimir_persona(nombre,apellido = '',edad = 0):
    print(f'Persona : nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Adair','Cruz',18)

# Llamar la función usando argumentos por nombre
imprimir_persona(nombre='Samantha',apellido='Corona', edad=20)

# Llamar la función usando argumentos por nombre, pero intercambiando el órden
imprimir_persona(edad = 20, apellido='Angeles', nombre='Luisa')

#Argumentos con valores por defdault
imprimir_persona(nombre='Jesus')
imprimir_persona(apellido='De Huitrón',nombre='Aurelia')

