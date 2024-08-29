# simples
# Crie uma string contendo a frase "Eu amo python!", e imprima os objetos da sequencia
from operator import invert

str = "Eu amo phyton!"
for ltr in str:
    print(ltr, ' ', end='')
print()

# Mutável
# Crie uma lista contendo os números de 1 a 5.
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)
lista.remove(2)
print(lista)
lista.reverse()
print(lista)

# Imutável
tupla1 = (10, 11, 12)
tupla2 = (13, 14, 15)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)