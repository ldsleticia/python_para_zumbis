quilo_de_peixe_trazido = int(input("Quantos quilos de peixe você trouxe hoje? "))
if quilo_de_peixe_trazido > 50:
    excesso = quilo_de_peixe_trazido - 50
    multa = excesso * 4.00
    print(
        f"Você trouxe {excesso} kg a mais de peixe e deverá pagar uma multa de R$ {multa: .2f}"
    )
else:
    excesso = 0
    multa = 0
    print(
        f"Você está dentro do padrão exigido, não há o que ser pago em multa ({multa}) e você trouxe ({excesso}) kg a mais"
    )
