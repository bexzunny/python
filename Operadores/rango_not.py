# Revisar si una variable esta en un rango de 0 y 10
dato = int(input("Proporciona un número entero: "))

# Revisamos si está dentro del rango
#esta_dentro_rango = 1 <= dato <= 10
#print(f"Variable dentro del rango: {esta_dentro_rango}")

# Revisamos la lógica inversa
esta_fuera_rango = not(1 <=dato <= 10)
print(f"Variable fuera del rango: {esta_fuera_rango}")