#embaralhar cartas
import random
playing = True
chip_pool = 100

bet = 1

restart_phrase = "Pressione 'd' para jogar novamente ou 'q' para sair."

suits = ('H', 'D', 'C', 'S')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#classe das minhas cartas
class Card(object):
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def grab_suit(self):
		return self.suit

	def grab_rank(self):
		return self.rank

	def draw(self):
		print (self.suit + self.rank)

#classe das minhas mãos
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = False

	def __str__(self):
		hand_comp = ""

		for card in self.cards:
			card_name = card.__str__()
			hand_comp += " " + card_name

		return "The hand has {}".format(hand_comp)

	def card_add(self, card):
		self.cards.append(card)

		if card.rank == 'A':
			self.ace = True

		self.value += card_val[card.rank]

	def calc_val(self):
		if self.ace == True and self.value < 12:
			return self.value + 10

		else:
			return self.value

	def draw(self, hidden):
		if hidden == True and playing == True:
			starting_card = 1
		else:
			starting_card = 0

		for x in range(starting_card, len(self.cards)):
			self.cards[x].draw()


class Deck(object):
	def __init__(self):
		self.deck = []

		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

	def __str__(self):
		deck_comp = ""

		for card in self.deck:
			deck_comp += " " + cards.__str__()
		return "The deck has " + deck_comp

def make_bet():
	global bet
	bet = 0

	print ("Qual quantidade de fichas você gosta de apostar? (Digite todo inteiro por favor)")

	while bet == 0:
		bet_comp = input()
		bet_comp = int(bet_comp)

		if bet_comp > 1 and bet_comp <= chip_pool:
			bet = bet_comp

		else:
			print ("Aposta inválida. Você tem apenas " + str(chip_pool) + " fichas restantes.")

def deal_cards():
	global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

	deck = Deck()
	deck.shuffle()

	make_bet()

	player_hand = Hand()
	dealer_hand = Hand()

	#duas cartas para o jogador
	player_hand.card_add(deck.deal())
	player_hand.card_add(deck.deal())

	#duas cartas para o dealer
	dealer_hand.card_add(deck.deal())
	dealer_hand.card_add(deck.deal())

	result = "Hit ou Stand? Informe 'H' ou 'S' :"

	playing = True
	game_step()

def hit():
	global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

	if playing:
		if player_hand.calc_val() <= 21:
			player_hand.card_add(deck.deal())
		print ('Player hand is %s' %player_hand)

		if player_hand.calc_val() > 21:
			result = "Busted! " + restart_phrase
			chip_pool -= bet
			playing = False

	else:
		result = 'Desculpe, tente novamente!' + restart_phrase

	game_step()


def stand():
	global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

	if playing == False:
		if player_hand.calc_val() > 0:
			result = "Sorry, you can't stand!"

	else:
		while dealer_hand.calc_val() < 17:
			dealer_hand.card_add(deck.deal())

		if dealer_hand.calc_val() > 21:
			result = "Dealer perdeu! Você ganhou! " + restart_phrase
			chip_pool += bet
			playing = False

		elif dealer_hand.calc_val() < player_hand.calc_val():
			result = "Você ganhou! " + restart_phrase
			chip_pool += bet
			playing = False

		elif dealer_hand.calc_val() == player_hand.calc_val():
			result = "Empate " + restart_phrase
			playing = False

		else:
			result = "Dealer ganhou!" + restart_phrase
			chip_pool -= bet
			playing = False

		game_step()


def game_step():
	print ("")
	print ("Player hand is: ")
	player_hand.draw(hidden=False)

	print ("Player hand total is: " + str(player_hand.calc_val()))

	print ("")
	print ("Dealer hand is: ")
	dealer_hand.draw(hidden=False)

	print ("Dealer hand total is: " + str(dealer_hand.calc_val()))

	if playing == False:
		print ("Total de Fichas : "+str(chip_pool))

	print (result)

	player_input()

def game_exit():
	print ("Obrigado por jogar!")
	exit()

def player_input():
	plin = input().lower()

	if plin == 'h':
		hit()

	elif plin == 's':
		stand()

	elif plin == 'd':
		deal_cards()

	elif plin == 'q':
		game_exit()

	else:
		print ("Opção inválida! Informe h, s, d ou q:")
		player_input()

def intro():
	introducao  = "Bem vindo ao BlackJack!"
	print (introducao)


deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()

deal_cards()