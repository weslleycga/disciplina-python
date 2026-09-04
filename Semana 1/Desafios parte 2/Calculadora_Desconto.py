#nesse desafio irei criar uma calculadora de desconto, onde o usuario ira digitar o valor do produto e o percentual de desconto, e o programa ira calcular o valor do desconto e o valor final do produto com desconto.
#desafio 5 disciplina de python

#Nessa parte irei receber o valor do produto e o percentual de desconto do usuario
valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

#Aqui sera realizado o calculo do valor do desconto, multiplicando o valor do produto pelo percentual de desconto e dividindo por 100
valor_desconto = (valor_produto * percentual_desconto) / 100

#Aqui sera realizado o calculo do valor final do produto com desconto, subtraindo o valor do desconto do valor do produto
valor_final = valor_produto - valor_desconto

#Aqui sera exibido o valor do desconto e o valor final do produto com desconto, utilizando o f-string para formatar a saída com 2 casas decimais
print("O valor do desconto é:", f"{valor_desconto:.2f}")
print("O valor final do produto com desconto é:", f"{valor_final:.2f}")
