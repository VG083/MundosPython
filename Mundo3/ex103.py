# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='>desconhecido<', gol=0):
    """
    -> Essa função retorna nome e quantidade de gols de um jogador
    :param nome: Nome do jogador
    :param gol: Quantidade de gols no campeonato
    """
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')

nome = str(input('Nome: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)