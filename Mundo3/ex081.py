# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#  A) Quantos números foram digitados.
#  B) A lista de valores, ordenada de forma decrescente.
#  C) Se o valor 5 foi digitado e está ou não na lista.
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
valores.sort(reverse=True)
print(f'\nFoi digitado {len(valores)} números')
print(f'A lista é {valores}')
if 5 in valores:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')