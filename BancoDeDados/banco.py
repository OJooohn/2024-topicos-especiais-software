import sqlite3

conexao = sqlite3.connect('meu_banco.db')

cursor = conexao.cursor()

# Criar tabela pessoas
"""
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
''')
"""

# Inserir pessoa na tabela pessoas
"""
cursor.execute('''
    INSERT INTO pessoas (nome, idade) VALUES (?, ?)
''', ('João', 30))
"""

# Criando uma lista de pessoas
""" 
pessoas = [
    ('Dayane', 19),
    ('Eduardo', 20),
    ('John', 20)
]

# Adicionando lista de pessoas usando executemany
cursor.executemany('''
    INSERT INTO pessoas (nome, idade) VALUES (?, ?)
''', pessoas)
"""

# Selecionar pessoas com idade menor que 20
"""
cursor.execute('SELECT * FROM pessoas WHERE idade < 20')
resultado = cursor.fetchall()

# Imprime em forme de lista
# print(resultado)

# Imprimindo pessoas de forma personalizada
for pessoa in resultado:
    # print(pessoa)
    print(f'ID: {pessoa[0]} ')
    print(f'Nome: {pessoa[1]} ')
    print(f'Idade: {pessoa[2]}')
    print('-'*20)
"""

# Alterando um dado de uma pessoa da tabela pessoas
"""
cursor.execute('''
    UPDATE pessoas SET idade = ? WHERE nome = ?
''', (21, 'John'))
"""

# Deletando uma pessoa da tabela pessoas
"""
cursor.execute('''
    DELETE from pessoas WHERE nome = ?
''', ('Eduardo', ))
"""

# conexao.commit()
# pip install pandas
import pandas as pd

query = 'SELECT * FROM pessoas'
tabela = pd.read_sql_query(query, conexao)
print(tabela)

# Fechando a conexão do banco de dados
conexao.close()
