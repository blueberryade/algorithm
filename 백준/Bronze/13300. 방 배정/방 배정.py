n,k = map(int,input().split())

cnt = 0
lst = [0]*12

for i in range(n):
    s,y = map(int,input().split())
    if s == 0:
        lst[y-1]+=1
    else:
        lst[y+5]+=1

for i in lst:
    if i%k == 0:
        cnt +=i//k
    else:
        cnt+=i//k+1
print(cnt)