# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# from math import factorial
# n = int(input("Digite um número para calcular seu fatorial: "))
# f = factorial(n)
# print("O fatorial de {} é {}")
n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
while c > 0:
    print("{} ".format(c), end="")
    print("* " if c > 1 else "= ", end="")
    f *= c
    c -= 1
print("{}".format(f))
