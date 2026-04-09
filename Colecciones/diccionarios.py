from os import pwrite

print('---- Diccionarios en python ----')
# Creamos un diccionario de persona con clave y valor
persona = {
    'nombre':'Sergio',
    'edad': 30,
    'ciudad':'México'
}

print(f"Diccionario de persona: {persona}")

# Acceder a los elementod del diccionario
print(f'Nombre: {persona['nombre']}')
print(f"Edad: {persona.get('edad')}")
print(f"Ciudad: {persona.get('ciudad')}")

# Modificar un valor del diccionario
persona['edad'] = 35
print(f"Diccionario de persona: {persona}")

#Agregar nuevo elemento
persona['profesion'] = 'ingeniero'
print(f"Diccionario de persona: {persona}")

# Eliminar un elemento
del persona['ciudad']
print(f"Diccionario de persona: {persona}")

# Iterar los elementos del diccionario (Llave, valor)
for llave, valor in persona.items():
    print(f"Llave: {llave}, valor :{valor}")

# Obtener los valores
print(f"\nValores del diccionaro")
for valor in persona.values():
    print(f" - Valor: {valor}")

# Obtener las llaves
print(f"\nLlaves del diccionario")
for llave in persona.keys():
    print(f" - Llave: {llave}")