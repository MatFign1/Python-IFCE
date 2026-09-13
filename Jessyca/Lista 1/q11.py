#Verificação de Paridade e Sinal
num = int(input("Digite um número inteiro diferente de zero: "))

if num % 2 == 0 and num > 0:
    print("Par e positivo")
elif num % 2 == 0 and num < 0:
    print("Par e negativo")
elif num % 2 != 0 and num > 0:
    print("Ímpar e positivo")
elif num % 2 != 0 and num < 0:
    print("Ímpar e negativo")
else:
    print("Zero não possui sinal positivo/negativo")