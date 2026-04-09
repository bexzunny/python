# Programa: Reemplazar textos en python

mensaje = "Hola mundo, mundo"

# Reemplazar TODAS las coincidencias
nuevo=mensaje.replace("mundo", "python")
print(nuevo)
# Salida: Hola python, python

# Reemplazar una sola vez
uno_solo = mensaje.replace("mundo","Dev",1)
print(uno_solo)