#Desconto de Loja
valor = float(input("Digite o valor da compra: R$ "))

if valor > 500:
    desconto = valor * 0.10
    total = valor - desconto
    print(f"Desconto aplicado: 10% (R$ {desconto:.2f})")
    print(f"Valor final: R$ {total:.2f}")
elif valor >= 200:
    desconto = valor * 0.05
    total = valor - desconto
    print(f"Desconto aplicado: 5% (R$ {desconto:.2f})")
    print(f"Valor final: R$ {total:.2f}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Valor final: R$ {valor:.2f}")