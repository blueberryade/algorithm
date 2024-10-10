import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())


def dfs(s,t):
    if s == t:
        return 1
    if len(t) <= len(s):
        return 0
    
    ans = 0

    if t[-1] == "A":
        ans = dfs(s,t[:-1])
    
    if ans == 1:
        return 1
    
    if t[0] == "B":
        ans = dfs(s,t[::-1][:-1])
    
    return ans

print(dfs(s,t))