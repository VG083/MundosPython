# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
funcionario = {}
funcionario['nome'] = str(input('Nome do funcionário: '))
funcionario['nascimento'] = int(input('Data de nascimento: '))
funcionario['idade'] = datetime.now().year - funcionario['nascimento']
print(f'A idade de {funcionario["nome"]} é {funcionario["idade"]}')
funcionario['ctps'] = int(input('Número CTPS? (0 se não tiver) '))
print()
if(funcionario['ctps'] != 0 ):
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['aposentadoria'] = funcionario['contratacao'] + 35
    funcionario['idadeaposentadoria'] = funcionario['aposentadoria'] - funcionario['nascimento']
    funcionario['salario'] = float(input('Salário: '))
for k, v in funcionario.items():
    print(f'{k}: {v}')