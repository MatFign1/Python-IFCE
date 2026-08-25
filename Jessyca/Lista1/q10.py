#Classificação de nota em conceitos
nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('Conceito A')
elif nota >= 7:
    print('Conceito B')
elif nota >= 5:
    print('Conceito C')
else:
    print('Conceito D')