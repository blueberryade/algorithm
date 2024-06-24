from bisect import bisect_left,bisect_right
t = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

Asum = A
Bsum = B

for s in range(n):
    for e in range(s+1,n):
        Asum.append(sum(A[s:e+1]))
for s in range(m):
    for e in range(s+1,m):
        Bsum.append(sum(B[s:e+1]))        

Asum.sort()
Bsum.sort()

result = 0

for i in range(len(Asum)):
    l = bisect_left(Bsum,t-Asum[i])
    r = bisect_right(Bsum,t-Asum[i])
    result+=r-l
print(result)    