# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.
lista = list()
pessoa = list()
maiorpeso = menorpeso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(lista) == 0:
        maiorpeso = menorpeso = pessoa[1]
    else:
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = input('Deseja continuar? [s/n] ')
    if continuar in 'Nn':
        break
print(f'\A lista ficou {lista}')
print(f'Foram cadastrados os dados de {len(lista)} pessoas')
print(f'O maior peso cadastrado foi {maiorpeso}kg de ', end='')
for pessoa in lista:
    if pessoa[1] == maiorpeso:
        print(f'{pessoa[0]} ', end='')
print()
print(f'O menor peso cadastrado foi {menorpeso}kg de ', end='')
for pessoa in lista:
    if pessoa[1] == menorpeso:
        print(f'{pessoa[0]} ', end='')
print()