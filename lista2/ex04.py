numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))
numero_c = int(input("Digite o terceiro número: "))
if numero_a > numero_b and numero_a > numero_c:
    print("O primeiro número é maior")
elif numero_b > numero_a and numero_b > numero_c:
    print("O segundo número é maior")
elif numero_a == numero_b and numero_a == numero_c:
    print("Os três números são iguais")
else:
    print("O terceiro número é maior")
