def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mHOUVE UM ERRO NA LEITURA DO ARQUIVO\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome='Desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mHOUVE UM ERRO NA ABERTURA DO ARQUIVO\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHOUVE UM ERRO NA ESCRITA DO ARQUIVO\033[m')
        else:
            print(f'Novo registro de {nome} cadastrado com sucesso')
            a.close()