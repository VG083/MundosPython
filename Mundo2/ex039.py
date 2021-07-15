# Desafio 039: Alistamento militar
# 	Faça um programa que leia o nascimento de um jovem e informe de acordo com sua idade;
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# 	O seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print(' ')
    print('Sua idade é de {} anos'.format(idade))
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    tempo = 18 - idade
    ano = atual + tempo
    print(' ')
    print('Sua idade é de {} anos'.format(idade))
    print('Falta {} anos para o seu alistamento'.format(tempo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    atraso = idade - 18
    ano = atual - atraso
    print(' ')
    print('Sua idade é de {} anos'.format(idade))
    print('Você já devia ter se alistado há {} anos'.format(atraso))
    print('Seu alistamento foi em {}'.format(ano))