jose = "entrou as 6h"  # global


def fatec():
    global jose  # mesmo jose de fora que foi "emprestado"; unico jose
    jose = "entrou as 8h"  # local
    print(jose)


print(jose)
fatec()
print(jose)
