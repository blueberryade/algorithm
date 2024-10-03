import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())
ladder = [[False]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a,b = map(int,input().split())
    ladder[a][b] = True


def check():
    for start in range(1,n+1):
        k = start
        for i in range(1,h+1):
            if ladder[i][k]:
                k+=1
            elif ladder[i][k-1]:
                k-=1
        if k!=start:
            return False
    return True

def dfs(cnt,x,y):
    global answer
    if check():
        answer = min(answer,cnt)
        return
    if cnt == 3 or answer <= cnt:
        return
    for i in range(x,h+1):
        k = y if  i==x else 1
        for j in range(k,n):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(cnt+1,i,j+2)
                ladder[i][j]  = False



answer = 4
dfs(0,1,1)
print(answer if answer < 4 else -1)