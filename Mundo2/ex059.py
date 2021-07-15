# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 0
while (op != 5):
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    op = int(input("O que deseja fazer? "))
    if (op==1):
        print("A soma entre {} e {} é de {}".format(n1. n2, (n1+n2)))
    elif (op==2):
        print("A multiplicação entre {} e {} resulta em {}".format(n1, n2, (n1*n2)))
    elif (op==3):
        if (n1>n2):
            print("{} é o maior valor entre {} e {}".format(n1, n1, n2))
        elif (n1<n2):
            print("{} é o maior valor entre {} e {}".format(n2, n1, n2))
        else:
            print("Não há número maior, ambos tem o mesmo valor que é {}".format(n1))
    elif (op==4):
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif (op==5):
        print("Finalizando")
    else:
        print("Opção inválida! Tente outra vez!")
