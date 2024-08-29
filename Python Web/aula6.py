lista = []

for i in range(10):
    lista.append(i)

print(lista)

lista_2 = [num for num in range(10)]
print(lista_2)

lista_3 = [num * 3 for num in range(10)]
print(lista_3)

lista_4 = [num for num in range(22, 4, -2)]
print(lista_4)

pessoas = [
    {'nome': 'João', 'sobrenome': 'Silva'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'John', 'sobrenome': 'Chappell'},
    {'nome': 'Dayane', 'sobrenome': 'Dias'},
    {'nome': 'Eduardo', 'sobrenome': 'Wozniak'},
]

sobrenomes = [pe['sobrenome'] for pe in pessoas]
print(sobrenomes)

nomes = [pe['nome'] for pe in pessoas]
print(nomes)

nomes_2 = [pe['nome'] if 'y' in pe['nome'] else '-' for pe in pessoas]
print(nomes_2)

# Faz mais sentido assim (>.<)
nomes_3 = [pe['nome'] for pe in pessoas if 'y' in pe['nome'] ]
print(nomes_3)

# try:
# tentar

# except:
# erro

# else:
# restante

# finally:
# sempre faz

# except 1:
# erro 1
# except 2:
# erro 2
# else:
# erro "global"

def ordem(item_lista):
    return item_lista['nome']

# ordem(pessoas[1])
pessoas.sort(key = ordem)
print(pessoas)

for pe in pessoas:
    print(pe['nome'])

# lambda (parametro): (return)
pessoas.sort(key = lambda item : item['nome'])

def chamarFuncao(func, *args):
    return func(*args)

def somar(a, b, c):
    return a + b + c

som1 = chamarFuncao(somar, 1, 2, 3)

# lambda (parametros): (return)
som2 = chamarFuncao(lambda a, b, c: a + b + c, 4, 5, 6)