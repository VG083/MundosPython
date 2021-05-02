# Desafio 011: Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
b = float(input('Digite a largura em metros da sua parede: '))
h = float(input('Digite a altura em metros da sua parede: '))
a = b * h
t = a / 2
# b e h são respectivamente a largura(base) e altura da sua parede
# a é a área da parede
# t é a quantidade de tinta pra pintar a sua parede considerando que 1l pinta 2m² parede
print('É necessário {}l para pintar sua parede de {}m² com dimensão de {}x{}'.format(t, a, b, h))
