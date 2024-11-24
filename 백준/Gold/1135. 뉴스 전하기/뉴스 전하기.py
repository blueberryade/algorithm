N = int(input())
parent_lst = list(map(int,input().split()))
child_lst = [[] for _ in range(N)]

for child in range(1,N):
    parent = parent_lst[child]
    child_lst[parent].append(child)

def dfs(n):
    if not child_lst[n]:
        return 0
    result = []

    for c in child_lst[n]:
        result.append(dfs(c))
    result.sort(reverse=True)
    result = [result[i]+i+1 for i in range(len(child_lst[n]))]
    return max(result)

print(dfs(0))