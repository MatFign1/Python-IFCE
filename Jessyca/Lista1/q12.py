#Identificação de triângulo
n1 = float(input('Digite o lado 1: '))
n2 = float(input('Digite o lado 2: '))
n3 = float(input('Digite o lado 3: '))

if n1 == n2 and n2 == n3:
    print('Equilátero')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Isósceles')
else:
    print('Escaleno')