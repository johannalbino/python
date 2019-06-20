#!/usr/bin/env python
# -*- coding: utf-8 -*-

from platform import python_version

class gerandoPadrao(object):
    def __init__(self):
        self.nameArquivoFiscal = 'fiscalpadrao.sh'
        self.arquivoFiscal = ['sist/arqv/sp06a62* #Nota Referenciadas',
                 'sist/sped/sp14a56* #Apoio Fiscal',
                 'sist/sped/sp14a42* #Tabela de NCM',
                 'sist/sped/sp14a48* #Tabela de NCM',
                 'sist/sped/sp14a10* #Cadastro de produto Complementar',
                 'sist/arqd/sp01*03* #Dedo duro de produto',
                 'sist/arqf/sp03a13* #Cadastro de CFOP',
                 'sist/arqf/sp03a07* #Valores do livro de apuração']
        self.arquivoParametros = ['arq/* #',
                     'sist/arq/sp01a01* #Parametro da filial',
                     'sist/arq/sp01a00* #Parametro da filial',
                     'sist/arq/sp03a80* #Parametro da filial',
                     'sist/arq/sp01a04* #Ficha Financeira',
                     'sist/arq/sp01a77* #Grupo de preços']
        self.arquvioMateriais = ['arq/* #',
                     'sist/arq/sp01a09* #Pedido de cliente', 
                     'sist/arq/sp01a13* #Pedido de fornecedor', 
                     'sist/arqd/sp01*03* #Dedo duro produto',
                     'sist/arqa/sp01*03* #Arquivo auxiliar de produtos',
                     'sist/arqa/sp01*22* #Arquivo auxiliar de produtos',
                     'sist/arqpd/iv* #arquivos de inventario',
                     'sist/arq/sp01a27* #Cadastro de compradores']
        self.arquivoFinanceiro = ['sist/arq/*  #', 
                     'sist/arqb/*  #', 
                     'sist/arqc/* #']
        self.diretorios = ['sist/sped/*', 'sist/arqf*/', 'sist/arqv/*', 'sist/arqm/*']

    def usuario(self):
        condicao = True

        if int(python_version()[0]) < 3:
            client = input_raw("Qual o cliente ? ")
        
        else:
            client = input("Qual o cliente ? ")

        mes = int(input("Qual o mês de referencia que deseja criar o arquivo ? "))

        #validando o mes informado pelo usuario
        while condicao == True:
            if mes > 12 or mes <=0:
                print ("Mês informado incorreto.\n")
                mes = int(input("Qual o mês de referencia que deseja criar o arquivo ? "))
                condicao = True
            else:
                condicao = False

        ano = int(input("Qual o ano de referencia que deseja criar o arquivo ? (Apenas dois digitos. Ex: 19) "))

        #retornando uma tupla com a i
        return ['base'+client, mes, ano]

    def dir(self, ano, mes):
        self.dir = []
        for i in self.diretorios:
            self.dir.append(i+'%s%s* #' %(ano, mes))
            self.dir.append(i+'%s%s* #' %(mes, ano))

    def gerarArquivoFiscal(self):
        self.dados = self.usuario()

        #tratando o valor inteiro menor que 10 para ter dois digitos e não somente um
        if self.dados[1] < 10 and self.dados[1] > 0:
            self.dados[1] = '0'+str(self.dados[1])
        
        #executando a função para carregar a lista de diretorios + ano + mes
        self.dir(self.dados[2], self.dados[1])
        
        self.arquivoSaida = open(self.nameArquivoFiscal, "w+")
        self.arquivoSaida.writelines('#author: johann albino\n\n\n\n\n\n')
        for i in self.arquivoFiscal, self.arquivoParametros, self.dir:
            for x in i:
                self.arquivoSaida.writelines('rar a '+self.dados[0]+' '+str(x)+'\n')
        self.arquivoSaida.writelines('mv '+self.dados[0]+' /u/rede/avanco/ \n')

        self.arquivoSaida.writelines("#Seu arquivo esta disponivel em /u/rede/avanco/"+self.dados[0]+".rar\n")

        print ("Seu arquivo padrao foi gerado com sucesso!")
        self.arquivoSaida.close()


padrao = gerandoPadrao()

try:
    print ('Bem vindo a geração de arquivo padrão para buscar base no cliente.\n')
    print ('\n')
    print ('Instruções:\n')
    print ('Este programa vai gerar um arquivo no formato .sh e no local onde esta armazenado este programa.\n ')
    print ('Você deve informar qual o setor que você deseja gerar as informações.\n')
    print ('Você deve informar o nome do cliente para gerar o arquivo de dados do cliente com o nome correto.\n')
    print ('Deve informar o mes de referencia que deseja buscar as informações. \n')
    print ('Deve informar o ano de referencia que deseja buscar as informações. \n')
    print ('Após gerar o arquivo .sh deve colocar no servidor no caminho /u e digitar o comando : sh setor+padrao.sh\n')
    print ('Ao terminar a execução do comando no servidor, vai criar um arquivo no formato .rar com o nome base+nomeCliente.rar no local /u\n')

    print ("Deseja criar uma base padrao para qual setor ?\n")
    print ("1 - Fiscal\n2 - Contabil\n3 - Materiais\n4 - Financeiro\n")
    opcao = int(input("Você deseja criar uma arquivo padrao para qual tipo de teste?\n"))
    while True:
        if opcao == 1:
            padrao.gerarArquivoFiscal()
        
        elif opcao == 2:
            pass
        
        elif opcao == 3:
            pass
        
        elif opcao == 4:
            pass   

except NameError as e:
    print (e)