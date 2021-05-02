# Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
n1 = float(input('Digite o preço do produto: '))
n2 = float(input('Digite o valor do desconto que será aplicado: '))
d1 = n1 / 100
d2 = n2 * d1
v = n1 - d2
# n1 é o valor total do produto
# n2 é a porcentagem do desconto que será aplicado
# d1 é o valor de 1% de desconto
# d2 é o valor total do desconto
# v é o valor do produto com desconto aplicado
print('O valor do produto com {}% de desconto é de R${}'.format(n2, v))
