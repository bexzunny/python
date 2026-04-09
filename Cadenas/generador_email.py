# Programa: general email a partir de los datos
# Inicializar variables
nombre = "Adair Jesús"
empresa = "Bex Zunny"
ext_dominio = ".gob.mx"

# Generar titulo
print("+"*4 + "Generador de email" + "+"*4)
print(f"Nombre de usuario: {nombre}")

# Pasar a minúsculas todo y reemplazar " " (espacios) por "." (punto)
nombre_norm = nombre.lower().replace(" ", ".")

# Imprimir el usuario normalizado
print(f"Nombre usuario normalizado: {nombre_norm}\n")

# Imprimir el nombre de la empresa y el dominio
print(f"Nombre de empresa: {empresa}\nDominio: {ext_dominio}")

#crear el dominio
dominio_norm = f"@{empresa.lower().replace(' ','')}{ext_dominio}"

#imprimir el dominio normalizado
print(f"Dominio normalizado: {dominio_norm}\n")

#imprimir el email generado
email=f"{nombre_norm}{dominio_norm}"
print(f"Email final generado: {email}")