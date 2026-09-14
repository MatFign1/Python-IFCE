#Gerador de sequência personalizada
inicio = int(input("Digite o número inicial: "))
passo = int(input("Digite o passo da sequência: "))

atual = inicio

while atual <= 100:
    print(atual, end=" ")
    atual += passo

print(atual)  # Imprime o valor que ultrapassou 100