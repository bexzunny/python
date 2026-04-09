<<<<<<< HEAD
# 10, 9: A 8,9 = B

calificacion = float(input("Ingrese la calificación a convertir: "))

print(f"Su calificación {calificacion} en alfabeto es: ",end="")
match calificacion:
    case x if 9 <= x <= 10:
        print("A")
    case x if 8 <= x < 9:
        print("B")
    case x if 7 <= x < 8:
        print("C")
    case x if 6 <= x < 7:
        print("D")
    case x if 5 <= x < 6:
        print("E")
    case x if 0 <= x < 5:
        print("F")
=======
# 10, 9: A 8,9 = B

calificacion = float(input("Ingrese la calificación a convertir: "))

print(f"Su calificación {calificacion} en alfabeto es: ",end="")
match calificacion:
    case x if 9 <= x <= 10:
        print("A")
    case x if 8 <= x < 9:
        print("B")
    case x if 7 <= x < 8:
        print("C")
    case x if 6 <= x < 7:
        print("D")
    case x if 5 <= x < 6:
        print("E")
    case x if 0 <= x < 5:
        print("F")
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
