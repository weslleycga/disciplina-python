#Conversor de tempo disciplina de Python
# o objetivo desse programa é converter o tempo em segundos para horas, minutos e segundos
tempo = int(input("Digite o tempo em segundos: ")) #variável tempo recebe o valor digitado pelo usuário em segundos

#Abaixo Calculei o número de horas, minutos e segundos a partir do tempo em segundos
horas = tempo // 3600 #utilizei a divisão inteira para obter o número de horas
minutos = (tempo % 3600) // 60 #O simbolo de % representa o resto da divisão
segundos = (tempo % 3600) % 60 #utilizei a divisão pelo resto para obter o número de segundos
print("O tempo é: {} horas, {} minutos e {} segundos".format(horas, minutos, segundos)) #utilizei o método format para exibir o resultado na tela de forma organizada, tambem poderia ser utilizado o f-string, mas optei por utilizar o método format.