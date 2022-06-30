# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'lista.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar todas as pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do programa'])
    if resposta == 1:
        cabecalho('Listando todas as pessoas cadastradas')
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Cadastrando uma nova pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Fechando programa')
        break
    else:
        print('\033[31mERRO, DIGITE UMA OPÇÃO VÁLIDA\033[m')
sleep(1)