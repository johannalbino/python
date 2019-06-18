from collections import Counter

l = [2,2,3,4,3,3,2,1,2,3,2]

lc = Counter(l)

print (lc)
print (type(lc))

t = Counter('dshalkfjslkjflkjfskld')
print(t)

frase = 'Quantas palavras aparecem dentro desta frase? Serão 4 palavras que aparece?'

c = Counter(frase.split())

print (c.most_common(2))

print (c.items())

print (dict(c))



