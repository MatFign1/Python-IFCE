#Avaliação de Desempenho Escolar com Comportamento
media = float(input("Digite a média das notas (0 a 10): "))
comportamento = float(input("Digite o índice de comportamento (0 a 10): "))

if 5 <= media <= 5.9:
    print("Em recuperação")
elif media >= 8 and comportamento >= 8:
    print("Excelente aluno")
elif media >= 6 and comportamento >= 6:
    print("Bom aluno")
elif media < 6 or comportamento < 6:
    print("Precisa melhorar")