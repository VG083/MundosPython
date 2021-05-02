# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
# n1 é o valor do número
# d é o dobro do número
# t é o triplo do número
# r é a raiz quadrada do número
print('O dobro de {} é {}'.format(n1, d))
print('O triplo de {} é {}'.format(n1, t))
print('A raiz quadrada de {} é {:.2f}'.format(n1, r))
