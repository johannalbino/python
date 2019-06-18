from mongoengine import connect

connect('cursoMongoDB')

from models import usuario

us = usuario.objects.first()
us.to_json()
us = usuario.objects(primeiro__contains='Bia')

for i in usuario.objects:
	print(usuario.ultimo)