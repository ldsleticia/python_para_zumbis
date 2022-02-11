# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
    dia_semana = True
    feriado = True
    if dia_semana == True and feriado == True:
        print("Você pode ficar dormindo")
    elif dia_semana == True:
        print("Você não pode ficar dormindo")
    elif dia_semana == False:
        print("Você pode ficar dormindo")
    elif feriado == True:
        print("Você pode ficar dormindo")
    elif feriado == False:
        print("Você não pode ficar dormindo")
    return dia_semana, feriado


dormir(True, True)
