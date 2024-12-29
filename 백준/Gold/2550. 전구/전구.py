from bisect import bisect_left

N = int(input())
switch = list(map(int,input().split()))
bulb = list(map(int,input().split()))

dp = [0]*(N+1)

for i,v in enumerate(bulb):
    dp[v] = i+1

LIS = []
idx = []

for s in switch:
    now = dp[s]
    if len(LIS) == 0 or LIS[-1] < now:
        idx.append(len(LIS))
        LIS.append(now)
        
    else:
        cur = bisect_left(LIS,now)
        if len(LIS) == cur:
            LIS.append(now)
        else:
            LIS[cur] = now
        idx.append(cur)

print(len(LIS))

answer = []
pos = max(idx)

for v in idx[::-1]:
    N-=1
    if pos == v:
        answer.append(switch[N])
        pos-=1

print(*sorted(answer))