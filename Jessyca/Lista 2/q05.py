#Aplicativo de Clima Inteligente
temp = float(input("Digite a temperatura (°C): "))

if temp < 10:
    print("Muito frio! Use um casaco pesado.")
elif temp <= 20:
    print("Fresco, leve um agasalho.")
elif temp <= 30:
    print("Tempo agradável.")
else:
    print("Muito quente! Beba bastante água.")