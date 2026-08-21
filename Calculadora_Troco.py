#desafio 1 - Calculadora de Troco disciplina de Python
#definir as variáveis
valor1 = float(input("Digite o valor do produto: ")) #Este é o preço do produto
valor2 = float(input("Digite o valor pago: "))  #Este é o valor pago pelo cliente

#criei essas condições para verificar se o valor pago é maior, igual ou menor que o valor do produto
if valor2 > valor1:
    troco = valor2 - valor1
    print("O valor do seu troco é: {}".format(troco))
elif valor2 == valor1:
    troco = valor2 - valor1
    print("O valor do seu troco é: {}".format(troco))
else:
    print("o valor não é suficiente para realizar a compra")
