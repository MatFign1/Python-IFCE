#Contador de tentativas
numero_secreto = 7
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você ainda tem {tentativas} tentativa(s).")

if tentativas == 0:
    print("Suas tentativas acabaram!")