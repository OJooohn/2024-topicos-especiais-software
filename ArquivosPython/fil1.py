
while True:
    nome = input('>> Digite o nome do arquivo: ')
    if not nome:
        break

    try:
        arquivo = open(f'{nome}', 'r')

    except FileNotFoundError:
        print('>> Erro - FileNotFoundError')

    else:
        print(arquivo.read())
        break
