# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome: '))
    jogos = int(input('Quantas partidas ele jogou? '))
    for c in range (0, jogos):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar[S/N]: ')).upper()[0]
        if continua in 'SN':
            break
        print('Erro! Utilize apenas S ou N')
    if continua == 'N':
        break
print()
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print()
for k,v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 interrompe]: '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Não existe jogador {busca}')
    else:
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print()