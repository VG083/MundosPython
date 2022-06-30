# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
valores = list()
maior = 0
menor = 0
for i in range(0,5):
    valores.append(int(input('Digite um número inteiro: ')))
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
print(f'Sua lista é {valores}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
