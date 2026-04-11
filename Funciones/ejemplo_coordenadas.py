print("--- Obtener coordenadas x,y,z ----")

def obtener_coordeanas():
    x, y, z = 10, 20, 30
    return(x, y, z)

# Llamar la función
resultado = obtener_coordeanas()
print(resultado)
# Unpacking de tupla
x1, y1, z1 = resultado
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')
