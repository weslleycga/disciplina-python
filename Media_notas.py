# Programa que calcula a média de 3 notas 
#desafio 4 disciplina de python
#Nessa parte irei receber as 3 notas do aluno
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#Aqui sera realizado a media das notas do aluno, somando as 3 notas e dividindo por 3
media = (n1 + n2 + n3) / 3

#Aqui sera exibido a media das notas do aluno, utilizando o f-string para formatar a saída com 2 casas decimais
print("A média das notas é:", f"{media:.2f}")