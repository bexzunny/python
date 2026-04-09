print("++++ Playlist de canciones ++++")

#Crear una laista vacía
lista_reproduccion =[]

numero_canciones = int(input("Cuantas canciones deseas agregar: "))
#Iterar cada elemento en la lista para agregar un nuevo elemento
for indice in range (numero_canciones):
    cancion = input(f"Proporciona el índice de la canción {indice+1}:")
    lista_reproduccion.append(cancion)

# Agregar canciones
lista_reproduccion.append("Tarantula - Gorillaz")
lista_reproduccion.append("CHIHIRO - Billie Eilish")
lista_reproduccion.append("Wildflower - Billie Eilish")

# Ordenar la lista en orden alfabético .sort()
#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

# Mostrar la lista de canciones
print("\nLa reproducción en órden alfabético:")
print(lista_reproduccion)

# Mostrar la lista iterando sus elementos
print("Iteramos la playlist")
for cancion in lista_reproduccion:
    print(f"- {cancion}")