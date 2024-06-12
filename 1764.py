class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []

        # Ordena todas as arestas pelo seu peso
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Inicializa os conjuntos disjuntos
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Printa as arestas selecionadas
        cont = 0
        for u, v, weight in result:
            cont = cont + weight
        print(cont)


# Exemplo de uso
while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  g = Graph(N)
  for i in range(M):
    U, V, P = map(int, input().split())
    g.add_edge(U, V, P)
    
  g.kruskal_mst()