import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
add,minus,mul,div = list(map(int,input().split()))

max_value = -1e9
min_value = 1e9

def dfs(i,now):
    global max_value,min_value,add,minus,mul,div
    if i == n:
        max_value = max(now,max_value)
        min_value = min(now,min_value)
    else:
        if add > 0:
            add-=1
            dfs(i+1,now+nums[i])
            add+=1
        if minus > 0:
            minus-=1
            dfs(i+1,now-nums[i])
            minus+=1
        if mul > 0:
            mul-=1
            dfs(i+1,now*nums[i])
            mul+=1
        if div > 0:
            div-=1
            dfs(i+1,int(now/nums[i]))
            div+=1
dfs(1,nums[0])
print(max_value)
print(min_value)

            
