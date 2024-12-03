import sys
input = sys.stdin.readline

N,d,k,c = map(int,input().split())
data = [int(input()) for _ in range(N)]

result = 0

for i in range(N):
    if i+k > N:
        cur_cnt = len(set(data[i:N] + data[:(i+k)%N] + [c]))
    else:
        cur_cnt = len(set(data[i:i+k] + [c]))
    
    result = max(result,cur_cnt)
        

print(result)