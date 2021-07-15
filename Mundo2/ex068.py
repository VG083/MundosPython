# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Ímpar ou par? [P/I] ")).strip().upper()[0]
    print("Você jogou {} e o computador jogou {}, então o total foi {}".format(jogador, pc, total))
    print("Deu par" if (total%2 == 0) else "Deu par")
    if (tipo == "P"):
        if (total%2 == 0):
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif (tipo == "I"):
        if (total%2 == 1):
            print("Você venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente... ")
print(" ")
print("GAME OVER")
print("Você venceu {} vezes".format(v))
