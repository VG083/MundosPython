# Desafio 026: Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e mostre
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
f = input('Digite uma frase aqui: ')
ff = f.lower()
ff1 = ff.count('a')
ff2 = ff.find('a')
ff3 = ff.rfind('a')
print('A letra A aparece {} vezes na frase.'.format(ff1))
print('A primeira letra A apareceu na posição {}'.format(ff2 + 1))
print('A última letra A apareceu na posição {}'.format(ff3 + 1))