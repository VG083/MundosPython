# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
import math
o = float(input('Digite o comprimento do cateto oposto do seu triângulo retângulo: '))
a = float(input('Digite o comprimento do cateto adjacente do seu triângulo retângulo: '))
h2 = math.hypot(o, a)
#h1 = (math.pow(o, 2)) + (math.pow(a, 2))
#h2 = math.sqrt(h1)
print('Um triângulo com cateto oposto de {} e cateto adjacente {} tem uma hipotenusa de {:.2f}'.format(o, a, h2))
