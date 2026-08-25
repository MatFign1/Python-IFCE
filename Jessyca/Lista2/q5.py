#Aplicativo de clima inteligente
temp = float(input('Digite a temperatura: '))

if temp < 10:
    print('Muito frio! Use um casaco pesado')
elif temp <= 20:
    print('Fresco, leve um agasalho')
elif temp <= 30:
    print('Tempo agradável')
else:
    print('Muito quente! Beba bastante água.')