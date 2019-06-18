lista = [-1, 90, 88, 3,2,1]

for i in range(len(lista)):
	menor = i

	for x in range(i+1, len(lista)):
		
		if lista[x] < lista[menor]:
			menor = x

	if lista[i] != lista[menor]:
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux

print (lista)
