print("---- Agenda contactos ----")

agenda = {
    'adair': {
        'telefono': '7731322268',
        'email': 'adair@gmail.com',
        'calle': 'Principal'
    },
    'samantha': {
        'telefono': '7732839576',
        'email': 'lius@gmail.com',
        'calle': 'cerro'
    },
    'maria': {
        'telefono': '7733967740',
        'email': 'maria@gmail.com',
        'calle': 'Calzada'
    }
}

# Acceder a la información de un contacto en específico
print(f"""Información del contacto samantha
Teléfono: {agenda['samantha']['telefono']}
Email: {agenda.get('samantha').get('email')}
Dirección: {agenda['samantha']['calle']}""")

# agregar nuevo contacto
# si la llave (nombre) ya existe
# sólo se actualizarán los datos
agenda['Ana'] = {
    'telefono': '5539948255',
    "email": 'anamari@gmail.com',
    'calle': 'olvidada'
}

# Eliminar un contacto existente
agenda.pop('maria')
#del agenda['maria']
print(agenda)

# Mostramos los contactos de la agenda
print("\n contactos de la agenda")
for nombre,detalle in agenda.items():
    print(f"""Nombmre: {nombre}
Telefono: {detalle['telefono']}
email: {detalle['email']}
Calle: {detalle['calle']}
""")