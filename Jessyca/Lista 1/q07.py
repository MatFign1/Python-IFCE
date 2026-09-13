#Classificação de Temperatura
temp = float(input("Digite a temperatura em graus Celsius: "))

if temp < 15:
    print("Frio")
elif temp <= 25:
    print("Agradável")
else:
    print("Quente")