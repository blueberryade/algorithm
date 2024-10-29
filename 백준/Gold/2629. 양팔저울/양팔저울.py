import sys
input =  sys.stdin.readline

n = int(input())
weights = list(map(int,input().split()))
m = int(input())
marbles = list(map(int,input().split()))

max_weight = sum(weights)
dp = [[False]*(max_weight+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(1,n+1):
    weight = weights[i-1]
    for j in range(max_weight+1):
        if dp[i-1][j]:
            dp[i][j] = True
            if j + weight <= max_weight:
                dp[i][j+weight] = True
            if abs(j-weight)<=max_weight:
                dp[i][abs(j-weight)] = True



result = []
for i in marbles:
    if i > max_weight:
        result.append("N")
    elif dp[n][i]:
        result.append("Y")
    else:
        result.append("N")

print(*result)