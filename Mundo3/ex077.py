# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('python', 'javascript', 'ruby', 'perl', 'swift', 'objetive-c', 'go', 'assembly', 'bash', 'lua')

for i in tupla:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')