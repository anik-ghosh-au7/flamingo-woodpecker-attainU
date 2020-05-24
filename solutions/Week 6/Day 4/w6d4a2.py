class Graph:
    def __init__(self, size, weighted=False, directed=False):
        self.size = size
        self.graph = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.weighted = weighted
        self.directed = directed

    def add_edges(self, u, v, w=0):
        if self.weighted and self.directed:
            self.graph[u][v] = w
        elif self.weighted and not self.directed:
            self.graph[u][v] = w
            self.graph[v][u] = w
        elif not self.weighted and not self.directed:
            self.graph[u][v] = 1
            self.graph[v][u] = 1
        else:
            self.graph[u][v] = 1

    def get_elem(self, i, j):
        return self.graph[i][j]

    def print_graph(self):
        return self.graph


def transform_to_adj_list(graph, weighted):
    lis = {i: [] for i in range(graph.size)}
    if weighted:
        for i in range(graph.size):
            for j in range(graph.size):
                if graph.get_elem(i, j) != 0:
                    lis[i].append((j, graph.get_elem(i, j)))
    else:
        for i in range(graph.size):
            for j in range(graph.size):
                if graph.get_elem(i, j) != 0:
                    lis[i].append(j)
    return lis


g = Graph(5, True, False)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

print("Weighted & Undirected graph - ")
print("matrix representation - ", g.print_graph())
print("list representation - ", transform_to_adj_list(g, True))

print("----------------------------------------------------------------------------")

g = Graph(5, True, True)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

print("Weighted & Directed graph - ")
print("matrix representation - ", g.print_graph())
print("list representation - ", transform_to_adj_list(g, True))

# Weighted & Undirected graph -
# matrix representation -  [[0, 10, 0, 40, 0], [10, 0, 20, 0, 50], [0, 20, 0, 30, 0], [40, 0, 30, 0, 0], [0, 50, 0, 0, 0]]
# list representation -  {0: [(1, 10), (3, 40)], 1: [(0, 10), (2, 20), (4, 50)], 2: [(1, 20), (3, 30)], 3: [(0, 40), (2, 30)], 4: [(1, 50)]}
# ----------------------------------------------------------------------------
# Weighted & Directed graph -
# matrix representation -  [[0, 10, 0, 0, 0], [0, 0, 20, 0, 50], [0, 0, 0, 30, 0], [40, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# list representation -  {0: [(1, 10)], 1: [(2, 20), (4, 50)], 2: [(3, 30)], 3: [(0, 40)], 4: []}
