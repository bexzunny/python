# Defiinimos la clase coche
class Coche:
    def __init__(self,marca,modelo,color):
        self._marca = marca
        self._modelo=modelo #Atributos protegidos
        self._color=color

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')
        # Dentro de la clase no es necesario get y set

    # def get__marca(self):
    #     return self._marca
     # Ctr + /
    @property # Definir el método haciendolo pythonic
    def marca(self):
        return self._marca

    # def set_marca(self,marca):
    #     self._marca = marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color





# Programa principal
if __name__ =='__main__':
    # Creación de un primer coche
    coche1= Coche('Toyota', 'Yaris','Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean públicos
    #coche1.set_marca('Honda')
    #coche1.set_modelo('Civic')
    #coche1.set_color('rojo')
    coche1.conducir()

    # Atributo de marca del coche 1
    coche1.marca = 'Honda'
    coche1.modelo= 'Civic'
    coche1.color= 'Rojo'
    coche1.conducir()

    # Agregar atributos de manera dinámica
    setattr(coche1,'nuevo_atributo','Valor')
    coche1.nuevo_atributo2 = 'Valor 2'
    print(f'Atributos del coche1: {coche1.__dict__}')
    print(coche1.nuevo_atributo)
    print(coche1.nuevo_atributo2)
    # No se guarda en la clase padre
    # Si se crea un nuevo objeto tiene lo default
    coche2 = Coche('Chevrolet', 'Tracker', 'Azul')
    coche2.conducir()
    print(f'Atributos del coche2: {coche2.__dict__}')

#    print(f'nuevo_atributo coche2 {coche2.nuevo_atributo}')