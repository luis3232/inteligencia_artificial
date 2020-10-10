class pilha:
	def  __init__(pilha):
		pilha.p = []
		pilha.quantidadeDiscos = 4

	def push(pilha, t):
		if(pilha.pushable(t)):
			pilha.p.append(t)
			return True
		else:
			return False
			
	def pop(pilha):
		return pilha.p.pop()
		
	def top(pilha):
		if pilha.p:
			return pilha.p[-1]
		
	def remove(pilha):
		pilha.p.pop(0)
		
	def ehVazio(pilha):
		return (len(pilha.p) == 0)
		
	def imprimePino(pilha):
		print (pilha.p)
		
	def ehCheio(pilha):
		return (len(pilha.p) >= pilha.quantidadeDiscos)
		
	def pushable(pilha, t):
		if (pilha.ehCheio()):
			return False
		else:
			return pilha.ehVazio() or t < pilha.top()
			
	def tamanho(pilha):
		return len(pilha.p)	

	def ehIgual(pilha, pinoAux):
		return pilha.p == pinoAux.p




		
