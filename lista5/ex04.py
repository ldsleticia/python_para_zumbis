""" Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo 
se ele contém o dígito 2 mas não o dígito 7.  Então, na opinião dela, quantos números 
sortudos existem entre 18644 e 33087, incluindo os extremos? Resposta: 7995 """

contador = 0

for i in range(18644, 33088):
    numbers = []
    aux = ''
    aux = str(i)
    is2 = False
    is7 = False
    for s in aux:
        numbers.append(s)
    for c in numbers:
        if c == "2":
            is2 = True
        elif c == "7":
            is7 = True
    if is2 == True and is7 == False:
        contador += 1
print(contador)