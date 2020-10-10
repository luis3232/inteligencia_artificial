import labirinto_desenho

class EstadoLabirinto:
    def __init__(self, posicao = [], custo = 0, pai = None, custo_caminho = 0, fn = 0):
        self.pai = pai
        self.fn = fn
        self.custo = custo
        self.posicao = posicao
        self.custo_caminho = custo_caminho
    def obter_fn(self):
        return self.fn
    def obter_custo(self):
        return self.custo

def Distancia_MANHATTAN(x1,y1,x2,y2):
    return (x1-x2) + (y1 - y2)

def Alimenta_Labirinto(labirintoE):
    for linha in labirinto_desenho.desenha_labirinto:

        auxiliar = []

        for coluna in linha:

            if coluna == ' ':
                auxiliar.append(0)
            elif coluna == 'E':
                auxiliar.append(1)
            elif coluna == 'S':
                auxiliar.append(2)
            else:
                auxiliar.append(3)
                
        labirintoE.append(auxiliar)

    return labirintoE

def ArmazenaEnt(ent, labirinto):
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[0])):
            
            if(labirinto[linha][coluna] == 1):
                ent.append(linha)
                ent.append(coluna)
    return ent

def ArmazenaSai(sai, labirinto):
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[0])):
            
            if(labirinto[linha][coluna] == 2):
                sai.append(linha)
                sai.append(coluna)
    return sai