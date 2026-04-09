print("Calcular el area y perimetrode un rectangulo")
#Pedir los datos de base y altura en float
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# hacer las operaciones
perimetro = (base*2)+(altura*2)
area = base * altura

#Imprimir
print(f"El perímetro del rectángulo es: {perimetro}\nEl área es de: {area}")