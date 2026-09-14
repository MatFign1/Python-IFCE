#Sistema de Notas de Funcionários
nota = float(input("Digite a nota do funcionário (0 a 10): "))

if nota >= 9:
    print("Avaliação: Excelente")
    print("Parabéns! Continue assim!")
elif nota >= 7:
    print("Avaliação: Bom")
elif nota >= 5:
    print("Avaliação: Regular")
elif nota >= 0:
    print("Avaliação: Insatisfatório")
    print("Procure melhorar seu desempenho.")
else:
    print("Nota inválida.")