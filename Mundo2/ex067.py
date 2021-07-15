# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input("Digite um número para saber sua tabuada: "))
    print(" ")
    if (num < 0):
        break
    for c in range(1, 11):
        print("{} * {} = {}".format(num, c, (num*c)))
    print(" ")
