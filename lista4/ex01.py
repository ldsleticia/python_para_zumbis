import random
# Fazdendo com sort
""" sorteio = random.sample(range(100), 10)
sorteio_ordenado = sorted(sorteio)
print(sorteio_ordenado)
print(f'O maior número dessa lista de números é {sorteio_ordenado[9]}')
print(f'O menor número dessa lista de números é {sorteio_ordenado[0]}') """

# Fazendo com for
sorteio = random.sample(range(100), 10)
print(sorteio)

for i in range(0, len(sorteio)):    
    for j in range(i+1, len(sorteio)):    
        if(sorteio[i] > sorteio[j]):    
            temp = sorteio[i];    
            sorteio[i] = sorteio[j];    
            sorteio[j] = temp;
print(sorteio)
print(f'O maior número dessa lista de números é {sorteio[9]}')
print(f'O menor número dessa lista de números é {sorteio[0]}')