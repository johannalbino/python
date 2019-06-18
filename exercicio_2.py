#exercicio dois
#Faça um programa que recebe duas notas digitadas pelo usuario. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado
from statistics import *

nota1 = float(input ("Qual a sua primeira nota ?"))
nota2 = float(input ("Qual a sua segunda nota ?"))

def status(n1, n2):
	#resultado = mean(n1, n2)
	resultado = (n1 + n2) / 2
	return resultado

media = status(nota1, nota2)

print (media)

if float(media) >= 6:
	print ("Você está aprovado!")
else:
	print ("Você foi reprovado!")