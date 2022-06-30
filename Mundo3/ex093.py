# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
jogos = int(input('Quantas partidas ele jogou? '))
for c in range (0, jogos):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print()
for k,v in jogador.items():
    print(f'{k}: {v}')
print()
print(f'O jogador {jogador["nome"]} jogou {len([jogador["gols"]])}')
print()
for i,v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
