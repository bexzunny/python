# Programa: Pedir la información e imprimir aceca de una receta de cocina
print("+"*4+" Receta de cocina "+"+"*4)
nombre_receta = input("Ingresa el nombre de la receta: ")
ingredientes = input("Ingresa los ingreditentes de la receta: ")
tiempo = int(input("Ingresa el tiempo de preparación (minutos): "))
dificultad = input("Ingresa la dificultad del platillo: ")

print("-"*10)
print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo}")
print(f"Dificultad: {dificultad}")

