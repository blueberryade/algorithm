from collections import deque

n,k = map(int,input().split())
way = [0]*100001
q = deque()
q.append(n)
result = 0
cnt = 0

while q:
    now = q.popleft()
    temp = way[now]

    if now == k:
        result = temp
        cnt+=1
        continue
        
    for i in (now-1,now+1,now*2):
        if 0<=i<100001 and (way[i] ==0 or way[i]==way[now]+1):
            way[i] = way[now]+1
            q.append(i)

print(result)    
print(cnt)
