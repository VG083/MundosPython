# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
t = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(t), end="")
        t += r
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))