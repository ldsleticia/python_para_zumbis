n = 0
soma = 0
while n <= 10:
    x = int(input('Digite um número: '))
    soma = soma + x
    n = n + 1
print(f'Média: {soma/10: .1f}')