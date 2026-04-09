print("Bienvenido a una aplicación fitness")

#Declaración constantes
META_PASOS_DIARIOS = 1000
CALORIAS_POR_PASO = 0.04 #en kilocalorias

# Request de datos
nombre = input("Ingrese su nombre:")
pasos_caminados = int(input("Ingrese los pasos camindados hoy: "))

# Calculo de las kilodcalorias
calorias_quemadas = pasos_caminados *  CALORIAS_POR_PASO

# Verificación de pasos diaros cumplidos
cumplio_la_meta = True if pasos_caminados >= META_PASOS_DIARIOS else False

# Imprimir los datos
print(f"{nombre}, usted ha quemado: {calorias_quemadas} Kilocalorias")
if cumplio_la_meta:
    print(f"Felicidades por cumplir su meta de pasos: {pasos_caminados}")
else:
    print(f"Intente esforzarce, no consiguió la meta: {pasos_caminados}")
