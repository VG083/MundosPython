# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print('Entre 1 e 500 há {} números múltiplos de 3'.format(contador))
print('A soma entre todos os múltiplos de 3 são: {}'.format(soma))
