# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia R$0,15 por km rodado
d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos Km foram rodados durante esses {} dias? '.format(d)))
v = (60*d) + (0.15*k)
print('O total a pagar pelo aluguel do carro é de R${}'.format(v))
