from Biblioteca.libro_cls import Libro


class Biblioteca:

    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self,nombre,autor,genero):
        libro = Libro(nombre,autor,genero)
        self.libros.append(libro)

    def buscar_lib_autor(self, autor):
        print(f'----Autor: {autor}----')
        for libro in self.libros:
            if libro._autor == autor:
                print(f'Libro: {libro._nombre}',end=' ')
                print(f'----Género: {libro.genero}')

    def buscar_lib_genero(self, genero):
        print(f'----Género: {genero}----')
        for libro in self.libros:
            if libro._genero == genero:
                print(f'Libro: {libro._nombre}', end=' ')
                print(f'----Autor: {libro.autor}')

    def buscar_todos(self):
        print(f'----Libros en {self.nombre}----')
        for libro in self.libros:
            print(f'Libro: {libro._nombre}', end=' ')
            print(f'----Autor: {libro.autor}',end=' ')
            print(f'----Género: {libro.genero}')

