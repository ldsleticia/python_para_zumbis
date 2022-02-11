# calcula a Fibonacci do número
num_a = 1
num_b = 1
fib = int(input("Digite um número: "))
while num_a < fib:
    num_a, num_b = num_b, num_a + num_b
print(num_b)

# calcula a posição Fibonacci do número que escrevemos
fib = int(input("Digite um número: "))
a, b = 1, 1
k = 1

while k <= fib - 2:
    a, b = b, a + b
    k = k + 1
print(b)
