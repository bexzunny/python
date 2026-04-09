# Promedio de calificaciones
def comprobar(strng):
    try:
        strng=float(strng)
        if not strng>10:
            if not strng<0:
                return True
            else:
                print("Debe ingresar una calificacion mayor a 0")
                return False
        else:
            print("Debe ingresar una calificación menor a 10")
            return False
    except:
        print("Debe ingresar un numero (0-10)")
        return False

def pedir_numero(i):
    es_valido = False
    while es_valido==False:
        numero=input(f"Ingrese la calificación {i+1}: ")
        es_valido=comprobar(numero)
    return float(numero)


print("++++ Promedio de calificaciones ++++")
no_calificaciones=None
lista_calif=[]
suma =0

no_calificaciones=int(input("Ingrese el numero de calificaciones: "))

for i in range(no_calificaciones):
    lista_calif.append(pedir_numero(i))
    suma+=lista_calif[i]
promedio = suma/no_calificaciones
print(f"Las calificaciones propoorcionadas son: {lista_calif}")
print(f"El promedio es de: {promedio}")