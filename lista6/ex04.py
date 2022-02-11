# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
    if n < 21:
        c = 21 - n
    else:
        c = (21 - n) * 2
    return abs(c)


print(diff21(19))
print(diff21(25))
