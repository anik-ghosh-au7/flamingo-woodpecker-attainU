graph = {
    'A': {'D': 1, 'B': 3},
    'B': {'A': 3, 'C': 1, 'D': 3},
    'C': {'B': 1, 'D': 1, 'E': 5, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 1, 'E': 6},
    'E': {'C': 5, 'D': 6, 'F': 2},
    'F': {'C': 4, 'E': 2}
}


# print no. of vertices in O(1)
# print no. of edges in O(V)
def getEdges(graph):
    # (from_ver,to_ver,weight)
    all_edge = set()  # {(a,b,3),(f,g,4)}  (b,a,3)
    for each_vertex in graph:
        for adj_vert in graph[each_vertex]:
            if (adj_vert, each_vertex, graph[each_vertex][adj_vert]) not in all_edge:
                all_edge.add((each_vertex, adj_vert, graph[each_vertex][adj_vert]))
    return all_edge


# print(getEdges(graph))
# print(get)
def kruskal(graph):
    answer_edge = []
    all_edges = getEdges(graph)
    all_edges = sorted(all_edges, key=lambda x: x[2])
    set_list = []
    for vertex in graph:
        st = set()
        st.add(vertex)
        set_list.append(st)
    for edge in all_edges:
        vertex1, vertex2 = edge[0:2]
        # vertex1, vertex2 = edge[0],edge[1]
        for curr_set in set_list:
            if vertex1 in curr_set:
                set1 = curr_set
            if vertex2 in curr_set:
                set2 = curr_set
        if set1 == set2:
            continue
        else:
            answer_edge.append(edge)
            set_list.append(set1.union(set2))
            set_list.remove(set1)
            set_list.remove(set2)
    return answer_edge

    print(all_edges)


print(kruskal(graph))
