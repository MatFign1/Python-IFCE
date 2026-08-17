#Desconto de Loja
valor = float(input('Digite o valor da compra: '))

if valor > 500:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print('Desconto: ', desconto)
    print('Valor final: ', valor_final)

elif valor >= 200:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print('Desconto: ', desconto)
    print('Valor final: ', valor_final)

else:
    desconto = 0
    valor_final = valor
    print('Nenhum desconto')
    print('Valor final: ', valor_final)