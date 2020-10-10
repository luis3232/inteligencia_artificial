import Torres

from collections import deque
from copy import deepcopy
from copy import copy

def remove_filhos(filhos, estados_abertos, fechado):
	for filho in filhos[:]:
		if estados_abertos:
			for estado in estados_abertos:
				if filho.ehIgual(estado):
					filhos.remove(filho)
		if fechado:
			for estado in fechado:
				if filho.ehIgual(estado):
					filhos.remove(filho)
	return filhos
	

def busca_largura():
    print("Usando Busca Largura: ")
    inicio = Torres.torres()
    print ("Estado Inicial:")
    inicio.toString()
    print ("")
    estados_abertos = deque([inicio])
    custo = -1
    fechado = list()
    while estados_abertos:
        X = estados_abertos.popleft()
        custo += 1
        if X.ehEstadoFinal():
            X.custoReal += custo
            return X
        else:
            X.geraAcoes()
            acoes = X.acoesValidas
			#gera filhos de X
            filhos = []
            for acao in acoes:
                Y = deepcopy(X)
                Y.acao(acao)
                filhos.append(Y)
			#coloca X em fechado
            fechado.append(X)
			#descarta os filhos de X se ja estiver aberto ou fechado
            filhos = remove_filhos(filhos, estados_abertos, fechado)
			#coloca os filhos restantes na esquerda do aberto
            estados_abertos.extend(filhos)

def main():
    estado_final = busca_largura()
    print ("Estado Final:")
    estado_final.toString()
    print ("O custo real do estado final foi de %d, com %d passos!" % (estado_final.custoReal, estado_final.custo))
    print ("Os passos feitos foram:")
    print (estado_final.caminho)

if __name__ == '__main__':
	main()

