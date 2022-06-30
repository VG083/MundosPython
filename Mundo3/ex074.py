# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random

tupla = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))

print('\nOs números sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior número foi: {max(tupla)}')
print(f'O menor número foi: {min(tupla)}')