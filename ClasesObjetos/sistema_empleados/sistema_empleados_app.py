from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print('--- Sistema de empleados ---')

# Crear una instancia de una empresa
empresa1 = Empresa('ADLEXIA')

# Contratar algunos empleados
empresa1.contratar_empleado('Adair','IT')
empresa1.contratar_empleado('Jennifer','IT')
empresa1.contratar_empleado('Bexley','Ventas')
empresa1.contratar_empleado('Jesús','RH')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.contador_empleados}')

# Obtener el número de empleados en el departamento IT
print(f'Empleados en IT:'
      f'{empresa1.buscar_empleado_departamento("IT")}')

# Obtener el número de empleados por empresa
empresa1.obtener_total_empleados()