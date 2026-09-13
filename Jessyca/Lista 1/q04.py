#Nota e aprovação
nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")