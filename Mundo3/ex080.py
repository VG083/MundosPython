# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()

for i in range(0,5):
    valor = int(input('Digite um número inteiro: '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                break
            posicao += 1

print(f'A lista é {valores}')