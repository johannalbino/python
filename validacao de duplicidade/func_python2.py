# Este programa tem como finalidade comparar os itens do registro 0200 do sped de um arquivo com outro
#author: Johann Allbino 


produto1 = open("0200ant.txt", "r")
produto2 = open("0200atual.txt", "r")
arq_saida = open ("dif0200.txt", "w+")

list_produto1 = []   #lista para receber cada linha dos produtos do registro 0200 anterior
list_produto2 = [] #lista para receber cada linha dos produtos do registro 0200 atual

for i in produto1:
    list_produto1.append(i)
#criando a lista de produtos do arqivo produto1

for b in produto2:
    list_produto2.append(b)
#criando a lista de produtos do arquivo produto2

lmaior = 0 #para saber qual lista menor para rodar o for

#validação de qual lista é maior para a variavel lmaior receber a quantidade de linhas da lista
if len(list_produto1) < len(list_produto2): 
    lmaior = len(list_produto2)
else: 
    lmaior = len(list_produto1)

li = []

for b in range(0,len(list_produto1)):
    li.append(list_produto1[b].split('|')[2])
#Recebendo a lista de códigos internos de produtos do arquivo produto1

for i in range(0, lmaior):
    lp = list_produto2[i].split('|')[2]
    print (lp)
    if lp not in li:
        arq_saida.writelines(list_produto2[i])
#arq_saida.close()