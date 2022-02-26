from Persona import Persona
class Cliente(Persona):
    def __init__(self,nombre, apellido, dni, telefono, categoria):
        super().__init__(nombre, apellido, dni, telefono)
        self.categoria = categoria