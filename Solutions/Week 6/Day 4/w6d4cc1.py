class Graph:
    def __init__(self, size, directed=False):
        self.size = size
        self.graph = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.directed = directed

    def add_edges(self, u, v):
        if self.directed:
            self.graph[u][v] = 1
        else:
            self.graph[u][v] = 1
            self.graph[v][u] = 1

    def get_elem(self, i, j):
        return self.graph[i][j]


def transform_to_adj_list(uw_graph):
    lis = {i: [] for i in range(uw_graph.size)}  # {0: [1, 3], 1: [0, 2, 4], 2: [1,3 ], 3: [2, 0], 4: [1]}
    for i in range(uw_graph.size):
        for j in range(uw_graph.size):  # 0, 0 - 0, 1 - 0, 2 - 0, 3 - 0, 4 --> 1, 0 - 1, 1 - 1, 2 - 1, 3 - 1, 4 .... 4, 4
            if uw_graph.get_elem(i, j) != 0:
                lis[i].append(j)
    return lis


g = Graph(5, False)
g.add_edges(0, 1)
g.add_edges(1, 2)
g.add_edges(2, 3)
g.add_edges(3, 0)
g.add_edges(1, 4)

print("Unweighted & Undirected graph - ")
print("matrix representation - ", g.graph)
print("list representation - ", transform_to_adj_list(g))

print("----------------------------------------------------------------------------")

g = Graph(5, True)
g.add_edges(0, 1)
g.add_edges(1, 2)
g.add_edges(2, 3)
g.add_edges(3, 0)
g.add_edges(1, 4)

print("Unweighted & Directed graph - ")
print("matrix representation - ", g.graph)
print("list representation - ", transform_to_adj_list(g))

# Unweighted & Undirected graph -
# matrix representation -  [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0]]
# list representation -  {0: [1, 3], 1: [0, 2, 4], 2: [1, 3], 3: [0, 2], 4: [1]}
# ----------------------------------------------------------------------------
# Unweighted & Directed graph -
# matrix representation -  [[0, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# list representation -  {0: [1], 1: [2, 4], 2: [3], 3: [0], 4: []}


#   0  1  2  3  4
# [[0, 1, 0, 1, 0], 0
#  [1, 0, 1, 0, 1], 1
#  [0, 1, 0, 1, 0], 2
#  [1, 0, 1, 0, 0], 3
#  [0, 1, 0, 0, 0]] 4
