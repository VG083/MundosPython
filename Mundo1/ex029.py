# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
print('Programa de multa')
print('Velocidade limite: 80Km/h')
print(' ')
v = int(input('Digite aqui a velocidade em Km/h que o automóvel estava: '))
if v <= 80:
    print(' ')
    print('O automóvel estava no limite de velocidade!')
else:
    print(' ')
    print('O automóvel estava acima do limite de velocidade e será multado.')
    m = v - 80
    mv = m * 7
    print('O valor da multa será R${},00'.format(mv))
