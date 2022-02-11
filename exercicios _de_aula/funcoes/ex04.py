import random

print(random.randint(1, 100))
nomes = "ana pedro maria antonio".split()
print(random.choice(nomes))
print(random.shuffle(nomes))  # esté retornando none
print(random.sample(range(100), 10))
