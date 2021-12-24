num_a = 1
num_b = 1
fib = int(input('Digite um número: '))
while num_a < fib:
    num_a, num_b = num_b, num_a + num_b
print(num_b)