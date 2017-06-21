from collections import deque
import numpy as np



class Pilha():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])
                


class BSTNode(object):
    def __init__(self, key,nulo,k,final = []):
        self.key = key
        self.nulo = nulo
        self.k = k
        self.final = final
        self.pai = None

    def getNulo(self):
        for i in self.key:
            print(i)
               
def compara(m,m2):
    igual = True
    for w in range(3):
        for k in range(3):
            igual = igual and m2[w][k] == m[w][k]


    return igual            

def comparamatrizes(m,matrizes):
    
    for matriz in matrizes:
        igual = True
        for k in range(3):
            for i in range(3):
                igual = igual and m[k][i] == matriz[k][i]
            
        if(igual):
            return igual

    return igual 

def imaisum(k,no,i,j,fila,matrizes):
    mcopy = np.copy(no.key)
    copia = mcopy[i+1][j]
    mcopy[i+1][j] = 0
    mcopy[i][j] = copia
    if (not comparamatrizes(mcopy,matrizes)):
        novoNo = BSTNode(mcopy,(i+1,j),k+1)
        novoNo.pai = no
        fila.append(novoNo)
        matrizes.append(mcopy)

def imenosum(k,no,i,j,fila,matrizes):
    mcopy = np.copy(no.key)
    copia = mcopy[i-1][j]
    mcopy[i-1][j] = 0
    mcopy[i][j] = copia
    if (not comparamatrizes(mcopy,matrizes)):
        novoNo = BSTNode(mcopy,(i-1,j),k+1)
        novoNo.pai = no
        fila.append(novoNo)
        matrizes.append(mcopy)

def jmaisum(k,no,i,j,fila,matrizes):
    mcopy = np.copy(no.key)
    copia = mcopy[i][j+1]
    mcopy[i][j+1] = 0
    mcopy[i][j] = copia
    if (not comparamatrizes(mcopy,matrizes)):
        novoNo = BSTNode(mcopy,(i,j+1),k+1)
        novoNo.pai = no
        fila.append(novoNo)
        matrizes.append(mcopy)

def jmenosum(k,no,i,j,fila,matrizes):
    mcopy = np.copy(no.key)
    copia = mcopy[i][j-1]
    mcopy[i][j-1] = 0
    mcopy[i][j] = copia
    if (not comparamatrizes(mcopy,matrizes)):
        novoNo = BSTNode(mcopy,(i,j-1),k+1)
        novoNo.pai = no
        fila.append(novoNo)
        matrizes.append(mcopy)


def busca(m,nulo,final):
    arvore = BSTNode(np.copy(m),nulo,0,final)
    fila = deque() 
    fila.append(arvore)
    matrizes = [m]
    custo = 0
    while(fila):
        custo += 1
        no = fila.popleft()
        print(no.key)
        print(no.k)

        k = no.k

        if (compara(no.key,arvore.final)):
            pilha = Pilha()

            while(no):
                pilha.push(no)
                no = no.pai

            while(not pilha.isEmpty()):
                no = pilha.pop()
                print("Movimento: "+ str(no.k))
                print(no.key)

            print("Custo busca : " + str(custo))
            return

        nulo = no.nulo
        if(nulo[0] == 0):
            i = 0
            if(nulo[1] == 0):
                j = 0
                imaisum(k,no,i,j,fila,matrizes)
                jmaisum(k,no,i,j,fila,matrizes)

            elif(nulo[1] == 2):
                j = 2
                
                imaisum(k,no,i,j,fila,matrizes)
                jmenosum(k,no,i,j,fila,matrizes)

            else:
                j = 1
                jmaisum(k,no,i,j,fila,matrizes) 
                jmenosum(k,no,i,j,fila,matrizes)
                imaisum(k,no,i,j,fila,matrizes)     


        elif (nulo[0] == 2 ):
            i = 2
            if(nulo[1] == 0):
                j = 0
                imenosum(k,no,i,j,fila,matrizes)
                jmaisum(k,no,i,j,fila,matrizes)

            elif(nulo[1] == 2):
                j = 2
                imenosum(k,no,i,j,fila,matrizes)
                jmenosum(k,no,i,j,fila,matrizes)

            else:
                j = 1
                imenosum(k,no,i,j,fila,matrizes)
                jmenosum(k,no,i,j,fila,matrizes)
                jmaisum(k,no,i,j,fila,matrizes)    
        else:
            i = 1
            if(nulo[1] == 0):
                j = 0
                jmaisum(k,no,i,j,fila,matrizes)
                imenosum(k,no,i,j,fila,matrizes)
                imaisum(k,no,i,j,fila,matrizes)
                

            elif(nulo[1] == 2):
                j = 2
                imenosum(k,no,i,j,fila,matrizes)
                imaisum(k,no,i,j,fila,matrizes)
                jmenosum(k,no,i,j,fila,matrizes)
            else:
                j = 1
                imenosum(k,no,i,j,fila,matrizes)
                imaisum(k,no,i,j,fila,matrizes)
                jmaisum(k,no,i,j,fila,matrizes)
                jmenosum(k,no,i,j,fila,matrizes)
        

#inicial = np.array([[3,7,8],[5,2,1],[0,4,6]])
#final =  np.array([[1,2,3],[4,5,6],[7,8,0]])

inicial = np.array([[7,2,4],[5,0,6],[8,3,1]])

#final = np.array([[7,2,4],[5,0,6],[8,3,1]])

final = np.array([[5,7,4],[6,3,1],[8,2,0]])


#final =  np.array([[1,2,3],[4,5,6],[7,8,0]])


nulo = []

for i in np.where(inicial == 0):
    nulo.append(int(i))

busca(inicial,nulo,final)

    
