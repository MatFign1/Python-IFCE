#Diagnóstico de Temperatura Corporal
temperatura = float(input("Digite sua temperatura corporal: "))

if temperatura < 35:
    print("Hipotermia — procure um médico.")

elif temperatura <= 37:
    print("Temperatura normal.")

elif temperatura <= 38:
    print("Febre leve.")

elif temperatura <= 39.9:
    print("Febre moderada.")

else:
    print("Febre alta — risco à saúde!")