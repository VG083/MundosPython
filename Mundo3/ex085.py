# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 1:
        numeros[1].append(valor)
    else:
        numeros[0].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros ímpares digitados foram: {numeros[1]}')
print(f'Os numeros pares digitados foram: {numeros[0]}')
