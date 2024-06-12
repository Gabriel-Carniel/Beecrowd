class Grafo:
    def __init__(self):
        self.adjacencia = {}
    
    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.adjacencia:
            self.adjacencia[vertice1] = []
        if vertice2 not in self.adjacencia:
            self.adjacencia[vertice2] = []
        
        self.adjacencia[vertice1].append(vertice2)

    def dfs_nivel(self, vertice, nivel, visitados=None):
        if visitados is None:
            visitados = set()

        visitados.add(vertice)
       
        for vizinho in self.adjacencia[vertice]:
            if vizinho not in visitados:
                nivel[vizinho-1][0] = vizinho
                nivel[vizinho-1][1] = nivel[vertice-1][1] + 1
                self.dfs_nivel(vizinho, nivel, visitados)
        return nivel
    
    def dfs_inv(self, vertice, tamanhoo, visitados):
        
        if (visitados[vertice-1] == True):
            return tamanhoo
        
        visitados[vertice-1] = True
        tamanhoo +=1
       
        for vizinho in self.adjacencia[vertice]:
              tamanhoo = self.dfs_inv(vizinho, tamanhoo, visitados)
        return tamanhoo
    
def main():
    
    from sys import stdin, stdout, setrecursionlimit
    setrecursionlimit(1000000)

    grafoNormal = Grafo()
    grafoInvert = Grafo()
    N, K = map(int, stdin.readline().split())
    sup = list(map(int, stdin.readline().split()))
    nivelV = [[0, 0] for _ in range(N)]
    nivelV[0][0] = 1
    nivelV[0][1] = 1
    for i in range(N-1):
        grafoNormal.adicionar_aresta(sup[i], i+2)
        grafoInvert.adicionar_aresta(i+2, sup[i])
    nivelV = grafoNormal.dfs_nivel(1, nivelV)
  

    nivelV.sort(key=lambda y: y[1], reverse=True)

    tamanho = [0] * N
    tamanhoo = 0
    visit = [False] * N

    for i in range(N):
        tamanho[i] = grafoInvert.dfs_inv(nivelV[i][0], tamanhoo, visit)
    res = 0
    tamanho.sort(reverse=True)
    for x in range(K):
        res = res + tamanho[x]
    stdout.write(f"{res}\n")

main()