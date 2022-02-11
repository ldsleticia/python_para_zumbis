import datetime


class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int(delta.days / 365)

    def __str__(self):
        return f"{self.nome}, {self.idade()} anos"


santos = Pessoa("Letícia", datetime.date(1996, 4, 16))
masanori = Pessoa("Fernando", datetime.date(1980, 9, 1))
print(santos.idade())
print(santos)
print(masanori.idade())
print(masanori)
