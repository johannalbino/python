produto = open("0200.txt", "r")
inventario = open("h010.txt", "r")
arq_saida = open ("inventario.txt", "w+")

list_produto = []   #lista para receber cada linha do arquivo de produtos
list_inventario = [] #lista para receber cada linha do arquivo inventario
it_produtos = []
it_inventario = []

for i in produto:
    list_produto.append(i)

for b in inventario:
    list_inventario.append(b)

lmaior = 0 #para saber qual lista menor para rodar o for

if len(list_produto) < len(list_inventario): 
    lmaior = len(list_inventario)
else: 
    lmaior = len(list_produto)

li = []

for b in range(0,len(list_inventario)):
    li.append(list_inventario[b].split('|')[2])

for i in range(0, lmaior):
    lp = list_produto[i].split('|')[2]
    if lp in li:
        arq_saida.writelines(list_produto[i])
        #arq_saida.close()