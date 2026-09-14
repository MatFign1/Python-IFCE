#Notas
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))
frequencia = float(input("Digite a frequência (%): "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 7 and frequencia >= 75:
    print("Situação: Aprovado")
elif (5 <= media < 7) or (60 <= frequencia <= 74):
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

if media >= 9:
    print("Parabéns pelo desempenho excepcional!")