#Caixa registradora
total = 0.0
preco = float(input("Digite o preço do produto (0 para finalizar): R$ "))

while preco != 0:
    total += preco
    preco = float(input("Digite o preço do produto (0 para finalizar): R$ "))

print(f"Total da compra: R$ {total:.2f}")