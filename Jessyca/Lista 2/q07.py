#Simulador de Envio de Encomendas
peso = float(input("Digite o peso do pacote em kg: "))
tipo = input("Digite o tipo de entrega (Econômica ou Rápida): ").strip().lower()

if tipo in ["econômica", "economica"]:
    if peso <= 2:
        frete = 10.0
    elif peso <= 10:
        frete = 20.0
    else:
        frete = 35.0
    print(f"Valor do frete: R$ {frete:.2f}")
elif tipo in ["rápida", "rapida"]:
    if peso <= 2:
        frete = 20.0
    elif peso <= 10:
        frete = 40.0
    else:
        frete = 60.0
    print(f"Valor do frete: R$ {frete:.2f}")
else:
    print("Tipo de entrega inválido.")