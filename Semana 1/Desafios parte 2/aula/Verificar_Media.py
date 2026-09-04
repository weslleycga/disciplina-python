n1, n2 , n3 = map(float, input("Digite as três notas separadas por espaço: ").split())
media = (n1 + n2 + n3) / 3
if media >= 7:
    print("Aprovado! Média:", media)
elif media >= 5:
    print("Recuperação! Média:", media)
else:
    print("Reprovado! Média:", media)