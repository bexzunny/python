# Mostrar la estación del año dependiendo el número del mes
print("Bienvenido, ingrese el número del mes: ")

mes = int(input("Proporcione el número del mes: "))

print(f"La estación del mes {mes} : ",end=" ")
match mes:
    case 1|2|12:
        print("Invierno")
    case 3|4|5:
        print("Primavera")
    case 6|7|8:
        print("Verano")
    case 9|10|11:
        print("Otoño")
    case _:
        print("Estación desconocida")
