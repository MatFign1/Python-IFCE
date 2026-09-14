#Eco Interativo
texto = ""
while texto != "sair":
    texto = input("Digite algo (ou 'sair' para encerrar): ")
    if texto != "sair":
        print(f"Você digitou: {texto}")