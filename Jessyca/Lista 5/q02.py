#Contagem crescente ou decrescente
ini = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

if ini < fim:
    atual = ini
    while atual <= fim:
        print(atual, end=" ")
        atual += 1
    print()
else:
    atual = ini
    while atual >= fim:
        print(atual, end=" ")
        atual -= 1
    print()