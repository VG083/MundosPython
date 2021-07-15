# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MFmf":
    sexo = str(input("Dado inválido. Informe novamente seu sexo: "))
print("Seu sexo({}) foi registrado.".format(sexo))
