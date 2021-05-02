# Desafio 027: Primeiro e último nome de uma pessoa
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente
n = input('Insira seu nome completo aqui: ')
nc = n.title()
nd = nc.split()
first = nc.split()[0]
last = nc.split()[-1]
print(' ')
print('Primeiro nome: {}'.format(first))
print('Último nome: {}'.format(last))
