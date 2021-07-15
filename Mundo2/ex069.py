# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if (idade >= 18):
        tot18 += 1
    if (sexo == "M"):
        totH += 1
    if (sexo == "F") and (idade < 20):
        totM20 += 1
    r = " "
    while r not in "SN":
        r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if (r == "N"):
        break
print("Total de pessoal de pessoas com mais de 18 anos: {}".format(tot18))
print("Total de homens cadastrados: {}".format(totH))
print("Total de mulheres com menos de 20 anos: {}".format(totM20))
