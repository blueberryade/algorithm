import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

result = 0
start, end = 0,0
visited = [False]*1000001

while start < N and end < N:
    if not visited[data[end]]:
        visited[data[end]] = True
        end+=1
        result+=(end-start)
    else:
        visited[data[start]] = False
        start+=1

print(result)