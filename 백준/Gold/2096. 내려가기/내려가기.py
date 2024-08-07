import sys
input = sys.stdin.readline

n = int(input())
dp_min = dp_max = list(map(int,input().split())) 


for i in range(1,n):
    a,b,c = map(int,input().split())
    dp_max = [
        max(dp_max[0],dp_max[1])+a,
        max(dp_max[0],dp_max[1],dp_max[2])+b,
        max(dp_max[1],dp_max[2])+c
    ]

    dp_min = [
        min(dp_min[0],dp_min[1])+a,
        min(dp_min[0],dp_min[1],dp_min[2])+b,
        min(dp_min[1],dp_min[2])+c
    ]

print(max(dp_max),min(dp_min))