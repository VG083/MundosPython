# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
decimo_termo = pt + (10-1) * r
for c in range(pt, decimo_termo + r, r):
    print("{}".format(c), end=" -> ")
print("FIM")
