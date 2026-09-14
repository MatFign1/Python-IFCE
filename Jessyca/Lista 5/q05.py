#Par ou ímpar acumulado
qtd_pares = 0
qtd_impares = 0
soma_pares = 0

while True:
    num = int(input("Digite um número inteiro (0 para sair): "))
    
    if num == 0:
        break
    
    if num % 2 == 0:
        qtd_pares += 1
        soma_pares += num
    else:
        qtd_impares += 1

print(f"\nQuantidade de pares: {qtd_pares}")
print(f"Quantidade de ímpares: {qtd_impares}")
print(f"Soma dos números pares: {soma_pares}")