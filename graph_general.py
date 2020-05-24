class Graph:
    def __init__(self, size, weighted=False, directed=False):
        self.size = size
        self.graph = {i: [] for i in range(self.size)}
        self.weighted = weighted
        self.directed = directed

    def add_edges(self, u, v, w=0):
        if self.weighted and self.directed:
            self.graph[u].append((v, w))
        elif self.weighted and not self.directed:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))
        elif not self.weighted and not self.directed:
            self.graph[u].append(v)
            self.graph[v].append(u)
        else:
            self.graph[u].append(v)

    def adj_matrix(self):
        mat = [[0 for _ in range(self.size)] for _ in range(self.size)]
        if self.weighted:
            for u in self.graph:
                for v, w in self.graph[u]:
                    mat[u][v] = w
        else:
            for u in self.graph:
                for v in self.graph[u]:
                    mat[u][v] = 1
        return mat

    def print_graph(self):
        return self.graph.items()


def transform_adj_list(mat, weighted):
    lis = {i: [] for i in range(len(mat))}
    if weighted:
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if mat[i][j] != 0:
                    lis[i].append((j, mat[i][j]))
    else:
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if mat[i][j] != 0:
                    lis[i].append(j)
    return lis


g = Graph(5, True, False)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

matrix = g.adj_matrix()

print("Weighted & Undirected graph - ", g.print_graph())
print("matrix representation - ", matrix)
print("list representation - ", transform_adj_list(matrix, True))

print("----------------------------------------------------------------------------")

g = Graph(5, True, True)
g.add_edges(0, 1, 10)
g.add_edges(1, 2, 20)
g.add_edges(2, 3, 30)
g.add_edges(3, 0, 40)
g.add_edges(1, 4, 50)

matrix = g.adj_matrix()

print("Weighted & Directed graph - ", g.print_graph())
print("matrix representation - ", matrix)
print("list representation - ", transform_adj_list(matrix, True))

# Weighted & Undirected graph -  dict_items([(0, [(1, 10), (3, 40)]), (1, [(0, 10), (2, 20), (4, 50)]), (2, [(1, 20), (3, 30)]), (3, [(2, 30), (0, 40)]), (4, [(1, 50)])])
# matrix representation -  [[0, 10, 0, 40, 0], [10, 0, 20, 0, 50], [0, 20, 0, 30, 0], [40, 0, 30, 0, 0], [0, 50, 0, 0, 0]]
# list representation -  {0: [(1, 10), (3, 40)], 1: [(0, 10), (2, 20), (4, 50)], 2: [(1, 20), (3, 30)], 3: [(0, 40), (2, 30)], 4: [(1, 50)]}
# ----------------------------------------------------------------------------
# Weighted & Directed graph -  dict_items([(0, [(1, 10)]), (1, [(2, 20), (4, 50)]), (2, [(3, 30)]), (3, [(0, 40)]), (4, [])])
# matrix representation -  [[0, 10, 0, 0, 0], [0, 0, 20, 0, 50], [0, 0, 0, 30, 0], [40, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# list representation -  {0: [(1, 10)], 1: [(2, 20), (4, 50)], 2: [(3, 30)], 3: [(0, 40)], 4: []}