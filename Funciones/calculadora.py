from funciones_calc import *
print('---- Calculadora ----')

while True:
    mostrar_menu()
    opcion = pedir_numero("_:")

    match opcion:
        case 1: # Suma
            num1,num2 = obtener_numeros()
            sumar(num1,num2)
        case 2: # Resta
            num1, num2 = obtener_numeros()
            restar(num1, num2)
        case 3: # Multiplicación
            num1,num2 = obtener_numeros()
            mult(num1,num2)
        case 4: # División
            num1,num2 = obtener_numeros()
            div(num1,num2)
        case 5: # Salid
            break
        case _:
            print('Opción no válida')