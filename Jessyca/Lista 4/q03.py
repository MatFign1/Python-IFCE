#Soma de números
soma = 0
numero = float(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    numero = float(input("Digite um número (0 para sair): "))

print(f"A soma total é: {soma}")