#Solicitar el nombre, dias de estadía y vista al mar
print("Bienvenido a Zunny's hotel")

CON_VISTA_AL_MAR = 150.50
SIN_VISTA_AL_MAR = 190.50

nombre = input("Ingrese su nombre: ")
dias_estancia = int(input("Cuántos días se va a quedar: "))
con_vista_al_mar = input("Quiere cuarto con vista al mar (si/no): ")


if con_vista_al_mar.strip().lower() == "si":
    total = dias_estancia* CON_VISTA_AL_MAR
    tiene_vista_mar = con_vista_al_mar
else:
    total = dias_estancia * SIN_VISTA_AL_MAR
    tiene_vista_mar = "no"
print(f"------Detalle de la reservación-----")
print(f"Reservación hecha, {nombre}")
print(f"Dias de estancia: {dias_estancia}")
print(f"Total de la estancia: {total}")
print(f"Con vista al mar: {tiene_vista_mar}")