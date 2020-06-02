import math
import os
import random
import re
import sys
import heapq

from collections import defaultdict


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    # graph = defaultdict(dict)
    graph = {i: {} for i in range(1, n + 1)} # {1: {}, 2: {}, 3: {}..}
    for u, v, w in edges:
        if v not in graph[u]:
            graph[u][v] = w
            graph[v][u] = w
        elif graph[u][v] > w:
            graph[u][v] = w
            graph[v][u] = w
    # print(graph)
    result_list = [-1] * (n + 1)    # [-1, 0, 5, 11, 13, -1]
    lst_for_hp = []  # prone
    heapq.heappush(lst_for_hp, (0, s))
    visited_set = set() # 1, 2, 3, 4
    while len(lst_for_hp) > 0:
        # print(lst_for_hp)
        popped_vertex = heapq.heappop(lst_for_hp)
        vertex = popped_vertex[1]
        total_weight = popped_vertex[0]  # total weight is the weight of the path
        if vertex in visited_set:
            continue
        result_list[vertex] = total_weight
        # print(vertex, total_weight)
        visited_set.add(vertex)
        for adj_vertex, weight in graph[vertex].items():  # traverse all adjacent vertex
            if adj_vertex not in visited_set:  # If not visited then push in heap
                heapq.heappush(lst_for_hp, (total_weight + weight, adj_vertex))

    # return result[1:s] + result[s + 1:]

    result_list.pop(s)  # sth element is popped before 0th elem else the index will change
    result_list.pop(0)
    return result_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
    print(result)

# Input
# 1
# 4 4
# 1 2 24
# 1 4 20
# 3 1 3
# 4 3 12
# 1

# Output
# [24, 3, 15]
