#projeto2
#blackjack
#autor: johann albino
import random

#funçao para exibir as cartas do jogador
def cartas(nPlayer, cartasIniciais):
	print ('Cartas do jogador %s' %nPlayer)
	for i in cartasIniciais:
		print (' _________')
		print ('|         |')
		print ('|   %s    |'%(i))
		print ('|_________|')

def dealer(cartasIniciais):
	pass


class jogadores(object):
	dinheiro = []
	cartasJo = []
	

	def __init__(self, nPlayer, money, cartasIniciais):
		self.nPlayer = list(range(1,nPlayer+1))
		for i in self.nPlayer:
			self.dinheiro.append(money)
			self.cartasJo.append(cartasIniciais)

		#j1, j2, j3, j4 = self.nPlayer

	def apostar(self,jogador,valor):
		self.dinheiro[jogador] = self.dinheiro[jogador] - valor
		return self.dinheiro[jogador]


class jogar(object):
	
	a = []
	b = []
	c = []
	d = []

	def __init__(self):
		pass

	def cartasIniciais(self, baralho, cartainicial, qtdcarta):
		for i in range(0,qtdcarta):
			if random.choice(baralho) not in cartainicial:
				cartainicial.append(random.choice(baralho))
			else:
				random.choice(baralho)
				self.cartainicial.append(random.choice(baralho))
		return cartainicial


	def baralho(self):
		for i in range(1,14):
			self.a.append('a%s' %(i))
			self.b.append('b%s' %(i))
			self.c.append('c%s' %(i))
			self.d.append('d%s' %(i))
		lista = self.a+self.b+self.c+self.d
		return lista

jogo = jogar()
baralho = jogo.baralho()
cartaini = []
qtdcarta = 2

qtdJogadores = int(input("Quantos jogadores ? "))

cartasJogador = jogo.cartasIniciais(baralho, cartaini, qtdcarta)

x = jogadores(qtdJogadores, float(2000.00), tuple(cartasJogador))
#x.dinheiro[1] = x.apostar(x.nPlayer[1], 200)
#print(x.dinheiro[1])
#x.dinheiro[1] = x.apostar(x.nPlayer[1], 200)

#x.dinheiro[1] = x.apostar(x.nPlayer[1], 200)

print (x.nPlayer[0], x.dinheiro[0], ' outro ', x.nPlayer[1], x.dinheiro[1])



print (cartas(x.nPlayer[0], x.cartasJo[0]))