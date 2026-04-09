print("Operador not")
condicion1 = True
#El operador regresa True si alguno de los operadores es True
resultado = not condicion1
print(f"Resultado not {condicion1} : {resultado}")

#Revisar si una variable es una cadena vacía
nombre= ""
es_cadena_vacia = not nombre
print(f"\n La variable NO tiene ningúnm valor: {es_cadena_vacia}")

#Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f"\n La variable NO tiene ningúnm valor: {es_variable_sin_valor}")
