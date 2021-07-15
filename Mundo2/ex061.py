# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
t = pt
cont = 1
while cont <= 10:
    print("{} -> ".format(t), end="")
    t += r
    cont += 1
print("FIM")
