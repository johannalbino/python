#buscando dados do banco
#autor: Johann Albino
import conectando_banco as con

#variavel recebendo funcao
colecao = con.conect()

def buscando(busca):
	procurar = colecao.find({'primeiro':busca})
	cont_busca = colecao.count_documents(procurar)
	if proc_cont > 0:
		for i in proc:
			return i[i]	
	else:
		print ("Nenhum registro encontrado!")






#

#print (proc_cont)
