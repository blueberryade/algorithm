import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]

result = 0

for i in range(n):
    if i+k > n:
        cur_cnt = len(set(sushi[i:n] + sushi[:(i+k)%n] + [c]))
    else:
        cur_cnt = len(set(sushi[i:i+k] + [c]))
    if result < cur_cnt:
        result = cur_cnt
        
print(result)