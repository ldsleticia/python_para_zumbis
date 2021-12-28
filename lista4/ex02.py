import random

sorteio = random.sample(range(100), 20)
print(f'os números sorteados foram {sorteio}')
par = []
impar = []

for x in sorteio:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
print(f'esses números são pares: {par}')
print(f'esses números são impares: {impar}')