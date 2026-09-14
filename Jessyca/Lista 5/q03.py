#Soma até a meta
meta = float(input("Digite uma meta positiva: "))

while meta <= 0:
    meta = float(input("Meta inválida! Digite uma meta positiva: "))

total = 0.0
quantidade = 0

while total < meta:
    num = float(input("Digite um número: "))
    total += num
    quantidade += 1

print(f"\nMeta alcançada!")
print(f"Total acumulado: {total}")
print(f"Quantidade de valores lidos: {quantidade}")