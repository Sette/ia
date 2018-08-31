import random, copy,csv
import pandas as pd
import numpy as np

class Perceptron:
	
	def __init__(self):
		self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
		self.iteracoes = iteracoes # número de épocas
		self.limiar = limiar # limiar
		self.pesos = [] # vetor de pesos
	
	def treinar(self):	
		for i in range(self.num_amostra):
			self.pesos.append(random.random())
		num_iteracoes = 0
		while True:
			erro = False 
			for i in range(self.num_amostras):
				u = 0
				for j in range(self.num_amostra):
					u += self.pesos[j] * self.amostras[i][j]
				u = u - self.limiar
				y = self.sinal(u)
				if y != self.saidas[i]:
					erro_aux = self.saidas[i] - y
					for j in range(self.num_amostra ):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
					self.limiar = self.limiar - self.taxa_aprendizado * erro_aux
					erro = True
			num_iteracoes += 1
			if num_iteracoes > self.iteracoes or not erro:
				break
	def testar(self, amostra, classe1, classe2):
		u = 0
		for i in range(self.num_amostra):
			u += self.pesos[i] * amostra[i]
		u = u - self.limiar
		y = self.sinal(u)
		if y == 0:
			print('A amostra pertence a classe %s' % classe2)
		else:
			print('A amostra pertence a classe %s' % classe1)

	def sinal(self, u):
		return 1 if u >= 0 else 0

	def loadAmostras(self,caminho):
		df = pd.read_csv(caminho)
		head = df.head(0)
		atributos = []
		for i in head:
			if (str(i) != "classe"):
				atributos.append(str(i))
		x_df = 	df[atributos]
		y_df = df['classe']
		Xdummies_df = pd.get_dummies(x_df)
		Ydummies_df = y_df
		X = Xdummies_df.values
		Y = Ydummies_df.values
		self.amostras = X
		self.saidas = Y 
		self.num_amostras = len(self.amostras) 
		self.num_amostra = len(self.amostras[0]) 
