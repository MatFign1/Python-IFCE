#Classificação de Nota em Conceito
nota = float(input("Digite uma nota (0 a 10): "))

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
elif nota >= 0:
    print("Conceito D")
else:
    print("Nota inválida")