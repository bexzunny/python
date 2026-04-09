print("Manejo de tuplas")
mi_tupla=(1,2,3,4,5)

print(mi_tupla)
#No se puede modificar una tupla
#mi_tupla[0]=10

#Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento,end =" ")

# Crear tupla para coordenada x,y
coordenadas = 3,5
# Acceder a cada elemento de la tupla
print(f"\nCoordenada en el eje x: {coordenadas[0]}")
print(f"Coordenada en el eje y: {coordenadas[1]}")

# Crear tupla unitaria
tupla_unitaria = 10,
print(f"Tupla de un elemento: {tupla_unitaria}")

# Tupla anidada
tuplas_anidadas = (1,(2,3),(4,5))
print(tuplas_anidadas[1][1])