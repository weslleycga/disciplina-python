# Desafios parte 2 - Aula 1
N = int(input())
mapa1 = [[] for _ in range(N+1)]
mapa2 = [[] for _ in range(N+1)]
# mapeamento das arestas do primeiro grafo
for _ in range(N - 1):
    u, v = map(int, input().split())
    mapa1[u].append(v)
    mapa1[v].append(u)
# mapeamento das arestas do segundo grafo
for _ in range(N - 1):
    u, v = map(int, input().split())
    mapa2[u].append(v)
    mapa2[v].append(u)

