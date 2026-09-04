print("--- Desafio 3: Estatísticas de 5 Números ---")
numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")