n = int(input())
lst = []
for _ in range(n):
    a,b,c = map(int,input().split())
    if a == b == c:
        lst.append(10000+a*1000)
    elif a == b or b == c:
        lst.append(1000+b*100)
    elif c == a:
        lst.append(1000+c*100)
    else:
        lst.append(max(a,b,c)*100)
print(max(lst))