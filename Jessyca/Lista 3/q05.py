#Simulador de Bônus Salarial
salario = float(input("Digite o salário base: R$ "))
tempo = int(input("Digite o tempo de casa (em anos): "))
avaliacao = float(input("Digite a avaliação anual (0 a 10): "))

if avaliacao >= 9 and tempo >= 5:
    percentual = 0.20
elif avaliacao >= 7 and tempo >= 2:
    percentual = 0.10
elif avaliacao >= 5:
    percentual = 0.05
else:
    percentual = 0.0

bonus = salario * percentual
salario_final = salario + bonus

print(f"Valor do bônus: R$ {bonus:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")