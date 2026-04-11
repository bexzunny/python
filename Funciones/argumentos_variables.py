print(f'Argumentos variables')

# en vez de args su puede poner otra palabra
def superheroe_superpoderes(superhero,nombre,*args):
    print(f'Superhero: {superhero} - {nombre} -{args}')
    # Iterar los superpoderes
    for superpower in args:
        print(f'\t superpoder: {superpower}')
# Llamar la función
superheroe_superpoderes('Spiderman','Peter Parker', 'spider-sense','spider-web')
superheroe_superpoderes('Iron man', 'Tony Stark','Playboy', 'Millonario')

# Es opcional enviar argumentos varialbes
superheroe_superpoderes('DareDevil', 'Matt')