class Usuario:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludo(self):
		print("Hola!, mi nombre es", self.nombre, self.apellido)
		
class Admin(Usuario):
	def superSaludo(self):
		print ("Hola", "me llamo", self.nombre, "y soy superUsuario")
usuario = Usuario("Felipe", "Feliz")

usuario.saludo()
usuario.nombre = "Chanchito"
usuario.saludo()
del usuario.nombre

admin = Admin("Super", "Felis")
admin.saludo()
admin.superSaludo()
