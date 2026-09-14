#Conversor de segundos
segundos_totais = int(input("Digite o valor em segundos (>= 0): "))

while segundos_totais < 0:
    segundos_totais = int(input("Valor inválido! Digite um valor em segundos (>= 0): "))

horas = 0
minutos = 0
segundos = segundos_totais

while segundos >= 3600:
    horas += 1
    segundos -= 3600

while segundos >= 60:
    minutos += 1
    segundos -= 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")