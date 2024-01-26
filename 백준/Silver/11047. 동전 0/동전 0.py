n, k = map(int,input().split())
cnt = 0
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)

for i in coin:
    if k == 0:
        break
    else:
        cnt += k // i
        k = k%i
print(cnt)
