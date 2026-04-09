# Programa: aplicar el concepto de slicing
        #210987654321
texto = "PROGRAMACIÓN"
        #123456789012
# 1. Basico [inicio:fin]
print(texto[0:4])   # PROG (el incice 4 no se incluye)

# Atajo desde el inicio [:fin]
print(texto[:4])    # PROG (se asume desde el inicio)

# 3. Atajo hasta el final [inicio:]
print(texto[8:])    #CION (desde el 8)

# 4. Índices negaticos
print(texto[-4:])   #CION (ultimos 4)

# 5. Pasos [::-pasos] invertir la cadena
print(texto[::-1])  #NÓICAMARGORP
