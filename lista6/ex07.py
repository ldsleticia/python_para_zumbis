# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
    if 100 - n <= abs(10):
        return print(True)
    elif 200 - n <= abs(10):
        return print(True)
    else:
        return print(False)

dista10(89)