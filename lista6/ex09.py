# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
    if len(s) <= 1:
        return s
    else:
        start = s[0]
        end = s[-1]
        return end + s[1:-1] + start
print(troca('ab'))