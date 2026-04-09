# Promedio de calificaciones
print("++++ Promedio de calificaciones ++++")
no_calificaciones=None
lista_calif=[]
suma =0

no_calificaciones=int(input("Ingrese el numero de calificaciones: "))

for i in range(no_calificaciones):
    lista_calif.append(int(input(f"Ingrese la calificación {i+1}: ")))
    suma+=lista_calif[i]
promedio = suma/no_calificaciones
print(f"Las calificaciones propoorcionadas son: {lista_calif}")
print(f"El promedio es de: {promedio}")