import geral

import busca_gulosa
import a_estrela

labirinto = []
labirinto = geral.Alimenta_Labirinto(labirinto)

print("Deseja realizar a busca pelo método de Busca Gulosa(1) ou Busca A(2)?")
s = input()

if(s == '1'):
    print(busca_gulosa.realiza_busca_gulosa(labirinto))
elif(s == '2'):
    print(a_estrela.realiza_busca_A(labirinto))
else: 
    print("Número digitado inválido!")