class Bloque:
	def __init__(self, masa, gravedad):
		self.masa = masa
		self.gravedad = gravedad

	def obtener_informacion_bloque(self):
		print("Info: bloque: {}, masa: {}g, gravedad: {}\n".format(
		self.bloque, self.masa, self.gravedad))

class Bloque_mena_hierro(Bloque):
	bloque = "mena_hierro"
	def __init__(self, masa, gravedad):
		super().__init__(masa, gravedad)
		print ("bloque puesto")


class Bloque_mena_oro(Bloque):
	bloque = "mena_oro"
	def __init__(self, masa, gravedad):
		super().__init__(masa, gravedad)
		print ("bloque puesto")

class Bloque_mena_diamante(Bloque):
	bloque = "mena_diamante"
	def __init__(self, masa, gravedad):
		super().__init__(masa, gravedad)
		print ("bloque puesto")


bloque_mena_hierro = Bloque_mena_hierro(15, "no")
bloque_mena_hierro.obtener_informacion_bloque()

bloque_mena_oro = Bloque_mena_oro(70, "no")
bloque_mena_oro.obtener_informacion_bloque()

bloque_mena_diamante = Bloque_mena_diamante(50, "no")
bloque_mena_diamante.obtener_informacion_bloque()
