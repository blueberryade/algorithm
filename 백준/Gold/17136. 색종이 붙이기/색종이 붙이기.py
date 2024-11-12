import sys
input = sys.stdin.readline

graph = [list(map(int,input().split())) for _ in range(10)]
paper_count = [0,5,5,5,5,5]
min_papers = sys.maxsize

def can_attach(x,y,size):
    if x+size > 10 or y+size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if graph[x+i][y+j] == 0:
                return False
    return True

def attach(x,y,size,value):
    for i in range(size):
        for j in range(size):
            graph[x+i][y+j] = value

def dfs(x,y,used_papers):
    global min_papers

    if y >= 10:
        dfs(x+1,0,used_papers)
        return
    
    if x >= 10:
        min_papers = min(min_papers,used_papers)
        return
    
    if graph[x][y] == 0:
        dfs(x,y+1,used_papers)
        return
    

    for size in range(5,0,-1):
        if paper_count[size] > 0 and can_attach(x,y,size):
            attach(x,y,size,0)
            paper_count[size]-=1
            dfs(x,y+1,used_papers+1)
            attach(x,y,size,1)
            paper_count[size]+=1

dfs(0,0,0)

print(min_papers if min_papers != sys.maxsize else -1)