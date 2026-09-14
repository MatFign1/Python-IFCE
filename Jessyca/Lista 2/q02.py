#Assistente de Cinema
idade = int(input("Digite a idade: "))
dia = input("Digite o dia da semana (ex: segunda, sexta, domingo): ").strip().lower()

if dia in ["segunda", "terça", "terca", "quarta", "quinta"]:
    preco_base = 20
else:
    preco_base = 30

if idade < 12:
    valor_final = preco_base * 0.50
elif idade > 60:
    valor_final = preco_base * 0.70
else:
    valor_final = preco_base

print(f"Valor a pagar: R$ {valor_final:.2f}")