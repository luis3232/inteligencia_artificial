import Pilha

class torres:
    def  __init__(torre):
        torre.A = Pilha.pilha()
        torre.B = Pilha.pilha()
        torre.C = Pilha.pilha()
        torre.pilhas = [torre.A, torre.B, torre.C]

        torre.acoes = (
            (0,1), #move A para B
            (0,2), #move A para C
            (1,0), #move B para A
            (1,2), #move B para C
            (2,0), #move C para A
            (2,1)  #move C para B
        )

        torre.caminho = []
        torre.acoesValidas = []
        torre.ultimaAcao = ()
        torre.custoReal = 0
        torre.custo = 0

        torre.estado_inicial()

    def estado_inicial(torre):
        for i in range (torre.A.quantidadeDiscos, 0, -1):
            torre.A.push(i)
        torre.geraAcoes()

    def estado_final(torre):
        estadofinal = Pilha.pilha()
        for i in range (torre.A.quantidadeDiscos, 0, -1):
            estadofinal.push(i)
        return estadofinal

    def geraAcoes(torre):
        acoes = list(torre.acoes)

        for acao in torre.acoes: #Para toda acao existente
            doPino = torre.pilhas[acao[0]]
            paraPino = torre.pilhas[acao[1]]
            if doPino.top(): #Se existir alguma coisa no pilha
                if not paraPino.pushable(doPino.top()): #Se o movimento for invalido
                    acoes.remove(acao) #Remove a acao de acoes validas
            else: #Se nao tiver nada no pilha, remove todas as acoes para o pilha
                acoes.remove(acao)

        if torre.ultimaAcao in acoes: #Remove a ultima acao realizada para evitar loop
            acoes.remove(torre.ultimaAcao)

        torre.acoesValidas = acoes

    def acao(torre, t):
        if t in torre.acoesValidas:
            doPino = torre.pilhas[t[0]]
            paraPino = torre.pilhas[t[1]]
            if doPino.top():
                paraPino.push(doPino.pop())
            torre.ultimaAcao = t
            torre.geraAcoes()
            torre.custo += 1
            torre.custoReal += 1
            torre.caminho.append(t)


    def acaoProximoConsiderandoF(torre, custo, estados_abertos):
        menor_F = 1000000
        index = 0
        menor_index = 1000000

        # procura o que tem menor heuristica e menor custo entre os estados abertos
        for X in estados_abertos:
            noh_F = X.funcaoF(custo)
            if noh_F < menor_F:
                menor_F = noh_F
                menor_index = index
            index += 1

        selected = estados_abertos[menor_index]
        del estados_abertos[menor_index]
        return selected

    def acaoProximoConsiderandoH(torre, estados_abertos):
        menor_F = 1000000
        index = 0
        menor_index = 1000000

        # procura a menor heuristica entre os estados abertos
        for X in estados_abertos:
            noh_F = X.heuristicaH()
            if noh_F < menor_F:
                menor_F = noh_F
                menor_index = index
            index += 1

        selected = estados_abertos[menor_index]
        del estados_abertos[menor_index]
        return selected

    def acaoProximoConsiderandoG(torre, custo, estados_abertos):
        menor_F = 1000000
        index = 0
        menor_index = 1000000

        # procura o menor custo entre os estados abertos
        for X in estados_abertos:
            noh_F = X.custoG(custo)
            if noh_F < menor_F:
                menor_F = noh_F
                menor_index = index
            index += 1

        selected = estados_abertos[menor_index]
        del estados_abertos[menor_index]
        return selected

    def acaoMenorEsquerda(torre):
        doPino = None
        paraPino = None
        
        for pilha in torre.pilhas:
            if pilha.top() == 1:
                doPino = torre.pilhas.index(pilha)
                paraPino = doPino - 1
                if paraPino == -1:
                    paraPino = 2

        torre.acao((doPino, paraPino))

    def acaoUltimoValido(torre):
        torre.acaoMenorEsquerda()
        torre.gerarAcoes()
        acoes = torre.acoesValidas
        
		#remove todas acoes que envolver o primeiro disco
        primeiroPino = None
        for pilha in torre.pilhas:
            if pilhas.top() == 1:
                primeiroPino = torre.pilhas.index(pilha)

        removeTodos = [(primeiroPino,0),(primeiroPino,1),(primeiroPino,2)]
        r = removeTodos

        for acao in r:
            if acao[0] == acao[1]:
                removeTodos.remove(acao)

        for acao in removeTodos:
            if acao in torre.acoesValidas:
                acao.remove(acao)

        if(len(acoes) > 1):
            print ("erro")
        elif torre.acoesValidas:
            torre.move(torre.acoesValidas[0])

    def ehEstadoFinal(torre):
        return torre.pilhas[2].tamanho() == torre.A.quantidadeDiscos

    def ehIgual(torre, t):
        return torre.A.ehIgual(t.A) and torre.B.ehIgual(t.B) and torre.C.ehIgual(t.C)

    def toString(torre):
        for pilha in torre.pilhas:
            if torre.pilhas.index(pilha) == 0: nome = 'A' 
            elif torre.pilhas.index(pilha) == 1: nome = 'B' 
            else: nome = 'C'
            print ("Torre: %s" % nome)
            pilha.imprimePino()

    def funcaoF(torre, custo):
        torre.custoReal = torre.custoG(custo) + torre.heuristicaH()
        return torre.custoReal

    def custoG(torre, custo):
        return custo + 1

    def heuristicaH(torre):
        valor = 0
        torreCorrente = torre.C
        estadofinal = torre.estado_final()
        try:
            for r_index in range(0, torreCorrente.tamanho()):
                if torreCorrente.p[r_index] == estadofinal.p[r_index]:
                    valor -= 1
        except IndexError:
            pass
        return valor



