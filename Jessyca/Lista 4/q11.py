#Calculadora simples
opcao = ""

while opcao != "sair":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    if op == "+":
        print(f"Resultado: {n1 + n2}")
    elif op == "-":
        print(f"Resultado: {n1 - n2}")
    elif op == "*":
        print(f"Resultado: {n1 * n2}")
    elif op == "/":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

    opcao = input("Deseja continuar ou 'sair'? ").strip().lower()