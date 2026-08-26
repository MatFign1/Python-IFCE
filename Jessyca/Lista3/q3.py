#Simulador de conta de energia residencial
consumo = float(input("Digite o consumo em kWh: "))
tipo = input("Digite o tipo de cliente: ").lower()

if tipo == "residencial":
    if consumo <= 100:
        valor = consumo * 0.50
    else:
        valor = consumo * 0.70

elif tipo == "comercial":
    if consumo <= 500:
        valor = consumo * 0.65
    else:
        valor = consumo * 0.80

elif tipo == "industrial":
    if consumo <= 1000:
        valor = consumo * 0.75
    else:
        valor = consumo * 1.00

print(f"Valor total da conta: R$ {valor:.2f}")