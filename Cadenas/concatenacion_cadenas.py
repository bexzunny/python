# Programa: Ejemplo concdatenación cadenas

# 1. Usando el operador +
nombre = "Lucia"
apellido = "Gómez"
nombre_completo=nombre + " " + apellido
print("Usando + :" + nombre_completo)

# 2. Usando el método print
edad = 28
print("Usando comas: ","Nombre: ",nombre_completo,"\tEdad: ",edad)

# 3. Usando f-Strings
ciudad ="Barcelona"
pais ="España"
profesion= "Ongenieria"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad+2} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)