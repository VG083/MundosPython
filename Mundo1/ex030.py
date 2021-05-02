# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
print('Ímpar ou par?')
print(' ')
n = int(input('Digite um número inteiro: '))
ip = n % 2
if ip == 1:
    print(' ')
    print('O número {} é ímpar.'.format(n))
else:
    print(' ')
    print('O número {} é par.'.format(n))
