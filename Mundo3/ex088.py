# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
jogos = []
numeros = []
sorteados = []
sorteio = 0
quantidade = int(input('Quantos jogos você deseja criar? '))
for contador in range(0, quantidade):
    while True:
        numero = randint(1,60)
        if numero not in sorteados:
            if numero not in numeros:
                numeros.append(numero)
                sorteados.append(numero)
                sorteio += 1
        if sorteio >= 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    sorteio = 0
print(f'\nForam criados {quantidade} jogos:')
for contador in range(0, quantidade):
    print(f'{contador+1}º jogo: {jogos[contador]}')