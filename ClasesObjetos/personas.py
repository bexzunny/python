class Persona:

    contador_personas=0

    def __init__(self,nombre=None,apellido=None):
        Persona.contador_personas+=1
        self._nombre = nombre
        self._apellido = apellido
        self._id = self.contador_personas

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido (self):
        return self._apellido
    @property
    def ide(self):
        return self._id

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    def mostrar_datos(self):
        print(f'''Datos persona: {self._id}
        Nombre: {self._nombre}
        Apellido: {self._apellido}''')

    @staticmethod
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_personas
    @classmethod
    def get_contador_personas_clase(cls):
        print('Método clase')
        return cls.contador_personas


if __name__ == '__main__':
    persona1 = Persona('Adair', 'Cruz')
    persona1.mostrar_datos()

    persona2 = Persona()
    persona2.nombre = 'Jennifer'
    persona2.apellido = 'Chávez'
    print(f'''Persona: {persona2.ide}
    Nombre: {persona2.nombre}
    Apellido: {persona2.apellido}''')
    print(f'Condador objetos persona: {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Clase: {Persona.get_contador_personas_clase()}')