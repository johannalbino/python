#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from platform import python_version
import json
from gerar_default_cl import GerarDefault as classe_gerar

padrao = classe_gerar()

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
