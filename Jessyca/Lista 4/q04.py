#Validação de entrada
numero = int(input("Digite um número entre 1 e 5: "))

while numero < 1 or numero > 5:
    print("Número inválido!")
    numero = int(input("Digite um número entre 1 e 5: "))

print(f"Número válido digitado: {numero}")