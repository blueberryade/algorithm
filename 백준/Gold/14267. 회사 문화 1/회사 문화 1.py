n,m = map(int,input().split())
superior = [0]+list(map(int,input().split()))
result = [0]*(n+1)

for _ in range(m):
    i,w = map(int,input().split())
    result[i]+=w

for i in range(2,n+1):
    result[i]+=result[superior[i]]

print(*result[1:])