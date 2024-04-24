n,r,c = map(int,input().split())

def solve(n,r,c):
    if n == 0:
        return 0
    return 2*(r%2)+(c%2)+4*solve(n-1,r//2,c//2)

print(solve(n,r,c))