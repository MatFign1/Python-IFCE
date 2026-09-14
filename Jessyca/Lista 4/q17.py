#Simulador de crescimento populacional
popA = 80000
popB = 200000
anos = 0

while popA <= popB:
    popA += popA * 0.03
    popB += popB * 0.015
    anos += 1

print(f"A população A ultrapassará B em {anos} anos.")