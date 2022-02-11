# Primeira forma de resolver o exerício
meses = [
    "janeiro",
    "fevereiro",
    "marco",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
dia, mes, ano = input("Digite uma data dd/mm/aaaa: ").split("/")
print(f"{dia} de {meses[int(mes) - 1]} de {ano}")

""" 
Segunda forma de reolver o exercício

    if mes == "01" or mes == "1":
    mes = meses[0]
    print(dia + " de " + mes + " de " + ano)

if mes == "02" or mes == "2":
    mes = meses[1]
    print(dia + " de " + mes + " de " + ano)

if mes == "03" or mes == "3":
    mes = meses[2]
    print(dia + " de " + mes + " de " + ano)

if mes == "04" or mes == "4":
    mes = meses[3]
    print(dia + " de " + mes + " de " + ano)

if mes == "05" or mes == "5":
    mes = meses[4]
    print(dia + " de " + mes + " de " + ano)

if mes == "06" or mes == "6":
    mes = meses[5]
    print(dia + " de " + mes + " de " + ano)

if mes == "07" or mes == "7":
    mes = meses[6]
    print(dia + " de " + mes + " de " + ano)

if mes == "08" or mes == "8":
    mes = meses[7]
    print(dia + " de " + mes + " de " + ano)

if mes == "09" or mes == "9":
    mes = meses[8]
    print(dia + " de " + mes + " de " + ano)

if mes == "10":
    mes = meses[9]
    print(dia + " de " + mes + " de " + ano)

if mes == "11":
    mes = meses[10]
    print(dia + " de " + mes + " de " + ano)

if mes == "12":
    mes = meses[11]
    print(dia + " de " + mes + " de " + ano) """
