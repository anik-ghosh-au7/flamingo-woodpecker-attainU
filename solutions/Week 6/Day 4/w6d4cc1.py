from collections import defaultdict


class Graph:
    def __init__(self, isWeighted=False, isDirected=False):
        self.graph = defaultdict(list)
        self.weighted = isWeighted
        self.directed = isDirected

    def addEdge(self, a, b, weight=0):
        if self.weighted and not self.directed:
            self.graph[a].append((b, weight))
            self.graph[b].append((a, weight))
        elif self.weighted and self.directed:
            self.graph[a].append((b, weight))
        elif not self.weighted and not self.directed:
            self.graph[a].append(b)
            self.graph[b].append(a)
        else:
            self.graph[a].append(b)

    def getAdjacencyMatrix(self):
        matrix = [[0 for i in range(0, len(self.graph))] for j in range(0, len(self.graph))]
        if self.weighted:
            for k in self.graph:
                for l, m in self.graph[k]:
                    matrix[k][l] = m
        else:
            for k in self.graph:
                for l in self.graph[k]:
                    matrix[k][l] = 1
        return matrix

    def print(self):
        print(self.graph)


def getAdjacencyList(matrix, isWeighted):
    lis = defaultdict(list)
    if isWeighted:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != 0:
                    lis[i].append((j, matrix[i][j]))
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != 0:
                    lis[i].append(j)
    return lis


print("UNWEIGHTED")
print("---------------------------------")
g = Graph(False, False)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(0, 4)
g.addEdge(1, 4)
g.addEdge(1, 3)
g.print()
mat = g.getAdjacencyMatrix()
print("matrix - ", mat)
print("list - ", getAdjacencyList(mat, False))

print("WEIGHTED")
print("---------------------------------")
g = Graph(True, False)
g.addEdge(0, 1, 2)
g.addEdge(1, 2, 3)
g.addEdge(2, 3, 4)
g.addEdge(3, 4, 1)
g.addEdge(0, 4, 5)
g.addEdge(1, 4, 3)
g.addEdge(1, 3, 3)
g.print()
mat = g.getAdjacencyMatrix()
print("matrix - ", mat)
print("list - ", getAdjacencyList(mat, True))