# Programa: pedir nombre, apellido y año de nacimiento, generar un id

from random import randint

# Pedir nombre
nombre = input("Ingresa tu nombre: ")

# Pedir apellido
apellido = input("Ingresa tu apellido: ")

# Pedir año de nacimiento
birthday = input("Ingresa tu año de nacimiento: ")


id_usuario = f"{nombre[0:2].upper()}{apellido[-2:].upper()}{birthday[-2:]}{randint(1000,9999)}"
print(f"Hola: {nombre}")
print("\tTu numero de identificación generado por el sistema es:")
print(f"\t{id_usuario}")
print(f"\tFelicidades¡")
