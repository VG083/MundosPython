# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
valores = list()
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
print(f'\nA lista é {valores}')
