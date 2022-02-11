# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
    if a == 10 or b == 10:
        return print(True)
    elif a + b == 10:
        return print(True)
    else:
        return print(False)


dez(10, 10)
