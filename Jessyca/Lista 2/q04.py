#Controle de Consumo de Água
consumo = float(input("Digite o consumo mensal de água (m³): "))

if consumo <= 10:
    valor_total = 30.0
elif consumo <= 20:
    excedente = consumo - 10
    valor_total = 30.0 + (excedente * 3)
else:
    excedente = consumo - 20
    valor_total = 60.0 + (excedente * 5)

print(f"Valor total da conta: R$ {valor_total:.2f}")