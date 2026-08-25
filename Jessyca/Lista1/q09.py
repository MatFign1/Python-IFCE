#Maior de três números
n1 = float(input('Digite o 1 número: '))
n2 = float(input('Digite o 2 número: '))
n3 = float(input('Digite o 3 número: '))

if n1 >= n2 and n1 >= n3:
    print('O maior é: ', n1)
elif n2 >= n1 and n2 >= n3:
    print('O maior é: ', n2)
else:
    print('O maior é: ', n3)