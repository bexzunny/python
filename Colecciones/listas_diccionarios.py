print("---- Listas y diccionarios ----")
personas = [
    {
        'nombre':'Samantha',
        'apellido':"Corona",
        'edad':19
     },
    {
        'nombre': 'Adair',
        'apellido': "Huitrón",
        'edad': 18
    }
]

# Iterar los datos
for persona in personas:
    for clave,valor in persona.items():
        print(f"{clave} : {valor}")
    print("---------")

for contador,persona in enumerate(personas):
    print(f"{contador + 1} - Persona: {persona}")