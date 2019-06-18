#projeto 1
#jogo da velha
#autor = Johann Albino
import random

def tabuleiro(board):

	print ('   |   |   ')
	print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print ('   |   |   ')
	print ('------------')
	print ('   |   |   ')
	print (' ' + board[4]+' | '+board[5]+' | '+board[6])
	print ('   |   |   ')
	print ('------------')
	print ('   |   |   ')
	print (' ' + board[1]+' | '+board[2]+' | '+board[3])
	print ('   |   |   ')

def jogadores():
	input()

	market = ''

	while not (market == 'X' or market == 'O'):
		market = input('Jogador 1: Você quer ser X ou O ? ').upper()

	if market == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def placar(board, market, position):
	board[position] = market

def ganhador(board, market):
	return ((board[9] == market and board[8] == market and board[7] == market) or #ganhando por cima
		(board[4] == market and board[5] == market and board[6] == market) or #ganhando pelo meio
		(board[1] == market and board[2] == market and board[3] == market) or #ganhando por baixo
		(board[7] == market and board[4] == market and board[1] == market) or #ganhando pela esquerda
		(board[8] == market and board[5] == market and board[2] == market) or #ganhando meio
		(board[9] == market and board[6] == market and board[3] == market) or #ganhando pela direita
		(board[7] == market and board[5] == market and board[3] == market) or #ganhando pela diagonal 
		(board[9] == market and board[5] == market and board[1] == market)) #ganhando pela diagonal) 

def primeir():
	if random.randint(0,1) == 0:
		return 'Jogador 2'
	else:
		return 'Jogador 1'

def checagem(board, position):

	return board[position] == ' '

def checar_board(board):
	for i in range(0,10):
		if checagem (board, i):
			return False
	return True

def player_choice(board):
	position = ''

	while position not in '1 2 3 4 5 6 7 8 9'.split() or not checagem(board, int(position)):
		position = input('Escolha sua jogada (1-9) : ')

	return int(position)

def denovo():
	return input('Quer jogar novamente? "SIM" ou "NAO"'.lower().startswith('s'))

print  ('Bem vindo ao jogo da velha!')

while True:

	board = [' '] * 10

	jogador1, jogador2 = jogadores()

	turn = primeir()
	print (turn+' começa!')

	play_on = True

	while play_on:
		#vez do jogador 1
		if turn == 'Jogador 1':
			tabuleiro(board)
			position = player_choice(board)
			placar(board, jogador1, position)

		#checar vitoria
		if ganhador(board, jogador1):
			tabuleiro(board)
			print ('Parabens! Voce venceu!')
			play_on = False
		else:
			if checar_board(board):
				tabuleiro(board)
				print ('Empate')
				break
			else:
				turn = 'Jogador 2'
		# vez do jogador 2
		if turn == 'Jogador 2':
			tabuleiro(board)
			position = player_choice(board)
			placar(board, jogador2, position)

		#checar vitoria
		if ganhador(board, jogador2):
			tabuleiro(board)
			print ('Parabens! Voce venceu!')
			play_on = False
		else:
			if checar_board(board):
				tabuleiro(board)
				print ('Empate')
				break
			else:
				turn = 'Jogador 1'
	if not denovo():
		break
		