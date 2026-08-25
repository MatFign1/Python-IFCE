#Controle de velocidade
velocidade = float(input('Digite a velocidade do carro: '))

if velocidade <= 80:
    print('Dentro do limite.')
elif velocidade <= 100:
    print('Multa leve')
    print("Valor da multa: R$ 100")
else:
    print('Multa grave')
    print('Valor da multa: R$ 300')