#Simulador de saque
saldo = 1000.0

while saldo > 0:
    print(f"Saldo atual: R$ {saldo:.2f}")
    saque = float(input("Quanto deseja retirar? (0 para encerrar): R$ "))
    
    if saque == 0:
        break
    elif saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= saque

print(f"Operação finalizada. Saldo restante: R$ {saldo:.2f}")