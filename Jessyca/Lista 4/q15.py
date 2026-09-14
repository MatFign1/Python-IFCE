#Contador de votos
votos_A = 0
votos_B = 0

voto = int(input("Digite o voto (1 para Candidato A, 2 para Candidato B, 0 para encerrar): "))

while voto != 0:
    if voto == 1:
        votos_A += 1
    elif voto == 2:
        votos_B += 1
    else:
        print("Voto inválido!")
    voto = int(input("Digite o voto (1 para Candidato A, 2 para Candidato B, 0 para encerrar): "))

print(f"Total de votos Candidato A: {votos_A}")
print(f"Total de votos Candidato B: {votos_B}")