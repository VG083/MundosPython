# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
n = random.randint(0, 5)
print('Bem-vindo ao jogo de adivinhação em Python v1.0')
print(' ')
print('A máquina acabou de sortear um número, tente adivinhar '
      'qual foi o número e eu irei dizer se você acertou ou não')
r = int(input('Digite o número que você deseja apostar: '))
print('Processando...')
time.sleep(2)
if r == n:
    print(' ')
    print('Você acertou! Eu estava pensando no número {} mesmo.'.format(n))
else:
    print(' ')
    print('Você errou! Eu estava pensando no número {}'.format(n))
