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
    

def compara(m,matrizes):
    for matriz in matrizes:
        igual = True
        for k in range(3):
            for i in range(3):
                igual = igual and m[k][i] == matriz[k][i]
            
        if(igual):
            return igual

    return igual 


#final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # nivel N
#inicial = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]]) # ninel 1
#inicial = np.array([[3, 1, 2], [6, 4, 5], [7, 0, 8]]) # nivel 3
#inicial = np.array([[3, 1, 2], [6, 4, 0], [7, 8, 5]])  # nivel 4
#inicial = np.array([[3, 1, 2], [0, 6, 4], [7, 8, 5]])  # nivel 7
#inicial = np.array([[3, 1, 2], [7, 6, 4], [0, 8, 5]]) # nivel 8
#inicial = np.array([[8, 7, 6], [5, 4, 3], [2, 1, 0]])  # nivel 26
#inicial = np.array([[8, 0, 7], [5, 4, 6], [2, 1, 3]])

inicial = np.array([[7,2,4],[5,0,6],[8,3,1]])

final = np.array([[7,2,4],[5,3,0],[8,1,6]])
#final = np.array([[0,1,2],[3,4,5],[6,7,8]])

no = No(inicial,final)

no.setNulo()
no.setF()

pilha = Pilha()

matrizes = [inicial]

custo = 0
while(True):
	no.movimento()
	for filho in no.filhos.values():
		if (not compara(filho.key,matrizes)):
			custo += 1
			matrizes.append(filho.key)
			pilha.push(filho)

	no = pilha.pop()

	if (pilha.isEmpty()):
		break

	if (no.verifica()):
		break	
		

pilha2 = Pilha()

while(no):
	pilha2.push(no)
	no = no.pai


while(not pilha2.isEmpty()):
	no = pilha2.pop()
	print("Movimento: "+ str(no.nivel))
	print(no.key)


print("Custo de busca: "+ str(custo))    


