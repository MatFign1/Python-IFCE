#Simulador de envio de encomendas
tipo = input("Digite o tipo de entrega (Econômica ou Rápida): ")
peso = float(input('Digite o peso do pacote em kg: '))

if tipo == "Econômica":
    if peso <= 2:
        valor = 10
    elif peso <= 10:
        valor = 20
    else:
        valor = 35

elif tipo == "Rápida":
    if peso <= 2:
        valor = 20
    elif peso <= 10:
        valor = 40
    else:
        valor = 60

else:
    valor = 0
    print('Tipo de entrega inválido.')

if valor > 0:
    print('Valor total a pagar: R$', valor)