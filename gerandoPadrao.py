#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from platform import python_version
import json


class GerarDefault(object):

    def __init__(self):
        self.programas_file = {}
        self.name_file = {}
        self.setor = ''

        with open('programas.json') as file:
            self.programas_file = json.load(file)

        with open('names.json') as file:
            self.name_file = json.load(file)

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
        print('#Seu arquivo está disponível na pasta /u/rede/avanco')
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

padrao = GerarDefault()

try:
    while True:
        os.system('cls')
        print('Bem vindo a geração de arquivo padrão para buscar base no cliente.\n')
        print('\n')
        print('Instruções:\n')
        print('Este programa vai gerar um arquivo no formato .sh e no local onde esta armazenado este programa.\n ')
        print('Você deve informar qual o setor que você deseja gerar as informações.\n')
        print('Você deve informar o nome do cliente para gerar o arquivo de dados do cliente com o nome correto.\n')
        print('Deve informar o mes de referencia que deseja buscar as informações. \n')
        print('Deve informar o ano de referencia que deseja buscar as informações. \n')
        print('Após gerar o arquivo .sh deve colocar no servidor no caminho /u e digitar o comando : sh setor+padrao.sh\n')
        print('Ao terminar a execução do comando no servidor, vai criar um arquivo no formato .rar com o nome base+nomeCliente.rar no local /u\n')
        print("Selecione uma opção:\n\n")
        print("1 - Gerar arquivo padrao\n2 - Visualizar programas gerados nos arquivos\n3 - Sair")
        try:
            options_setor = ['fiscal', 'contabil', 'materiais', 'financeiro']
            options = ['gerar', 'visualizar', 'exit']

            op = int(input("Qual a sua opção ? "))

            if op > len(options) or op < 1:
                print("Opção Inválida!\n")
                os.system('pause')

            else:
                if options[op-1] is 'gerar':
                    while True:
                        print("Setores: \n")
                        print("1 - Fiscal\n2 - Contabil\n3 - Materiais\n4 - Financeiro\n5 - Voltar\n")

                        try:
                            opcao = int(input("Deseja criar uma base padrao para qual setor ?\n"))
                            if len(options_setor) >= opcao >= 1:
                                for indice, valor in enumerate(options_setor):
                                    if valor in options_setor[opcao-1]:
                                        padrao.gerando_file(options_setor[indice])
                                        os.system('pause')

                            elif opcao is 5:
                                break

                            elif opcao > len(options_setor) or opcao < len(options_setor) or opcao is str:
                                print("Opção Inválida!\n")
                                os.system('pause')
                        except ValueError as er:
                            print("Opção Inválida!\n")
                            os.system('pause')

                elif options[op-1] is 'visualizar':
                    while True:
                        print("Setores:\n")
                        print("1 - Fiscal\n2 - Contabil\n3 - Materiais\n4 - Financeiro\n5 - Voltar\n")
                        try:
                            opcao = int(input("Deseja criar uma base padrao para qual setor ?\n"))
                            if len(options_setor) >= opcao >= 1:
                                for indice, valor in enumerate(options_setor):
                                    if valor in options_setor[opcao - 1]:
                                        padrao.view_programas(options_setor[indice])
                            elif opcao is 5:
                                break

                            elif opcao > len(options_setor) or opcao < len(options_setor) or opca is str:
                                print("Opção Inválida!\n")
                                os.system('pause')
                        except ValueError as e:
                            print("Opção Inválida!\n")
                            os.system('pause')

                elif options[op-1] is 'exit':
                    exit()
        except ValueError as a:
            print("Opção Inválida!\n")

except NameError as e:
    print(e)
