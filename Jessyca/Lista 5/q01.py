#Tabuada até N (validação simples)
n = int(input("Digite um número N entre 1 e 10: "))

while n < 1 or n > 10:
    n = int(input("Número inválido! Digite um número N entre 1 e 10: "))

i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1