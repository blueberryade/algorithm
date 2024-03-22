import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())
g = []
for _ in range(N):
    g.append([int(i) for i in input().split()])
    
answer = int(1e9)
idx = 0

for floor in range(257):
    exceed,lack = 0,0

    for i in range(N):
        for j in range(M):
            if g[i][j]> floor:
                exceed += g[i][j] - floor
            else:
                lack += floor - g[i][j] 
    if exceed + B < lack:
        continue
        
    if exceed *2 +lack <= answer:
        answer = (exceed*2)+lack
        idx = floor
print(answer,idx)
