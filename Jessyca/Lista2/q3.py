#Sistema de Notas de funcionário
nota = float(input('Digite a nota do funcionário: '))

if nota >= 9:
    print('Excelente')
    print('Parabéns! Continue assim!')
elif nota >= 7:
    print('Bom')
elif nota >= 5:
    print('Regular')
else:
    print('Insatisfação')
    print('Procure melhorar seu desempenho.')