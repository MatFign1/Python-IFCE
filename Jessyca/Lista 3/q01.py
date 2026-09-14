#Sistema de Controle de Estacionamento
horas = int(input("Digite o tempo de permanência em horas: "))
dia = input("Digite o dia da semana (ex: segunda, sábado): ").strip().lower()

if horas <= 2:
    valor = 10.0
elif horas <= 5:
    valor = 20.0
else:
    valor = 35.0

if dia in ["sábado", "sabado", "domingo"]:
    valor *= 1.20

print(f"Valor final a pagar: R$ {valor:.2f}")