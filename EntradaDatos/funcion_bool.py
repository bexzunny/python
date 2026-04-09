# Programa: Funcion bool

# 1. Numeros int y float
print(f"Caso 0: {bool(0)}")      # False: El vacío numerico
print(f"Caso 0.0: {bool(0.0)}")      # False: El vacío numerico
print(f"Caso 42: {bool(42)}")      # True: Valor distinto de 0

# 2. Texto str
# Cadena vacía = Nada = False
print(f"Caso \"\": {bool("")}")

# Cadena con espacio o texto = True
print(f"Caso \" \": {bool(" ")}")
print(f"Caso Hola: {bool("Hola")}")

# 3. None (ausencia total)
vavio = None
print(f"Caso None: {bool(vavio)}")
print(f"Caso False: {bool(False)}")