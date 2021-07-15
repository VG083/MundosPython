# Desafio 045: Jokenpô
# 	Crie um programa que faça o computador jogar Jokenpô com você
import random
import time
escolha = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print('Jokenpo')
print(' ')
print('0. Pedra')
print('1. Papel')
print('2. Tesoura')
j = int(input('O que você deseja escolher: '))
print(' ')
time.sleep(1)
print('O PC escolheu {}'.format(escolha[pc]))
print('Você escolheu {}'.format(escolha[j]))
print(' ')
if pc == 0:
    if j == 0:
        print('Empate')
    elif j == 1:
        print('Você venceu')
    elif j == 2:
        print('O PC venceu')
    else:
        print('ERROR')
elif pc == 1:
    if j == 0:
        print('O PC venceu')
    elif j == 1:
        print('Empate')
    elif j == 2:
        print('Você venceu')
    else:
        print('ERROR')
elif pc == 2:
    if j == 0:
        print('Você venceu')
    elif j == 1:
        print('O PC venceu')
    elif j == 2:
        print('Empate')
else:
    print('ERROR')