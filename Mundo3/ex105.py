# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#  - Quantidade de notas
#  - A maior nota
#  - A menor nota
#  - A média da turma
#  - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*n, situacao=False):
    """
    -> Essa função pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    ---> Quantidade de notas
    ---> A maior nota
    ---> A menor nota
    ---> A média da turma
    ---> A situação (opcional)
    :param n: Recebe as notas da turma
    :param situacao: Exibe a situacao da turma
    """
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/len(n)
    if situacao:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'Boa'
        elif dicionario['media'] >= 5:
            dicionario['situacao'] = 'Razoavel'
        else:
            dicionario['situacao'] = 'Ruim'
    return dicionario
        

resp = notas(6, 2.5, 7, 9, situacao=True)
print(resp)