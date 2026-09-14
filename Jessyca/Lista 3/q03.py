#Simulador de Conta de Energia Residencial
kwh = float(input("Digite o consumo em kWh: "))
tipo = input("Digite o tipo de cliente (residencial, comercial ou industrial): ").strip().lower()

if tipo == "residencial":
    if kwh <= 100:
        total = kwh * 0.50
    else:
        total = kwh * 0.70
    print(f"Valor total da conta: R$ {total:.2f}")
elif tipo == "comercial":
    if kwh <= 500:
        total = kwh * 0.65
    else:
        total = kwh * 0.80
    print(f"Valor total da conta: R$ {total:.2f}")
elif tipo == "industrial":
    if kwh <= 1000:
        total = kwh * 0.75
    else:
        total = kwh * 1.00
    print(f"Valor total da conta: R$ {total:.2f}")
else:
    print("Tipo de cliente inválido.")