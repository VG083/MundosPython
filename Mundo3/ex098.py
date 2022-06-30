# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada
def exibir(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i, end=' ')

def contador(inicio, fim, passo):
    if inicio < fim:
        fim += 1
        exibir(inicio, fim, passo)
    else:
        fim -= 1
        passo -= 2*passo
        exibir(inicio, fim, passo)


print('a) De 1 até 10, de 1 em 1')
contador(1, 10, 1)
print('\n\nb) De 10 até 0, de 2 em 2')
contador(10, 0, 2)
print('\n\nc) Contagem personalizada')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)