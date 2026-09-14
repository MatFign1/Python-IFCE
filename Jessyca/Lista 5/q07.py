#Caixa de estacionamento (cálculo por faixas)
horas = int(input("Digite a quantidade de horas (>= 0): "))

while horas < 0:
    horas = int(input("Entrada inválida! Digite a quantidade de horas (>= 0): "))

if horas == 0:
    valor_total = 0.0
else:
    h = horas
    valor_total = 0.0
    primeira_hora = True

    while h > 0:
        if primeira_hora:
            valor_total += 5.0
            primeira_hora = False
        else:
            valor_total += 3.0
        h -= 1

    if valor_total > 20.0:
        valor_total = 20.0

print(f"Valor final a pagar: R$ {valor_total:.2f}")