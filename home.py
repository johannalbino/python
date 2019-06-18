#buscando dados do banco
#autor: Johann Albino
import conectando_banco as con

#variavel recebendo funcao
colecao = con.conect()

opcao = int(input("1 - Buscar por um nome\n 2- Adicionar um usuario\n 3 - Deletar um usuario\nEscolha uma opcao: "))

#variavel para armazenar buscas
x = []

if opcao == 1:
	busca = str(input("Digite seu nome:"))
	proc = colecao.find({'primeiro':busca})
	proc_cont = colecao.count_documents({'primeiro':busca})
	
	if proc_cont > 0:
		for i in proc:
			x.append(str(i))
			print (x)	
	else:
		print ("Nenhum registro encontrado!")

elif opcao == 2:
	nome = str(input("\nDigite o nome do usuario:"))
	