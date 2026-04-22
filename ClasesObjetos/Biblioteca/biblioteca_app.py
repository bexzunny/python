from Biblioteca.biblioteca_cls import Biblioteca

print('---- Biblioteca ----')

biblioteca1 = Biblioteca('ADLEXANDRÍA')
biblioteca1.agregar_libro('El juego de ender','adair','fantasia')
biblioteca1.agregar_libro('La chica del tren','adair','fantasia')
biblioteca1.agregar_libro('Etéreo','jeyn','fantasia')
biblioteca1.agregar_libro('Sempiterno','jeyn','terror')

biblioteca1.buscar_lib_autor('adair')
biblioteca1.buscar_lib_genero('fantasia')
biblioteca1.buscar_todos()