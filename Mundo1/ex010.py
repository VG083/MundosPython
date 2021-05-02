# Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
# Considere: US$1,00 = R$3,27
n1 = float(input('Digite quantos reais você tem na sua carteira: R$'))
n2 = float(input('Digite quanto está a cotação do dólar: '))
v = n1 / n2
# n1 é o total de reais que você tem
# n2 é quanto o dólar está valendo
# v é quantos dólares dá pra você comprar com o dinheiro que tem na carteira
print('Com o seu dinheiro é possível comprar {:.2f} dólares.'.format(v))
