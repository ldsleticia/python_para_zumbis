# metros_quadrados = int(input("Quantos m2 você vai pintar? "))
# galao_preco = 80
# if metros_quadrados % 6 == 0:
#     galao_ate_aqui = galao_preco
#     galao_ate_aqui = galao_ate_aqui + galao_preco
#     print(f"Você gastará R$ {galao_ate_aqui: .2f}")
# else:
#     print(f'Você gastará R$ {galao_preco: .2f}')

metros_quadrados = int(input("Quantos m2 você vai pintar? "))
lata_preco = 80
lata_quantidade = 1
if metros_quadrados > 54:
    lata_ate_aqui = lata_preco
    lata_ate_aqui = lata_ate_aqui + lata_preco
    lata_quantidade_precisada = lata_quantidade
    lata_quantidade_precisada = lata_quantidade_precisada + lata_quantidade
    print(f'Você precisará de {lata_quantidade_precisada} para pintar {metros_quadrados} m2 e gastará R$ {lata_ate_aqui: .2f}')
else:
    print(f'Você precisará de {lata_quantidade} latas e gastará R$ {lata_preco: .2f}')