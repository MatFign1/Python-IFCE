#Assistente de Cinema
idade = int(input('Digite sua idade: '))
dia = input('Digite o dia da semana: ')

if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta":
    valor = 20
elif dia == "sexta" or dia == "sábado" or dia == "domingo":
    valor = 30
else:
    valor = 0

if idade < 12:
    valor = valor * 0.5
elif idade > 60:
    valor = valor * 0.3
else:
    valor = valor

print('Valor a pagar: R$', valor)