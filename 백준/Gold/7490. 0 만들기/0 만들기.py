import sys
input = sys.stdin.readline

def dfs(n,now,result):
    if now == n+1:
        if eval(result.replace(' ','')) == 0:
            print(result)
        return
    
    dfs(n, now+1, result+' '+str(now))
    dfs(n, now+1, result+'+'+str(now))
    dfs(n, now+1, result+'-'+str(now))


t = int(input())
for _ in range(t):
    n = int(input())
    dfs(n,2,'1')
    print()

