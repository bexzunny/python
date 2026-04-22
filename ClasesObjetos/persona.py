# Definición de una clase
# dos palabras AsiSeVaAVer
class Persona:
    def __init__(self,nombre,apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    #def inicializar_persona(self,nombre,apellido):


    def mostrar_persona(self):
       print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
       print(f'Dirección de memoria persona1: {id(self)}')
       print(f'Dirección de memoria hex: {hex(id(self))}')

# Creación de objetos
if __name__ == "__main__":
    # Creación de un primer objeto
    persona1= Persona('Adair','Cruz') # Se crea un objeto vacío
    #persona1.inicializar_persona('Adair','Cruz')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona('Jennifer', 'Sánchez')
    persona2.mostrar_persona()