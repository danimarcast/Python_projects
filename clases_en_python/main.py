from Empleado import Empleado
from Cliente import Cliente

#emp = Empleado('Daniel','Martinez','12345','4141412', 500000)
#cli = Cliente('Stiven', 'Castillo', '341223', '6342523', 'vip1')
personas=[]
def cargar():
    respuesta = input("¿Desea cargar un empleado (si/no)?")
    nombre = input("Ingrese el nombre")
    apellido = input("Ingrese el apellido")
    dni = input("Ingrese el dni")
    telefono = input("Ingrese el telefono")
    if respuesta == "si":
        salario=input("Ingrese el salario")
        emp = Empleado(nombre,apellido,dni,telefono,salario)
        personas.append(emp)
        #print(emp)
    else:
        categoria = input("Ingrese su categoria")
        cli=Cliente(nombre,apellido,dni,telefono,categoria)
        personas.append(cli)
        #print(cli)
cargar()
cargar()
cargar()
cargar()
for persona in personas:
    print(persona)

