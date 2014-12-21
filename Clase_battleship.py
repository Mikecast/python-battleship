	
#-*- coding: UTF-8 -*-
class battleship(object):
	"""docstring for battleship"""

	def __init__(self):
		super(battleship, self).__init__()
		self.tablerop1 = [] 
		self.tablerop2 = []
		self.nombrep1 = ""
		self.nombrep2 = ""
		self.dificultad = 3
		self.dimension = 0
		self.barcos = 0
		self.coordenadasp1 = []
		self.coordenadasp2 = []
		self.turno = True
		self.vidas = 0
		self.vidasp1 = 0
		self.vidasp2 = 0

	def establecer_dificultad(self):
		if self.dificultad == 1:
			self.dimension = 5
			self.barcos = 2
			self.vidas = 3
			self.vidasp1 = 3
			self.vidasp2 = 3
		if self.dificultad == 2:
			self.dimension = 10
			self.barcos = 4
			self.vidas = 5
			self.vidasp1 = 5
			self.vidasp2 = 5
		if self.dificultad == 3:
			self.dimension = 15
			self.barcos = 6
			self.vidas = 8
			self.vidasp1 = 8
			self.vidasp2 = 8
		self.colocar_barcos()
		self.ataque()

	def colocar_barcos(self):
		for num_barco in range(1,self.barcos + 1):
			x = raw_input("Ingrese la posición de su barco: " + str(num_barco))
			self.coordenadasp1.append(x)

	def ataque(self):
		pos_ataque = raw_input("Ingrese la posicion a atacar: ")
		if pos_ataque in self.coordenadasp1:
			print "GANO"
		else:
			print "Perdio"
			self.perder_vidas()

	def perder_vidas(self):
		self.vidasp1 = self.vidasp1 - 1
		if self.vidasp1 <= 0:
			print "GAME OVER"
		else:
			print "Tienes", self.vidasp1, " Vidas."


	def turno(self):
		self.turno = not(self.turno)

	def dibujar(self):
		linea = str('!')
		for FILA in range(0, self.dimension):
			for columna in range (0,self.dimension):
				linea= linea + ' ☺ !'	
		print linea
		linea = str('!')





nuevo = battleship()
nuevo.establecer_dificultad()






























