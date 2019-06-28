l = [1,2,3]
l1 = [3, 4,5,6, 1]
lmenor = 0

t = []

if len(l) > len(l1): lmenor = len (l1)

else: lmenor = len(l)

print (lmenor)

for i in range(0, lmenor):
	if l[i] in l1:
		t.append(l[i])

print (t)
#print (len(t))

#print (t)