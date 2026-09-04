print("--- Desafio 2: Menu de Operações ---")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Escolha a opção (1-4): "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        print(f"Resultado: {n1} + {n2} = {n1 + n2}")
    case 2:
        print(f"Resultado: {n1} - {n2} = {n1 - n2}")
    case 3:
        print(f"Resultado: {n1} * {n2} = {n1 * n2}")
    case 4:
        if n2 != 0:
            print(f"Resultado: {n1} / {n2} = {n1 / n2}")
        else:
            print("Erro: Divisão por zero!")
    case _:
        print("Opção inválida.")