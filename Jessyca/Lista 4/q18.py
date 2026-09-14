#ATM de moedas
centavos = int(input("Digite o valor do troco em centavos: "))

m25 = m10 = m5 = m1 = 0

while centavos >= 25:
    m25 += 1
    centavos -= 25

while centavos >= 10:
    m10 += 1
    centavos -= 10

while centavos >= 5:
    m5 += 1
    centavos -= 5

while centavos >= 1:
    m1 += 1
    centavos -= 1

print(f"Moedas de 25: {m25}")
print(f"Moedas de 10: {m10}")
print(f"Moedas de 5:  {m5}")
print(f"Moedas de 1:  {m1}")