class Graph:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(size)]

    def addEdge(self, vertex, adjacent_vertex):
        self.adj[vertex].append(adjacent_vertex)

    def iterative_dfs(self, current_vertex):
        visited_list = [False for _ in range(self.size)]
        stack = [current_vertex]
        result = []

        while stack:
            current_vertex = stack.pop()
            result.append(current_vertex)
            visited_list[current_vertex] = True

            for adjacent_vertex in self.adj[current_vertex]:
                if not visited_list[adjacent_vertex]:
                    stack.append(adjacent_vertex)

        return result


g = Graph(5)

# g.addEdge(0, 1)
# g.addEdge(1, 2)
# g.addEdge(2, 3)
# g.addEdge(3, 0)
# g.addEdge(1, 4)

# print("Iterative DFS : ", *g.iterative_dfs(0))  # 0 1 4 2 3

g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(0, 1)
g.addEdge(3, 3)
g.addEdge(1, 3)

print("Iterative DFS : ", *g.iterative_dfs(2))  # 2 0 1 3
