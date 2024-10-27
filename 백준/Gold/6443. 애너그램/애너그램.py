import sys
input = sys.stdin.readline

def backtrack(cnt):
    if len(word) == cnt:
        print("".join(answer))

    for k in visited:
        if visited[k]:
            visited[k]-=1
            answer.append(k)
            backtrack(cnt+1)
            visited[k]+=1
            answer.pop()

n = int(input())
for _ in range(n):
    word = sorted(list(input().rstrip()))
    visited = {}
    answer = []

    for i in word:
        if i in visited:
            visited[i]+=1
        else:
            visited[i] = 1
    backtrack(0)