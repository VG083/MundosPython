# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(lista):
    pos = maior = 0
    print(f'Os números analisados foram: ', end='')
    while pos < len(lista):
        print(lista[pos], end=' ')
        if lista[pos] > maior:
            maior = lista[pos]
        pos += 1
    print(f'\nO maior número é: {maior}')
maior([1, 2, 5, 3, 4])