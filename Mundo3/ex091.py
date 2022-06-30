# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    '1º jogador':randint(1,6),
    '2º jogador':randint(1,6),
    '3º jogador':randint(1,6),
    '4º jogador':randint(1,6),
}
ranking = []
print('Os valores sorteados foram:')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} marcou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos jogadores:')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} pontos')
