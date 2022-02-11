# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
    if a != b:
        c = a + b
    else:
        c = (a + b) * 2
    return c


print(soma_dobro(1, 1))
