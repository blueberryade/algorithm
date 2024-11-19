import sys
input = sys.stdin.readline

A,B = map(int,input().split())

def count_ones(x):
    if x < 0:
        return 0
    count = 0
    power = 1
    
    while power <= x:
        full_blocks = (x+1) // (power*2)
        remaining = (x+1) % (power*2)

        count+= full_blocks * power + max(0,remaining-power)
        power*=2

    return count
    
print(count_ones(B)-count_ones(A-1))