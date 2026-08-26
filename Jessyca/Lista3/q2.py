#Avaliação de Desempenho Escolar com Comportamento
media = float(input('Digite a média das notas: '))
comportamento = float(input('Digite o índice do comportamento: '))

if media >= 8 and comportamento >= 8:
    print('Excelente aluno')
elif media >= 5 and media < 6:
    print('Em recuperação')
elif media >= 6 and comportamento >= 6:
    print('Bom aluno')
else:
    print('Precisa melhorar')