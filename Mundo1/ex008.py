# Desafio 008: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
n1 = int(input('Digite um valor: '))
c = n1 * 100
m = n1 * 1000
# n1 é o valor em metro
# c é n1 em centímetros
# m é n1 em milímetros
print('{} metros equivale a {} centímetros.'.format(n1, c))
print('{} metros equivale a {} milímetros.'.format(n1, m))
