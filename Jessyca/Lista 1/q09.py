#Maior de Três Números
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a >= b and a >= c:
    print(f"O maior número é {a}")
elif b >= a and b >= c:
    print(f"O maior número é {b}")
else:
    print(f"O maior número é {c}")