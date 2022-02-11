nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
x = 0
while senha == nome:
    print("Usuário e senha não podem ser iguais")
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
else:
    print("Agora você pode acessar")
