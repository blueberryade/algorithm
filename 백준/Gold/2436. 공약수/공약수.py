import math

g,l = map(int,input().split())

n = l//g

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


for a in reversed(range(1,int(math.sqrt(n)+1))):
    if n % a == 0:
        x = g * a
        y = g * (n//a)

        if gcd(x,y) == g:
            print(x,y)
            break