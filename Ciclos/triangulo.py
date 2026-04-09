# Programa: preguntar el no. de filas de un triangulo y dibujarlo
print("----Dibujar un triángulo simétrico----")

filas = int(input("Ingresa el número de filas: "))


for a in range(1,filas+1):
    for e in range(a-filas,0):
        print(" ", end="")
    for i in range(0,a+(a-1)):
        print("*",end="")
    print()

for fila in range(1,filas+1):
    esp_blamco = " " *(filas-fila)
    ast = "*" * (2*fila-1)
    print(f"{esp_blamco}{ast}")