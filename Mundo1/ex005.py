# Desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número: '))
a = n1 - 1
s = n1 + 1
# n1 é o número
# a é o antecessor do número
# s é o sucessor do número
print('O número {} tem como antecessor o número {}'.format(n1, a))
print('O número {} tem como sucessor o número {}'.format(n1, s))
