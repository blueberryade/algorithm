import sys
input = sys.stdin.readline

g = int(input())
a,b = 1,1
result = True

while a+b <= g:
    tmp = a**2 - b**2

    if tmp == g :
        print(a)
        a +=1
        result = False

    elif tmp > g :
        b +=1
        
    elif tmp < g :
        a +=1

if result :
    print(-1)