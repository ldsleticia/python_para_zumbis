soma = 0
n = 0
while True:
    x = int(input("Se você digitar 0 sairá do programa: "))
    if x == 0:
        break
    soma = soma + x
    n = n + 1
print(f"Sua soma é de: {soma}")
print(f"Sua média é de: {soma/n}")
