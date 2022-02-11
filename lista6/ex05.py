# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
    if falando == True and hora < 7:
        print("Houston we have a problem")
    elif falando == True and hora > 20:
        print("Houston we have a problem")
    else:
        print("Papagaio calado ou cantando na hora certa")
    return falando, hora


papagaio(21, False)
