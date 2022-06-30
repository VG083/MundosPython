# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#  A) Quantas pessoas foram cadastradas
#  B) A média de idade
#  C) Uma lista com as mulheres
#  D) Uma lista de pessoas com idade acima da média
pessoas = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Utilize apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar[S/N]: ')).upper()[0]
        if continua in 'SN':
            break
        print('Erro! Utilize apenas S ou N')
    if continua == 'N':
        break
print()
print(f'A) Foram cadastradas {len(pessoas)} pessoas')
media = soma / len(pessoas)
print(f'B) A média de idade é {media:5.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Pessoas com idade acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')