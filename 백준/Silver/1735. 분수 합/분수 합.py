a,b = map(int,input().split())
c,d = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

num = gcd(a*d + c*b, b*d)
x = (a*d + c*b) // num
y = b*d // num
print(x,y)