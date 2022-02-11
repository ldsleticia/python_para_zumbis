num_a = int(input("Digite um número: "))
num_b = int(input("Digite mais um número: "))
while num_a % num_b != 0:
    num_a, num_b = num_b, num_a % num_b
print(f"mdc = {num_b}")
