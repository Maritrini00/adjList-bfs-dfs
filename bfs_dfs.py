#Lista de Adyacencia y búsqueda en anchura y profundidad
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_edges(self,s,d):
        if d not in self.adjList[s]:
            self.adjList[s].append(d)
        if s not in self.adjList[d]:
            self.adjList[d].append(s)

    def show_list(self):
        for v in self.adjList:
            print(v,":",self.adjList[v])

def dfs(graph,start,visited=None):
    if visited is None:
        visited = set() 
    visited.add(start)
    print(str(start)+ " ", end="")
    for n in graph.adjList[start]:
        if n not in visited:
            dfs(graph,n,visited)
    return visited

def bfs(graph,start):
    visited = set() 
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for n in graph.adjList[vertex]:
            if n not in visited:
                queue.append(n)
                visited.add(n)

grafo = Graph()
grafo.add_edges(0,1)
grafo.add_edges(0,2)
grafo.add_edges(1,0)
grafo.add_edges(1,3)
grafo.add_edges(1,4)
grafo.add_edges(2,0)
grafo.add_edges(3,1)
grafo.add_edges(4,2)
grafo.add_edges(4,3)

grafo.show_list()

print("\nDFS:")
dfs(grafo, 0)

print("\nBFS:")
bfs(grafo, 0)