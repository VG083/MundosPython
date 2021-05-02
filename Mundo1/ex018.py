# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# *Há uma biblioteca disso em algum modúlo(???)
import math
n = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O ângulo de {}º tem seno de {:.2f}'.format(n, s))
print('O ângulo de {}º tem cosseno de {:.2f}'.format(n, c))
print('O ângulo de {}º tem tangente de {:.2f}'.format(n, t))
