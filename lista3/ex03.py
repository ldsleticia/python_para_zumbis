populacao_a = 80000
populacao_b = 200000
anos = 0
while populacao_a <= populacao_b:
    percentual_a = 3 / 100
    percentual_b = 1.5 / 100
    populacao_a = populacao_a + populacao_a * percentual_a
    populacao_b = populacao_b + populacao_b * percentual_b
    anos = anos + 1
print(anos)
