# Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2) / 2
# n1 e n2 são suas duas notas
# m é a média de suas duas notas
print('A sua média é {:.1f}'.format(m))
