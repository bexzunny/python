class Libro:
    def __init__(self,nombre,autor,genero):
        self._nombre = nombre
        self._autor = autor
        self._genero = genero

    # Propiedades
    @property
    def nombre(self):
        return self._nombre
    @property
    def autor(self):
        return self._autor
    @property
    def genero(self):
        return self._genero

    #Setters
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @autor.setter
    def autor(self,autor):
        self._autor = autor

    @genero.setter
    def genero(self,genero):
        self._genero = genero
