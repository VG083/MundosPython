# Desafio 040: Calcular média
# 	Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com
# a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
m = (n1 + n2 + n3) / 3
if m < 5:
    print(' ')
    print('REPROVADO')
elif m < 7:
    print(' ')
    print('RECUPERAÇÃO')
elif m >= 7:
    print(' ')
    print('APROVADO')