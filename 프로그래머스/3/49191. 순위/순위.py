def solution(n, results):
    graph = [[0]*n for _ in range(n)]
    answer = 0
    
    for a,b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    
    for row in graph:
        if row.count(0) == 1:
            answer+=1
    
    
    return answer