import sys
from collections import Counter
input = sys.stdin.readline

r,c,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(3)]

r -=1
c -=1
result = 0

def r_operation(graph):
    new_graph = []
    max_col = 0
    for row in graph:
        counter = Counter(row)
        del counter[0]
        new_row = []
        for num,cnt in sorted(counter.items(),key=lambda x: (x[1],x[0])):
            new_row.extend([num,cnt])
        max_col = max(max_col,len(new_row))
        new_graph.append(new_row)
    
    for row in new_graph:
        while len(row) < max_col:
            row.append(0)

    return new_graph

def c_opertaion(graph):
    new_graph = []
    max_row = 0
    transposed= list(zip(*graph))
    for col in transposed:
        counter  = Counter(col)
        del counter[0]
        new_col = []
        for num,cnt in sorted(counter.items(),key=lambda x:(x[1],x[0])):
            new_col.extend([num,cnt])
        max_row = max(max_row,len(new_col))
        new_graph.append(new_col)
    
    for col in new_graph:
        while len(col) < max_row:
            col.append(0)
    new_graph = list(zip(*new_graph))
    return new_graph



while result<=100:
    if r< len(graph) and c< len(graph[0]) and graph[r][c] == k:
        print(result)
        break

    if len(graph) >= len(graph[0]):
        graph = r_operation(graph)
    else:
        graph = c_opertaion(graph)

    result+=1

else:
    print(-1)

