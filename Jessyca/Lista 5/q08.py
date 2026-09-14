#Adivinhação com limite de tentativas
secreto = 37
tentativas = 5

while tentativas > 0:
    palpite = int(input(f"Tentativa ({tentativas} restantes) - Adivinhe o número (1 a 50): "))
    
    if palpite == secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        diferenca = abs(palpite - secreto)
        
        if palpite > secreto:
            dica_tamanho = "menor"
        else:
            dica_tamanho = "maior"
            
        if diferenca <= 5:
            dica_temp = "quente"
        else:
            dica_temp = "frio"
            
        print(f"Errou! O número secreto é {dica_tamanho} que {palpite}. Você está {dica_temp}!")

if tentativas == 0:
    print(f"\nSuas tentativas acabaram! O número secreto era {secreto}.")