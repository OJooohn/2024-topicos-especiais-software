import json

"""
contas_dic = {
    'contas' : [
        {'num':  100, 'nome': 'Maria', 'saldo': 24.93},
        {'num':  200, 'nome': 'Dayane', 'saldo': 33.33},
        {'num':  300, 'nome': 'John', 'saldo': 17.43},
    ]
}


with open('contas.json', 'w') as contas:
    json.dump(contas_dic, contas)
"""

with open('contas.json', 'r') as arquivo:
    contas_json = json.load(arquivo)

    # print(contas_json)
    # print(contas_json['contas'])
    print(contas_json['contas'][0])

    print(json.dumps(contas_json, indent=4))

