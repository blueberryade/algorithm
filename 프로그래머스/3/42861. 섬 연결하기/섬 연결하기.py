def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n+1)]
    answer = 0
    
    def find(x):
        if parent[x]!=x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        
    
    for cost in costs:
        a,b,c = cost
        
        if find(a)!=find(b):
            union(a,b)
            answer+=c
    
    
    return answer