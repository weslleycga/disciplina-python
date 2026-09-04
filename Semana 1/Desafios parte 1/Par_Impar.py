# Programa que verifica se um número é par ou ímpar
#desafio 3 disciplina de python
num = int(input("Digite o numero inteiro: ")) # recebe o numero digitado pelo usuario

#Nessas condições, o operador % é utilizado para verificar se o resto da divisão do número por 2 é igual a 0. Se for, o número é par; caso contrário, é ímpar.
if num % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")
