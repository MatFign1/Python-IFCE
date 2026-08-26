#Sistema de controle de estacionamento
horas = int(input('Digite o tempo de permanência em horas: '))
dia = input('Digite o dia da semana: ').lower()

if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta":
    if horas <= 2:
        valor = 10
    elif horas <= 5:
        valor = 20
    else:
        valor = 35

elif dia == "sábado" or dia == "domingo":
    if horas <= 2:
        valor = 10 * 1.20
    elif horas <= 5:
        valor = 20 * 1.20
    else:
        valor = 35 * 1.20

print(f'Valor final: R$ {valor:.2f}')