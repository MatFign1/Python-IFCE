#Jogo da senha
senha_definida = input("Jogador 1: Defina a senha: ")
tentativas = 0
chute = ""

print("\n" * 20)  # Limpa a tela para esconder a senha do Jogador 2

while chute != senha_definida:
    chute = input("Jogador 2: Tente adivinhar a senha: ")
    tentativas += 1
    if chute != senha_definida:
        print("Senha incorreta!")

print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")