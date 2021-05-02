# Desafio 023: Separando dígitos de um número
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
# Ex:
# Digite um número: 1834
#
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
n = int(input('Digite um número: '))
n2 = str(n)
print('Analisando o número {}'.format(n))
print(n2)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
