from No import *


class Pilha():
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return (self.items == [])
				



final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # nivel 0
#inicial = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]]) # ninel 1
#inicial = np.array([[3, 1, 2], [6, 4, 5], [7, 0, 8]]) # nivel 3
#inicial = np.array([[3, 1, 2], [6, 4, 0], [7, 8, 5]])  # nivel 4
#inicial = np.array([[3, 1, 2], [0, 6, 4], [7, 8, 5]])  # nivel 7
#inicial = np.array([[3, 1, 2], [7, 6, 4], [0, 8, 5]]) # nivel 8
#inicial = np.array([[8, 7, 6], [5, 4, 3], [2, 1, 0]])  # nivel 26
#inicial = np.array([[8, 0, 7], [5, 4, 6], [2, 1, 3]])




inicial = np.array([[7,2,4],[5,0,6],[8,3,1]])

#final = np.array([[7,2,4],[5,3,0],[8,1,6]])
#final = np.array([[0,1,2],[3,4,5],[6,7,8]])
no = No(inicial,final)

no.setNulo()
no.setF()
no.movimento()

lista = []

custo = 0
while(True):
	no.movimento()
	for filho in no.filhos.values():
		custo += 1
		lista.append(filho)
	lista = sorted(lista,key = No.getF)
	no = lista[0]
	lista.remove(lista[0])
	if (not lista):
		break
	if (no.verifica()):
		menor = no
		if (lista[0].getF() > menor.getF()):
			break	
		
no = menor

pilha = Pilha()

while(no):
	pilha.push(no)
	no = no.pai


while(not pilha.isEmpty()):
	no = pilha.pop()
	print("Movimento: "+ str(no.nivel))
	print(no.key)


print("Custo de busca: "+ str(custo))