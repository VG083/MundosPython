# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
print('Maior e menor número')
print(' ')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
l = [n1, n2, n3]
ll = sorted(l)
print(' ')
print('O menor valor é {}'.format(ll[0]))
print('O maior valor é {}'.format(ll[2]))
