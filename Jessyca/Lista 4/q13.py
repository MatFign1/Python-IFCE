#Controle de estoque
estoque = 50

while estoque > 0:
    input("Pressione Enter para registrar a venda de 1 produto...")
    estoque -= 1
    print(f"Venda registrada. Produtos restantes: {estoque}")

print("Estoque esgotado!")