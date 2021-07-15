# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
n = randint(0, 10)
print("Bem-vindo ao jogo de adivinhação em Python v2.0")
print(" ")
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10")
acertou = False
palpites = 0
while not acertou:
    r = int(input("Seu palpite: "))
    palpites += 1
    if (r == n):
        acertou = True
    else:
        if (r < n):
            print("Mais... Tente outra vez!")
        elif (r > n):
            print("Menos... Tente outra vez!")
print("Parabéns! Você acertou com {} tentativas.".format(palpites))