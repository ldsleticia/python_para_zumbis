lado_a = int(input("Digite o lado A: "))
lado_b = int(input("Digite o lado B: "))
lado_c = int(input("Digite o lado C: "))
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    print('é um triangulo')
    if lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
        print("triângulo escaleno")
    elif lado_a == lado_b and lado_a != lado_c or lado_b == lado_c and lado_b != lado_a or lado_c == lado_a and lado_c != lado_b:
        print('triâgulo isóceles')
    else:
        print('triângulo equilatero')
else: 
    print('Não é um  triângulo')