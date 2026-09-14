#Caça ao tesouro
posicao = 0

while posicao != 10:
    print(f"Posição atual: x = {posicao}")
    movimento = input("Deseja ir para 'frente' ou para 'trás'? ").strip().lower()
    
    if movimento == "frente":
        posicao += 1
    elif movimento == "trás" or movimento == "tras":
        posicao -= 1
    else:
        print("Movimento inválido!")

print("Parabéns! Você chegou à posição 10 e encontrou o tesouro!")