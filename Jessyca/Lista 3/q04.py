#Diagnóstico de Temperatura Corporal
temp = float(input("Digite a temperatura corporal (°C): "))

if temp < 35:
    print("Hipotermia — procure um médico.")
elif temp <= 37:
    print("Temperatura normal.")
elif temp <= 38:
    print("Febre leve.")
elif temp <= 39.9:
    print("Febre moderada.")
else:
    print("Febre alta — risco à saúde!")