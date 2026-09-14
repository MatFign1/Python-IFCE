#Controle de Velocidade
velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade <= 80:
    print("Dentro do limite")
elif velocidade <= 100:
    multa = 100
    print("Multa leve")
    print(f"Valor total da multa: R$ {multa:.2f}")
else:
    multa = 300
    print("Multa grave")
    print(f"Valor total da multa: R$ {multa:.2f}")