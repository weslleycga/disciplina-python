print("--- Desafio 4: Sistema de Senha ---")
senha_correta = "1234"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido! Bem-vindo.")
        break
    else:
        tentativas += 1
        restantes = limite - tentativas
        print(f"Senha incorreta. Tentativas restantes: {restantes}")

if tentativas == limite:
    print("Acesso bloqueado após 3 erros.")