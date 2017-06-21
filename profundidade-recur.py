from collections import deque
import numpy as np

import sys
sys.setrecursionlimit(10 ** 9)

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
    def __init__(self, key, final = []):
        self.key = key
        self.pai = None
        self.achou = False
        self.nivel = 0
        self.custo = 0
        self.final = final


def compara(m,matrizes):
    
    for matriz in matrizes:
        igual = True
        for k in range(3):
            for i in range(3):
                igual = igual and m[k][i] == matriz[k][i]
            
        if(igual):
            return igual

    return igual            



def criaArvore(nulo,m,final):
    minicial = np.copy(m)
    matrizes = [minicial]
    arvore = BSTNode(np.copy(m),final)
    i = -1
    j = -1
    criaArvoreInterno(nulo,m,arvore,arvore,matrizes) 
    return arvore   


def imaisum(m,no,i,j,matrizes,raiz):
    mcopy = np.copy(m)
    copia = mcopy[i+1][j]
    mcopy[i+1][j] = 0
    mcopy[i][j] = copia
    if not compara(mcopy,matrizes):
        matrizes.append(mcopy) 
        novoNo = BSTNode(mcopy)
        novoNo.pai = no
        novoNo.nivel = no.nivel + 1
        criaArvoreInterno((i+1,j),mcopy,novoNo,raiz,matrizes)
          

def imenosum(m,no,i,j,matrizes,raiz):
    mcopy = np.copy(m)
    copia = mcopy[i-1][j]
    mcopy[i-1][j] = 0
    mcopy[i][j] = copia
    if not compara(mcopy,matrizes):
        matrizes.append(mcopy) 
        novoNo = BSTNode(mcopy)
        novoNo.pai = no
        novoNo.nivel = no.nivel + 1
        criaArvoreInterno((i-1,j),mcopy,novoNo,raiz,matrizes)    
    
        

def jmaisum(m,no,i,j,matrizes,raiz):
    mcopy = np.copy(m)
    copia = mcopy[i][j+1]
    mcopy[i][j+1] = 0
    mcopy[i][j] = copia
    if not compara(mcopy,matrizes):
        matrizes.append(mcopy) 
        novoNo = BSTNode(mcopy) 
        novoNo.pai = no
        novoNo.nivel = no.nivel + 1
        criaArvoreInterno((i,j+1),mcopy,novoNo,raiz,matrizes)
    

def jmenosum(m,no,i,j,matrizes,raiz):
    mcopy = np.copy(m)
    copia = mcopy[i][j-1]
    mcopy[i][j-1] = 0
    mcopy[i][j] = copia
    if not compara(mcopy,matrizes):
        matrizes.append(mcopy) 
        novoNo = BSTNode(mcopy)
        novoNo.pai = no
        novoNo.nivel = no.nivel + 1
        criaArvoreInterno((i,j-1),mcopy,novoNo,raiz,matrizes)
       
       


def criaArvoreInterno(nulo,m,no,raiz,matrizes):
    
    if (not raiz.achou):
        raiz.custo += 1
        igual = True
        
        for w in range(3):
            for k in range(3):
                igual = igual and raiz.final[w][k] == m[w][k]

        if(igual):
            raiz.achou = True
            print(m)

            pilha = Pilha()

            while(no):
                pilha.push(no)
                no = no.pai

            while(not pilha.isEmpty()):
                no = pilha.pop()
                print("Movimento: "+ str(no.nivel))
                print(no.key)
            return           
               

        if(nulo[0] == 0):
            i = 0
            if(nulo[1] == 0):
                j = 0
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmaisum(m,no,i,j,matrizes,raiz)       

            elif(nulo[1] == 2):
                j = 2
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    jmenosum(m,no,i,j,matrizes,raiz)

            else:
                j = 1
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmaisum(m,no,i,j,matrizes,raiz)        

        elif (nulo[0] == 2):
            i = 2
            if(nulo[1] == 0):
                j = 0
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmaisum(m,no,i,j,matrizes,raiz)

            elif(nulo[1] == 2):
                j = 2
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmenosum(m,no,i,j,matrizes,raiz)
            else:
                j = 1
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    jmaisum(m,no,i,j,matrizes,raiz)    
        else:
            i = 1
            if(nulo[1] == 0):
                j = 0
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):    
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    jmaisum(m,no,i,j,matrizes,raiz)
        
            elif(nulo[1] == 2):
                j = 2
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    jmenosum(m,no,i,j,matrizes,raiz)   

            else:
                j = 1
                if (not raiz.achou):
                    imenosum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    imaisum(m,no,i,j,matrizes,raiz)
                if (not raiz.achou):
                    jmenosum(m,no,i,j,matrizes,raiz)       
            


inicial = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
'''final = np.array([[1,2,3],[4,5,6],[7, 8, 0]])'''
#final = np.array([[3,1,2],[7,6,4],[0,8,5]])


final = np.array([[5,7,4],[6,3,1],[8,2,0]])


#final = np.array([[1,2,3],[4,5,6],[7,8,0]]) #Indicado

'''inicial = np.array([[3,7,8],[5,2,1],[0,4,6]])
final =  np.array([[0,1,2],[3,4,5],[6,7,8]])
'''

nulo = []

for i in np.where(inicial == 0):
    nulo.append(i)

raiz = criaArvore(nulo,inicial,final)

print("Custo da busca: " + str(raiz.custo))