print('+++ Manejo de Sets +++')

# Crear un conjunto
mi_set={1,2,3,4,5,4}
#No hay índices

print(f"Mi set: {mi_set}")

#Agregar elementos al set
mi_set.add(6)
mi_set.add(7)

print(f"Mi set modificado: {mi_set}")
#Intentamos agregar un elemento duplicado
mi_set.add(3)
print(f"Mi set duplicado: {mi_set}")

# Eliminar un elemento del conjunto
mi_set.remove(4)
print(f"Mi set modificado: {mi_set}")

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento,end=" ")

# Comprobar si existe match
# Método indistinguible para listas, tuplas, sets
print(f"\nExiste el valor 4 en el set? {4 in mi_set}")
print(f"\nExiste el valor 1 en el set? {1 in mi_set}")

# Obtener la longitud del set
mi_set.add(1)
print(f"Longitud del conjunto: {len(mi_set)}")