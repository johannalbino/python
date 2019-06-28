produto = open("0200.txt", "r")
inventario = open("h010.txt", "r")
arq_saida = open ("inventario.txt", "w+")

list_produto = []   #lista para receber cada linha do arquivo de produtos
list_inventario = [] #lista para receber cada linha do arquivo inventario
for i in produto:
    list_produto.append(i)

for b in inventario:
    list_inventario.append(b)

lmenor = 0 #para saber qual lista é menor para rodar o for 

if len(list_produto) > len(list_inventario): lmenor = list_inventario
else: lmenor = list_produto


for i in range(0, lmenor):
	if list_produto[i].split('|')[2] in list_inventario.split('|')[2]:
		arq_saida.writelines(list_produto[i])