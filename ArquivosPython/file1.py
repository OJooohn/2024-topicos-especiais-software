with open('contas.txt', 'w') as contas:
    contas.write('100 Maria 24.93\n')
    contas.write('200 Dayane 33.33\n')
    contas.write('300 John 17.43\n')
    contas.write('400 Thiago 21.45\n')

    print('500 Laura 26.37', file=contas)

def imprimirContas():
    with open('contas.txt', 'r') as contas:
        print(f'{"Número":<10}{"Nome":<10}{"Saldo":>10}')
        print('-'*30)

        for linha in contas:
            # print(linha)
            # print(linha.split())
            # array = linha.split()
            # num = array[0]
            # nome = array[1]
            # saldo = array[2]
            num, nome, saldo = linha.split()
            print(f'{num:<10}{nome:<10}{saldo:>10}')

        print('-'*30)

print('\n>> Antes das modificações')
imprimirContas()

contas = open('contas.txt', 'r')
temp = open('contas_temp.txt', 'w')

with contas, temp:

    for linha in contas:
        num, nome, saldo = linha.split()

        if num == '500':
            novaConta = ' '.join([num, 'Joaozinho', saldo])
            temp.write(novaConta + '\n')
        else:
            temp.write(linha)

import os
os.remove('contas.txt')
os.rename('contas_temp.txt', 'contas.txt')

print('\n>> Após as modificações')
imprimirContas()