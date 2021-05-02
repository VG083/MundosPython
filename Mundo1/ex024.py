# Desafio 024: Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
c = str(input('Digite o nome de uma cidade: '))
cc = c.title()
cd = cc.split()
m = cd[0].find('Santo')
if m == 0:
    print('A cidade "{}" começa com o nome "Santo". '.format(cc))
if m == -1:
    print('A cidade "{}" não começa com o nome "Santo". '.format(cc))
