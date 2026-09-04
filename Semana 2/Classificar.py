print("--- Desafio 1: Classificação de Cliente ---")

idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda do cliente: "))

if idade < 21:
    if renda < 2000:
        categoria = "Bronze"
    else:
        categoria = "Prata"
elif 21 <= idade <= 50:
    if renda < 5000:
        categoria = "Prata"
    else:
        categoria = "Ouro"
else:
    if renda < 10000:
        categoria = "Ouro"
    else:
        categoria = "Diamante"

print(f"Cliente classificado como: {categoria}")