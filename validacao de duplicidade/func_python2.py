# Este programa tem como finalidade comparar os itens do registro 0200 do sped de um arquivo com outro
#author: Johann Allbino 


inventario = open("inventario.txt", "r")
produto = open("0200_0519.txt", "r")
arq_saida = open ("inventariodif.txt", "w+")

list_produto = []   #lista para receber cada linha do arquivo de produtos
list_inventario = [] #lista para receber cada linha do arquivo inventario
it_produtos = []
it_inventario = []
for i in inventario:
    list_inventario.append(i)

for b in produto:
    list_produto.append(b)

lmaior = 0 #para saber qual lista menor para rodar o for

print (len(list_produto), len(list_inventario))

if len(list_produto) < len(list_inventario): 
    lmaior = len(list_inventario)
else: 
    lmaior = len(list_produto)

li = []

for b in range(0,len(list_produto)):
    li.append(list_produto[b].split('|')[2])

for i in range(0, lmaior):
    lp = list_inventario[i].split('|')[2]
    print (lp)
    if lp not in li:
        arq_saida.writelines(list_inventario[i])
#arq_saida.close()