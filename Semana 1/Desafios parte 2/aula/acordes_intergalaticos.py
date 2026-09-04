import sys

def resolver():
    # Usamos apenas split() para ignorar espaços e quebras de linha fantasmas
    dados = sys.stdin.read().split()
    
    if not dados:
        return

    # Lemos direto pelos índices
    N = int(dados[0])
    Q = int(dados[1])

    f = 1
    piano = [[i, f] for i in range(N)]
    acordes = []

    # O ponteiro começa no índice 2 (onde estão os primeiros valores de 'a' e 'b')
    ponteiro = 2
    for _ in range(Q):
        a = int(dados[ponteiro])
        b = int(dados[ponteiro + 1])
        acordes.append([a, b])
        ponteiro += 2  # Avança para o próximo par

    # SUA LÓGICA EXATA MANTIDA
    for a, b in acordes:
        quantidade_notas = [0] * 9    
        
        for i in range(a, b + 1): 
            valor_nota = piano[i][1]
            quantidade_notas[valor_nota] += 1 
            
        maior_frequencia = -1
        
        for valor_nota in range(9):
            if quantidade_notas[valor_nota] >= maior_frequencia:
                maior_frequencia = quantidade_notas[valor_nota]
                f = valor_nota
                
        for i in range(a, b + 1): 
            piano[i][1] = (piano[i][1] + f) % 9       

    # IMPRIMIR TUDO NA MESMA LINHA
    # A maioria dos problemas do Beecrowd espera saídas de array assim
    resultado = [gaveta[1] for gaveta in piano]
    print( *resultado ) # O asterisco desempacota a lista com espaços

if __name__ == "__main__":
    resolver()