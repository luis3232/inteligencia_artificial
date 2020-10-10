import geral

from pprint import pprint
from copy import deepcopy

def Movimentar_Busca_A(posicao_atual,sai,labirinto):
    
    lista = []
    
    cima = None
    baixo = None
    
    direita = None
    esquerda = None
    
    custo_pai = posicao_atual.custo_caminho
    
    zero_atual = posicao_atual.posicao[0]
    um_atual = posicao_atual.posicao[1]
    
    if(labirinto[zero_atual][um_atual + 1] == 0 or labirinto[zero_atual][um_atual + 1] == 2):
        
        posicao = [zero_atual,um_atual + 1]
        custo = geral.Distancia_MANHATTAN(posicao[0],posicao[1],sai[0],sai[1])
        
        pai = posicao_atual
        custo_caminho = custo_pai + 1
        fn = custo_caminho + custo
        direita = geral.EstadoLabirinto(posicao,custo,pai,custo_caminho,fn)
        
    if(labirinto[zero_atual -1 ][um_atual] == 0):
        
        posicao = [zero_atual - 1,um_atual]
        custo = geral.Distancia_MANHATTAN(posicao[0],posicao[1],sai[0],sai[1])
 
        pai = posicao_atual
        custo_caminho = custo_pai + 1
        fn = custo_caminho+custo
        cima = geral.EstadoLabirinto(posicao,custo,pai,custo_caminho,fn)
    
    if(labirinto[zero_atual + 1][um_atual] == 0 ):
        
        posicao = [zero_atual + 1,um_atual]
        custo = geral.Distancia_MANHATTAN(posicao[0],posicao[1],sai[0],sai[1])
 
        pai = posicao_atual
        custo_caminho = custo_pai + 1
        fn = custo_caminho+custo
        baixo = geral.EstadoLabirinto(posicao,custo,pai,custo_caminho,fn)
 
    if(um_atual != 0):
        
        if(labirinto[zero_atual][um_atual - 1] == 0):
            
            posicao = [zero_atual,um_atual - 1]
            custo = geral.Distancia_MANHATTAN(posicao[0],posicao[1],sai[0],sai[1])
            
            pai = posicao_atual
            custo_caminho = custo_pai + 1
            
            fn = custo_caminho + custo
            
            esquerda = geral.EstadoLabirinto(posicao,custo,pai,custo_caminho,fn)
        
    if(cima != None):
        lista.append(cima)
    if(baixo != None):
        lista.append(baixo)
        
    if(direita != None):
        lista.append(direita)
    if(esquerda != None):
        lista.append(esquerda)
        
    lista = sorted(lista,key = geral.EstadoLabirinto.obter_fn,reverse = True)   
    
    return lista
            
def realiza_busca_A(labirinto):
    
    ent = []
    sai = []
    
    ent = geral.ArmazenaEnt(ent, labirinto)
    sai = geral.ArmazenaSai(sai, labirinto)
    
    solucao = geral.EstadoLabirinto(sai,0)
    
    hist = []
    
    heur = geral.Distancia_MANHATTAN(ent[0],ent[1],sai[0],sai[1])
    posicao_atual = geral.EstadoLabirinto(ent,heur,None,0,0) 
    
    hist.append(posicao_atual)
    
    Mensagem = ""
    
    novo_movimento = True
    solucao_encontrada = False
    
    front = []
    
    while(solucao_encontrada != True):
        
        movimentos = Movimentar_Busca_A(posicao_atual,sai,labirinto)
        
        for i in range(len(movimentos)):
            
            for j in range(len(hist)):
                if(movimentos[i].posicao == hist[j].posicao):
                    novo_movimento = False
                    break
                    
            if(novo_movimento == True):
                if(movimentos[i].posicao == solucao.posicao):
                    solucao_encontrada = novo_movimento
                    conjunto_solucao=deepcopy(movimentos[i])
                    break
                    
                front.append(movimentos[i])
                hist.append(movimentos[i])
                
            novo_movimento = True
            
        if(solucao_encontrada != True):
            
            if(front != []):
                front = sorted(front,key=geral.EstadoLabirinto.obter_fn,reverse = True)
                posicao_atual = front.pop()
            else:                
                Mensagem = "\nSem mais nenhum caminho disponivel pela busca A!"
                break
        else:
            Mensagem = "\nSolução Encontrada pela busca A! \nCusto do Caminho: " + str(conjunto_solucao.custo_caminho)
            
    return Mensagem