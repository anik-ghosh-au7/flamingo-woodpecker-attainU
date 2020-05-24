class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def connect(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def find_all_distances(self, root):
        distances = [-1 for _ in range(self.n)]
        queue = []
        distances[root] = 0
        queue.append(root)

        while queue:
            node = queue.pop(0)
            children = self.edges[node]
            for child in children:
                if distances[child] < 0:
                    distances[child] = distances[node] + 6
                    queue.append(child)

        distances.pop(root)

        print(" ".join(map(str, distances)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)

# Input
# 2

# Part - 1
# 4 2
# 1 2
# 1 3
# 1

# Output
# 6 6 -1

# Part - 2
# 3 1
# 2 3
# 2

# Output
# -1 6
