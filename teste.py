"""import random


a = []
b = []
c = []
d = []

def baralho():
	for i in range(1,14):
		a.append('a%s' %(i))
		b.append('b%s' %(i))
		c.append('c%s' %(i))
		d.append('d%s' %(i))

	lista = a+b+c+d
	return lista

def cartasIniciais(baralho, cartainicial, qtdcarta):
	for i in range(0,qtdcarta):
		if random.choice(carta) not in cartainicial:
			cartainicial.append(random.choice(carta))
		else:
			random.choice(carta)
			cartainicial.append(random.choice(carta))
	return cartainicial

carta = baralho()
cartainicial = []
qtdcarta = 2

play = cartasIniciais(carta, cartainicial, qtdcarta)
print(play)"""

# -*- coding:utf-8 -*-

import csv

listaG = []
arquivoSaida = 'teste.csv'

with open('Arquivos_avanco.txt', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='-', quotechar='|')
	for row in spamreader:
		listaG.append([','.join(row)])
		#print (','.join(row))

with open(arquivoSaida, 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Marca', 'Modelo', 'Ano'])
	for i in listaG:
		spamwriter.writerow(i)
