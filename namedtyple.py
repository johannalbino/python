from collections import namedtuple

t = (12, 13, 14)

print (t[0])

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Huskie', name='Sam')

print (sam.age)