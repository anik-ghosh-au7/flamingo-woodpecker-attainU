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


g = Graph(5, False, False)
g.add_edges(0, 1)
g.add_edges(1, 2)
g.add_edges(2, 3)
g.add_edges(3, 0)
g.add_edges(1, 4)

print("Unweighted & Undirected graph - ")
print("matrix representation - ", g.print_graph())
print("list representation - ", transform_to_adj_list(g, False))

print("----------------------------------------------------------------------------")

g = Graph(5, False, True)
g.add_edges(0, 1)
g.add_edges(1, 2)
g.add_edges(2, 3)
g.add_edges(3, 0)
g.add_edges(1, 4)

print("Unweighted & Directed graph - ")
print("matrix representation - ", g.print_graph())
print("list representation - ", transform_to_adj_list(g, False))

# Unweighted & Undirected graph -
# matrix representation -  [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0]]
# list representation -  {0: [1, 3], 1: [0, 2, 4], 2: [1, 3], 3: [0, 2], 4: [1]}
# ----------------------------------------------------------------------------
# Unweighted & Directed graph -
# matrix representation -  [[0, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# list representation -  {0: [1], 1: [2, 4], 2: [3], 3: [0], 4: []}
