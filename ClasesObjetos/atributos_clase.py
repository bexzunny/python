class Persona:

    atributo_clase = 0

    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia


# Programa principal
if __name__ == '__main__':
    print(f'--- Atributos de Clase ---')
    print(f'Atributo de clase: {Persona.atributo_clase}')

    # Modificar el atributo de clase
    Persona.atributo_clase+=1
    print(f'Atributo nuevo de clase: {Persona.atributo_clase}')

    # Creamos el primer objeto
    persona1= Persona(15)
    print(f'Atributo de clase desde persona 1 (no recomendable): {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona 1 : {persona1.atributo_instancia}')

    # Segundo objeto
    persona2= Persona(30)
    print(f'Atributo de clase desde persona 2 (no recomendable): {persona2.atributo_clase}')
    print(f'Atributo de instancia desde persona 2 : {persona2.atributo_instancia}')