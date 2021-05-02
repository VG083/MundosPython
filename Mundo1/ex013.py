# Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
n1 = float(input('Digite o salário do funcionário: '))
n2 = float(input('Digite a porcentagem do aumento: '))
a1 = n1 / 100
a2 = a1 * n2
v = n1 + a2
# n1 é o salário inicial
# n2 é a porcentagem do aumento que será aplicado
# d1 é o valor de 1% de aumento
# d2 é o valor total de aumento
# v é o salário com aumento aplicado
print('O salário do funcionário com {}% de aumento será R${}'.format(n2, v))
