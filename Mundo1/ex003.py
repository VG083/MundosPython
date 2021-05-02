# Crie um programa que leia dois números e mostre a soma entre eles.
print('Bem vindo, essa é uma  calculadora de soma')
n1=int(input('Digite um número: '))
n2=int(input('Digite mais um número: '))
s=n1+n2
# print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))