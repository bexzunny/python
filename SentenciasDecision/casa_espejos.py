print("++++Bienvenido a la casa de los espejos++++")

edad = int(input("Cuantos años tienes: "))
tiene_miedo = input("Te da miedo la oscuridad? (si/no): ")

if not tiene_miedo.strip().lower() == "si":
    es_miedoso = False
else:
    es_miedoso = True

if not edad<=10 and es_miedoso == False:
    print("Puedes pasar.")
else:
    print("No queremos niños.")
