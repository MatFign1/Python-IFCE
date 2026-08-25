#Controle de consumo de água
consumo = float(input('Digite o consumo mensal de água em m³: '))

if consumo <= 10:
    valor = 30
elif consumo <= 20:
    valor = 30 + (consumo - 10) * 3
else:
    valor = 60 + (consumo - 20) * 5

print('Valor total da conta: R$', valor)