graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 1, 'A': 2},
    'D': {'A': 4, 'C': 3, 'E': 2, 'F': 11},
    'E': {'D': 2, 'F': 7},
    'F': {'D': 11, 'E': 7},
    'C': {'B': 1, 'D': 3, 'H': 2, 'G': 6},
    'G': {'C': 6, 'H': 2, 'I': 4},
    'H': {'C': 2, 'G': 2, 'I': 1},
    'I': {'G': 4, 'H': 1}
}


def getEdges(graph):
    # (from_ver,to_ver,weight)
    all_edge = set()  # {(a,b,3),(f,g,4)}  (b,a,3)
    for each_vertex in graph:
        for adj_vert in graph[each_vertex]:
            if (adj_vert, each_vertex, graph[each_vertex][adj_vert]) not in all_edge:
                all_edge.add((each_vertex, adj_vert, graph[each_vertex][adj_vert]))
    return all_edge


import heapq

lst_for_hp = []  # prone
heapq.heappush(lst_for_hp, (0, "H", None))
infected_set = set()
answer_edge = []
while len(lst_for_hp) > 0:
    poped_vertex = heapq.heappop(lst_for_hp)
    if poped_vertex[1] not in infected_set:
        infected_set.add(poped_vertex[1])
        answer_edge.append(poped_vertex)
    else:
        continue
    for adj_vertex, weight in graph[poped_vertex[1]].items():
        if adj_vertex not in infected_set:
            heapq.heappush(lst_for_hp, (weight, adj_vertex, poped_vertex[1]))
print(answer_edge)
