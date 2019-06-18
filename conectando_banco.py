#conectando no banco de dados
#autor: Johann Albino

from pymongo import MongoClient

def conect():
	cliente = MongoClient('mongodb://localhost:27017/')
	banco = cliente.cursoMongoDB
	colecao = banco.usuario
	return colecao