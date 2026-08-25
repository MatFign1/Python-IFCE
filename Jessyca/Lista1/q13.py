#Calculadora Simples
n1 = float(input('Digite o 1 número: '))
n2 = float(input('Digite o 2 número: '))
oper = input('Digite a operação (+, -, *, /): ')

if oper == '+':
    print(n1 + n2)
elif oper == '-':
    print(n1 - n2)
elif oper == '*':
    print(n1 * n2)
elif oper == '/':
    if n2 != 0:
        print(n1 / n2)
    else:
        print('Não é possível dividir por zero')
else:
    print('Operação inválida')