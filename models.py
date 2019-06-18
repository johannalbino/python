import mongoengine

class usuario(mongoengine.Document):
	primeiro = mongoengine.StringField()
	ultimo = mongoengine.StringField()
	idade = mongoengine.IntField()
	hobby = mongoengine.ListField()
	recomendações = mongoengine.ListField()


