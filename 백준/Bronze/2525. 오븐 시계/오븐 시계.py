h,m = map(int, input().split())
t = int(input())

th = t//60
tm = t%60

h += th
m += tm
if m>59:
    m -=60
    h+=1
if h>23:
    h-=24

print(h,m)
