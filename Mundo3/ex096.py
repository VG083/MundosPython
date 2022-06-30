# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    return largura*comprimento

l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))

print()
print(f'O terreno possui uma área de {area(l, c):.2f}m²')