#Jogo de adivinhação
import random

numero_secreto = random.randint(1, 100)
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite (1 a 100): "))
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    elif palpite > numero_secreto:
        print("O número secreto é menor!")

print("Parabéns! Você acertou!")