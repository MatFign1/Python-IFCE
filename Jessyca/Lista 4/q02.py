#Senha correta
senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")
    if senha != "python123":
        print("Senha incorreta. Tente novamente.")

print("Acesso concedido!")