#Classificação de temperatura
temp = float(input('Digite a temperatura: '))

if temp < 15:
    print('Frio')
elif temp <= 25:
    print('Agradável')
else:
    print('Quente')