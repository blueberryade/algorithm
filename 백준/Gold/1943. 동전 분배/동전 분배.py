import sys
input = sys.stdin.readline

for _ in range(3):
    total = 0
    coins = []

    for _ in range(int(input())):
        coin,cnt = map(int,input().split())
        total += coin*cnt
        coins.append((coin,cnt))
    
    if total % 2 == 1:
        print(0)
        continue

    total //=2
    dp = [True]+[False]*total
    
    answer = 0
    for i in range(len(coins)):
        c,n = coins[i]

        for j in range(total,c-1,-1):
            if dp[j-c]:
                for k in range(n):
                    if j+c*k <= total:
                        dp[j+c*k] = True
                    else:
                        break
        if dp[-1]:
            answer = 1
            break
    print(answer)