print("++++ Manejo de listas ++++")

mi_lista = [1,2,3,4,5]

print(f"{mi_lista} -> Lista original")

# Largo de una lista
print(f"Largo de una lista: {len(mi_lista)}")

# Acceder a los elemenots de una lista por el indice
print(f"Accedemos al valor del índice 4 : {mi_lista[4]}")
print(f"Acceder al último índice de la lista: {mi_lista[-1]}")

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f"Modificamos el valor del índice 1: {mi_lista[1]}")

# Agregar un elemento al final de la lista
mi_lista.append(6)
print(f"{mi_lista} -> Se agregó el elemento 6")

# Añadir un nuevo elemento al índice especificado
mi_lista.insert(2,15)
print(f"{mi_lista} -> Se agregó 15 al index 2")

# Eliminar elementos de una lista
#   Método remove
mi_lista.remove(5)
print(f"{mi_lista} -> se removió el elemento con el valor 5")

#   método pop
mi_lista.pop(1) #Remueve el el elemento 1 de la lista
print(f"{mi_lista} -> se removió el elemento con el index 1")

#   del
del mi_lista[2]
print(f"{mi_lista} -> se removió el elemento con el index 2")

#Obtener sublistas
sublista = mi_lista[1:3] #Genera una sublista del 1 al 2
print(f"sublista [1:3] = {sublista}")