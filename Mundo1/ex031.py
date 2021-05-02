# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print('Preço da passagem')
print(' ')
v = int(input('Digite quantos Km você deseja viajar: '))
if v <= 200:
    vt = 0.5 * v
    print(' ')
    print('Sua viagem vai custar R${}'.format(vt))
else:
    tv = 0.45 * v
    print(' ')
    print('Sua viagem vai custar R${}'.format(tv))
