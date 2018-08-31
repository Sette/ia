
import perceptron as p


def main():
	rede = p.Perceptron(taxa_aprendizado=0.1, iteracoes=1000, limiar=0.6)
	rede.loadAmostras("and.csv")
	rede.treinar()
	#teste = [1,0.5,1,0]
	#rede.testar(teste, 'Sim', 'Não')	
	
	for teste in rede.amostras:
		rede.testar(teste, 'Verdadeiro', 'Falso')
	
if __name__ == "__main__":
	main()