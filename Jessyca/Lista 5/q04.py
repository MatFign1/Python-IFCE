#Média de notas com sentinela
soma_notas = 0.0
qtd_validas = 0

while True:
    nota = float(input("Digite uma nota de 0 a 10 (-1 para encerrar): "))
    
    if nota == -1:
        break
    
    if 0 <= nota <= 10:
        soma_notas += nota
        qtd_validas += 1
    else:
        print("Nota inválida! Tente novamente.")

if qtd_validas > 0:
    media = soma_notas / qtd_validas
    print(f"\nMédia: {media:.2f}")
    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
else:
    print("Nenhuma nota válida foi informada.")