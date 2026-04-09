# Ejemplo: Cadenas inmutables

animal = "gato"
# animal[4] = "s"     error
# CORRECTO  : concatenar (sumar)
#Tomamos "gato" +"s" y lo guardamos en una nuev avariable
plural = animal+"s"
print(animal) # Salida: "gato" (intacto)
print(plural) # Salida "gatos" (nuevo objeto)

plural= f"{animal}s"
print(plural)