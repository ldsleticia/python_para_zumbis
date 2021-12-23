from calendar import isleap

ano = int(input("Digite o ano desejado: "))
if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')