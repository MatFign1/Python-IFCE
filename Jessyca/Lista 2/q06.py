#Classificação de Crédito
renda = float(input("Digite a renda mensal: R$ "))
idade = int(input("Digite a idade: "))

if renda < 2000:
    print("Crédito negado")
elif renda <= 5000:
    if idade < 25:
        print("Crédito limitado")
    else:
        print("Crédito padrão")
else:
    print("Crédito premium")