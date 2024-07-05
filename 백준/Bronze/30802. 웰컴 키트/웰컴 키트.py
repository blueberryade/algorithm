n = int(input())
size = list(map(int,input().split()))
T,P = map(int,input().split())

t = 0
for s in size:
    t += s //T
    if s%T!=0:
        t+=1

p1 = n//P
p2 = n%P

print(t)
print(p1,p2)