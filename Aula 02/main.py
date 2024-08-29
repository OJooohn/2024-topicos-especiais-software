# Sequencia
# Tipo de estrutura de dados que armazena uma coleção ordenada de elementos.
# As sequencias permitem que voce acesse seu elemetos individuais usando indices.
# Alem disso as sequencias suportam operaçoes comuns como fatiamento (slice), concatenação e repetição
from Tools.scripts.generate_global_objects import Printer

print('\n>> SEQUÊNCIA SIMPLES')
# Sequencia simples
# Armazenam itens de um tipo de dado

# Exemplo string
nome = 'Dayane'
# A variavel armazena os valores D, a, y, a, n, e, que são do mesmo tipo
for ltr in nome:
    print(ltr, ' ', end='')
print()

print('\n>> SEQUÊNCIA CONTAINER')
# Sequencia container
# Armazenam itens de diferentes tipos

# Exemplo list
list = ['D', 28, 55.1, True]
# Estamos armazenando os ponteiros (referencia) de cada um dos objetos da lista

for obj in list:
    print(obj, ' ', end='')
print()

print('\n>> SEQUÊNCIA MUTÁVEIS')
# Sequencias mutaveis
# Podem ser modificadas após a sua criação
# list, dict, set, byte, array

# Criando a lista
letras = ['A', 'B', 'C']
print('Antes  da modificação:', letras)

# Modificando a lista
letras.append('D')
print('Depois da modificação:', letras)

print('\n>> SEQUÊNCIA IMUTÁVEIS')
# Sequencia imutaveis
# Não podem ser modificadas após a criação
# str, tuple, frozenset

# Criando uma str
nome_2 = 'John'
print(nome_2)
print('Antes  da "alteração":', id(nome_2))

nome_2 += ' Chappell'
print(nome_2)
print('Depois da "alteração":', id(nome_2))

# Neste exemplo, não houve uma alteração, apenas atribuimos a referencia da nova string a variavel nome_2
# Assim a terceira string é criada

# 'John' -> primeira string
# 'Chappell' -> segunda string
# 'John Chappell' -> terceira string
