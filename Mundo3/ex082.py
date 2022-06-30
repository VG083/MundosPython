# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = list()
par = list()
impar = list()
while True:
    valor = int(input('Digite um número inteiro: '))
    if valor in valores:
        print('O valor já existe na lista')
    else:
        valores.append(valor)
        print('O valor foi adicionado na lista')
    continuar = input('Deseja continuar? [s/n] ')
    if continuar in 'Nn':
        break
valores.sort()
for i, v in enumerate(valores):
    if v%2 == 0:
        par.append(v)
    elif v%2 == 1:
        impar.append(v)
print(f'\nA lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
