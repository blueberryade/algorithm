import sys
input = sys.stdin.readline

def find(a):
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        a,b = b,a
    parent[a] = b

def rob():
    for i in range(1,N+1):
        if i!=parent[i]:
            continue
        for j in range(K-1,friends_num[i]-1,-1):
            dp[j] = max(dp[j],dp[j-friends_num[i]]+candies[i])

N,M,K = map(int,input().split())
candies = [0]+list(map(int,input().split()))
parent = [i for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    union(a,b)

friends_num = [1]*(N+1)
dp = [0]*K

for i in range(1,N+1):
    if i!=parent[i]:
        root = find(i)
        candies[root]+=candies[i]
        friends_num[root]+=friends_num[i]        

rob()
print(max(dp))
        