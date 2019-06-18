print (hex(10)) #convertendo em hexadecimail

print (bin(123)) #convertendo em binario

print (pow(4,2)) #pow é a função elevada

print (round(3.8)) #Arredondamento de numero

print (round(3.1415, 3))

#string avançados

s = 'hello word'

print (s.capitalize())

print (s.upper())

print (s.lower())

print (s.count('o'))

print (s.find('o'))

print (s[4])

s = 'hello'

print (s.isalnum())

print (s.isalpha())

print (s.isupper())

print (s.endswith('o'))


print (s.split('e'))

print (s.partition('e'))

print (s)

#conjuntos/sets avançados

s = set()

s.add(1)

print(s)

s.add(2)

print (s)

s.clear()

print (s)

s = {1, 2, 3}

sc = s.copy()

print (sc)

s.add(4)

print (s.difference(sc))

s1 = {1, 2, 3}
s2 = {1, 4, 5}

s1.difference_update(s2)

print (s1)

s1.discard(2)

print (s1)

s1 = {1, 2, 3}
s2 = {1, 4, 5}

print (s1.intersection(s2))

s1.intersection_update(s2)

print (s1)

s1 = {1, 2, 3}
s2 = {1, 4, 5}

print(s1.union(s2))


#dicionarios avançados

x = {x:x**2 for x in range(10)}

print (x)

d = {'k1' : 1, 'k2' : 2}

print (d)

for k in d.keys():
	print (k)

for x in d.values():
	print (x)

for u in d.items():
	print (u)


#listas avançadas 
l = [1, 2, 3]

print (l)

l.append(4)

print (l)

print (l.count(2))

l.extend([1,2,3])

print (l)

print (l.index(3))

l.insert(2, 55)

print (l)

l.pop()

print (l)

l.remove(1)

print (l)

l.reverse()

print (l)

l.sort()

print (l)