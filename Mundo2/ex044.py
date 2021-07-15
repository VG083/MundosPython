# Desafio 044: Gerenciador de pagamentos
# 	Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de
# 	pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros
v = float(input('Digite o valor da compra: R$ '))
print(' ')
print('Métodos de pagamento: ')
print(' ')
print('1. À vista com dinheiro ou cheque (10% de desconto)')
print('2. À vista no cartão(5% de desconto)')
print('3. Parcelado em até 2x no cartão (Valor normal)')
print('4. Parcelado em 3x ou mais no cartão (20% de juros)')
print(' ')
m = int(input('Digite o método de pagamento: '))
if m == 1:
    pdp = v / 100
    d = pdp * 10
    vf = v - d
    print(' ')
    print('A compra vai custar R$ {}'.format(vf))
elif m == 2:
    pdp = v / 100
    d = pdp * 5
    vf = v - d
    print(' ')
    print('A compra vai custar R$ {}'.format(vf))
elif m == 3:
    print(' ')
    print('A compra vai custar R$ {}'.format(v))
elif m == 4:
    pdp = v / 100
    d = pdp * 20
    vf = v + d
    print(' ')
    print('A compra vai custar R$ {}'.format(vf))