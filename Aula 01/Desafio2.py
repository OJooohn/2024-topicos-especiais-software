numerosDigitados = input('Digite os numeros: ')
numerosString = numerosDigitados.split()

numeros = []
for i in range (len(numerosString)):
    numeros.append(int(numerosString[i]))
    
maior = max(numeros)
menor = min(numeros)

numerosOrdenados = sorted(numeros)

soma = 0
par = 0
impar = 0
for i in range (len(numeros)):
    soma += numeros[i]
    if numeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1

media = soma / len(numeros)

print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Números Ordenados: {numerosOrdenados}')
print(f'Quantidade de números pares: {par}')
print(f'Quantidade de números ímpares: {impar}')
