from sistema_empleados.empleado import Empleado


class Empresa:

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self,nombre,departamento):
        empleado = Empleado(nombre,departamento)
        self.empleados.append(empleado)

    def buscar_empleado_departamento(self,departamento):
        contador_empleados = 0
        for empleadou in self.empleados:
            if empleadou.departamento == departamento:
                contador_empleados+=1
        return contador_empleados

    def obtener_total_empleados(self):
        print(f'\nTotal de Empleados para la empresa: {self.nombre}')
        for empleado in self.empleados:
            print(f'''Empleado {empleado.id}
        Nombre: {empleado.nombre}
        Departamento: {empleado.departamento}''')