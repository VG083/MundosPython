# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
dados = []
notas = []
quantidade = 0
while True:
    dados.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    dados.append((notas[0]+notas[1])/2)
    alunos.append(dados[:])
    dados.clear()
    notas.clear()
    quantidade += 1
    continuar = input('Deseja continuar? [s/n] ')
    if continuar in 'Nn':
        break
print()
for contador in range (0, quantidade):
    print(f'{contador+1}º aluno:')
    print(f'  Nome: {alunos[contador][0]}')
    print(f'  Média: {alunos[contador][2]}')
print()
while True:
    continuar = input('Deseja saber a nota de algum aluno? [s/n] ')
    if continuar in 'Nn':
        break
    aluno = int(input('De qual aluno deseja saber a nota? '))
    print(f'O aluno {alunos[aluno-1][0]} tirou as notas: {alunos[aluno-1][1]}\n')