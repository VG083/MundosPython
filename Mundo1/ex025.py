# Desafio 025: Procurando uma string dentro de outra
# Crie um  programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome
n = input('Digite aqui um nome: ')
nm = n.title()
nn = nm.find('Silva')
if nn == -1:
    print('{} não contém o nome "Silva".'.format(nm))
else:
    print('{} contém o nome "Silva".'.format(nm))
#print('Seu nome tem Silva? {}'.format('silva' in nm.lower()))
