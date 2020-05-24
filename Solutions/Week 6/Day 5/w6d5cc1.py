from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, current_vertex, adjacent_vertex):
        self.graph[current_vertex].append(adjacent_vertex)

    def bfs(self, current_vertex):
        visited = [False for _ in range(len(self.graph))]
        queue = [current_vertex]
        result = []

        while queue:
            current_vertex = queue.pop(0)
            visited[current_vertex] = True
            result.append(current_vertex)

            for i in self.graph[current_vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return result


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("BFS traversal from vertex 2 : ", *g.bfs(2))
