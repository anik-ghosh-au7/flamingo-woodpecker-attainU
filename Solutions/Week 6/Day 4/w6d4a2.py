class Graph:
    def __init__(self, size, directed=False):
        self.size = size
        self.graph = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.directed = directed

    def add_edges(self, u, v, w=0):
        if self.directed:
            self.graph[u][v] = w
        else:
            self.graph[u][v] = w
            self.graph[v][u] = w

    def get_elem(self, i, j):
        return self.graph[i][j]


def transform_to_adj_list(w_graph):
    lis = {i: [] for i in range(w_graph.size)}  # {0: [(1, 10), (3, 40)], 1: [(0, 10), (2, 20), (4, 50)], 2: [(1, 20), (3, 30)], 3: [(0, 40), (2, 30)], 4: [(1, 50)]}
    for i in range(w_graph.size):
        for j in range(w_graph.size):
            if w_graph.get_elem(i, j) != 0:
                lis[i].append((j, w_graph.get_elem(i, j)))
    return lis


g = Graph(5, False)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

print("Weighted & Undirected graph - ")
print("matrix representation - ", g.graph)
print("list representation - ", transform_to_adj_list(g))

print("----------------------------------------------------------------------------")

g = Graph(5, True)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

print("Weighted & Directed graph - ")
print("matrix representation - ", g.graph)
print("list representation - ", transform_to_adj_list(g))

# Weighted & Undirected graph -
# matrix representation -  [[0, 10, 0, 40, 0], [10, 0, 20, 0, 50], [0, 20, 0, 30, 0], [40, 0, 30, 0, 0], [0, 50, 0, 0, 0]]
# list representation -  {0: [(1, 10), (3, 40)], 1: [(0, 10), (2, 20), (4, 50)], 2: [(1, 20), (3, 30)], 3: [(0, 40), (2, 30)], 4: [(1, 50)]}
# ----------------------------------------------------------------------------
# Weighted & Directed graph -
# matrix representation -  [[0, 10, 0, 0, 0], [0, 0, 20, 0, 50], [0, 0, 0, 30, 0], [40, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# list representation -  {0: [(1, 10)], 1: [(2, 20), (4, 50)], 2: [(3, 30)], 3: [(0, 40)], 4: []}

#   0  1   2   3  4
# [[0, 10, 0, 40, 0],  0
#  [10, 0, 20, 0, 50], 1
#  [0, 20, 0, 30, 0],  2
#  [40, 0, 30, 0, 0],  3
#  [0, 50, 0, 0, 0]]   4


