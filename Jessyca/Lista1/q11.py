#Verificação de paridade e sinal
num = int(input('Digite um número: '))

if num > 0 and num % 2 == 0:
    print('Par e positivo')
elif num < 0 and num % 2 == 0:
    print('Par e negativo')
elif num > 0 and num % 2 != 0:
    print('Ímpar e positivo')
elif num < 0 and num % 2 != 0:
    print('Ímpar e negativo')
else:
    print('Zero')