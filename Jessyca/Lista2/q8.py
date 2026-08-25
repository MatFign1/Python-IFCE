#Notas
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
frequencia = float(input("Digite a frequência do aluno (%): "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and frequencia >= 75:
    print("Aluno:", nome)
    print("Média:", media)
    print("Aprovado")

elif (media >= 5 and media < 7) or (frequencia >= 60 and frequencia <= 74):
    print("Aluno:", nome)
    print("Média:", media)
    print("Recuperação")

else:
    print("Aluno:", nome)
    print("Média:", media)
    print("Reprovado")

if media >= 9:
    print("Parabéns pelo desempenho excepcional!")