import os
from platform import python_version
import json


class GerarDefault(object):

    def __init__(self):
        with open('programas.json') as file:
            self.programas_file = json.load(file)

        with open('names.json') as file:
            self.name_file = json.load(file)

        self.setor = ''
        self.data = []
        self.file_output = ''
        self.mes = 0
        self.ano = 0
        self.client = ''
        self._diretorios = []
        self._programas = []
        # print ("Listas carregadas com sucesso!")

    def validation_input(self, text):
        if int(python_version()[0]) < 3:
            return raw_input(text)
        else:
            return input(text)

    def get_information(self):

        self.valida = False
        self.client = self.validation_input("Qual o nome fantasia do cliente ? ")

        if len(self.client.split()) > 1:
            self.client = self.valida_name(self.client.split())

        self.mes = self.validation_input("Qual o mês de referencia que deseja criar o arquivo ? ")
        self.valida = self.valida_inteiro(self.mes)

        # validando o mes informado pelo usuario
        if self.valida is True:
            self.mes = int(self.mes)
            while self.valida is True and self.mes > 12 or self.mes <= 0:
                print("Mês incorreto.\n")
                self.mes = self.validation_input("Qual o mês de referencia que deseja criar o arquivo ? ")
                self.valida = self.valida_inteiro(self.mes)
                if self.valida is True:
                    self.mes = int(self.mes)

        while self.valida is False:
            print("Mês informado incorreto.\n")
            self.mes = self.validation_input("Qual o mês de referencia que deseja criar o arquivo ? ")
            self.valida = self.valida_inteiro(self.mes)

            if self.valida is True:
                self.mes = int(self.mes)

        self.ano = self.validation_input(
            "Qual o ano de referencia que deseja criar o arquivo ? (Apenas dois digitos. Ex: 19) ")
        self.valida = self.valida_inteiro(self.ano)

        # validando o ano informado pelo usuario
        if self.valida is True and len(str(self.ano)) <= 2:
            self.ano = int(self.ano)

        while self.valida is False or len(str(self.ano)) > 2:
            print("Ano incorreto.\n")
            self.ano = self.validation_input(
                "Qual o ano de referencia que deseja criar o arquivo ? (Apenas dois digitos. Ex: 19) ")
            self.valida = self.valida_inteiro(self.ano)

            if self.valida is True:
                self.ano = int(self.ano)

        # retornando uma lista
        return ['base_' + self.client, self.mes, self.ano]

    def get_directory(self, ano, mes):
        for i in self.programas_file['diretorios']:
            self._diretorios.append(i + f'{ano}{mes}* #')
            self._diretorios.append(i + f'{mes}{ano}* #')
        return self._diretorios

    def valida_name(self, name_base):
        _name_base = ''
        for i in name_base:
            _name_base += i
        return _name_base

    def valida_inteiro(self, inteiro):
        if type(inteiro) != int and inteiro.isdigit() is False:
            return False
        elif type(inteiro) != int and inteiro.isdigit() is True:
            return True

    def gerando_file(self, setor):
        self.data = self.get_information()
        if self.data[1] < 10:
            self.data[1] = '0' + str(self.data[1])

        self.get_directory(self.data[2], self.data[1])

        if setor is 'fiscal':
            self.file_output = open(self.name_file['name_file_fiscal'], "w+")
            self._programas = self.programas_file['programas_fiscal']
        elif setor is 'contabil':
            self.file_output = open(self.name_file['name_file_contabil'], "w+")
            self._programas = self.programas_file['programas_contabeis']
        elif setor is 'materiais':
            self.file_output = open(self.name_file['name_file_materiais'], "w+")
            self._programas = self.programas_file['programas_materiais']
        elif setor is 'financeiro':
            self.file_output = open(self.name_file['name_file_financeiro'], "w+")
            self._programas = self.programas_file['programas_financeiros']

        self.file_output.writelines('#author: Johann Albino\n\n\n\n\n\n\n')
        for i in self._programas, self.programas_file['programas_parametros'], self._diretorios:
            for x in i:
                self.file_output.writelines('rar a ' + self.data[0] + ' ' + str(x) + '\n')
        self.file_output.writelines('mv ' + self.data[0] + '.rar /u/rede/avanco')
        self.file_output.close()

    def view_programas(self, setor):
        self.setor = setor
        if self.setor is 'fiscal':
            _programas = self.programas_file['programas_fiscal']
        elif setor is 'contabil':
            _programas = self.programas_file['programas_contabeis']
        elif setor is 'materiais':
            _programas = self.programas_file['programas_materiais']
        elif setor is 'financeiro':
            _programas = self.programas_file['programas_financeiros']
        for i in _programas, self.programas_file['programas_parametros'], self.programas_file['diretorios']:
            for x in i:
                print(x)
        os.system('pause')