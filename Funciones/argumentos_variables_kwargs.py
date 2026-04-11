# *args -arguments -tuple
# **kwargs  keyword arguments (key,value) un dict
print('---- Argumentos variables en forma de dict ----')
def superhero(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la función
superhero('spiderman', 'Spider-Sense', edad=17, empresa='Oscorp')
superhero('Ironman','Armadura','Playboy', edad=45)

# Es opcinoal enviar argumentos variables
superhero('Daredevil', instinto = 'Auditivo')
superhero('SHO')