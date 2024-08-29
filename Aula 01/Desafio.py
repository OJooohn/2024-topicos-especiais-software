frase = input('Digite uma frase: ')

# REMOVER ','
for i in range(len(frase)):
    frase = frase.replace(',', '')
    
palavras = frase.split()
palavras = list(set(palavras))

for i in range (len(palavras)):
    quant = frase.count(palavras[i])
    print(f'{palavras[i]}: {quant}')
    
       
