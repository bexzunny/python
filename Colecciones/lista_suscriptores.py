print("++++ Lista suscriptores ++++")

suscriptores = {'luisa@gmail.com','marcos@gmail.com','helena@gmail.com'}

#Verificar si un nuevo suscriptor ya está en la lista
nuevo_suscriptor= 'marcos@gmail.com'
if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya está en la lista: {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}")

print(f"Lista suscriptores: {suscriptores}")

#Eliminamos un suscriptor
suscriptor_eliminar = 'helena@gmail.com'
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor: {suscriptor_eliminar} ha sido eliminado de la lista")
print(f"Lista de suscriptores: {suscriptores}")

#Verificamos la cantidad de suscriptores
print(f"Cantidad total de suscriptores: {len(suscriptores)}")
# Mostramos totos los suscriptores
print("----suscriptores---")
for suscriptor in suscriptores:
    print(f" - {suscriptor}")