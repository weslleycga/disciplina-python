print("Escolha uma das opções abaixo:")
print("1. Opção 1: confirmação de inscrição na maratona")
print("2. Opção 2: cancelamento de inscrição")
print("3. Opção 3: consulta de inscrição")

opcao = int(input("Digite o número da opção desejada: "))

print("Você escolheu a opção:", opcao)

match opcao:
    case 1:
        print("inscrição confirmada na maratona")
    case 2:
        print("inscrição cancelada")
    case 3:
        print("Você escolheu a Opção 3")

