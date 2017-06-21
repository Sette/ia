
import numpy as np



class No:
	def __init__(self,key,final):
		self.pai = None
		self.key = key
		self.custo = 0
		self.f = 0
		self.final = final
		self.movimentos = ["esquerda","direita","baixo","cima"]
		self.nulo = []
		self.filhos = {}
		self.nivel = 0

	def getF(self):
		return self.f	

	def setNulo(self):
		for i in np.where(self.key == 0):
			self.nulo.append(i)
	

	def movimento(self):

		i = int(self.nulo[0])
		j = int(self.nulo[1])
		if (j == 0):
			try:
				self.movimentos.remove("esquerda")
			except ValueError:
				print("Não removeu")	

		if (i == 0):
			try:
				self.movimentos.remove("cima")
			except ValueError:
				print("Não removeu")
		if (i == 2):
			try:
				self.movimentos.remove("baixo")
			except ValueError:
				print("Não removeu")
		if (j == 2):
			try:
				self.movimentos.remove("direita")	
			except ValueError:
				print("Não removeu")


		for movimento in self.movimentos:
			matriz = self.movimentar(movimento)
			no = No(matriz,self.final)
			no.nivel = self.nivel + 1
			no.setNulo()
			no.setF()
			no.pai = self	
			#print("Tem h = " + str(no.custo))	
			#print("Tem f = " + str(no.f))	
			self.filhos[movimento] = no

			'''Teste aquiii'''


	def movimentar(self,movimento):

		i = int(self.nulo[0])
		j = int(self.nulo[1])

		
		mcopy = np.copy(self.key)
		if (movimento == "cima"):
			copia = mcopy[i-1][j]
			mcopy[i-1][j] = 0

		if (movimento == "baixo"):
	   		copia = mcopy[i+1][j]
	   		mcopy[i+1][j] = 0

		if (movimento == "esquerda"):
	   		copia = mcopy[i][j-1]
	   		mcopy[i][j-1] = 0
		
		if (movimento == "direita"):	
	   		copia = mcopy[i][j+1]
	   		mcopy[i][j+1] = 0
	
		mcopy[i][j] = copia
		
		return mcopy

	def verifica(self):
		igual = True
		for w in range(3):
 			for k in range(3):
 				igual = igual and self.final[w][k] == self.key[w][k]
		return igual

	def setF(self):
		self.setH()
		self.f =int(self.custo) + int(self.nivel)
					
	
	def setH(self):
		for i in range(3):
			for j in range(3):
				posicao = []
				if(self.key[i][j] != 0):
					for k in np.where(self.final == self.key[i][j]):
					    posicao.append(k)
					self.custo += abs(posicao[0] - i) + abs(posicao[1] - j)
	