import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
mlst = list(map(int,input().split()))
a.sort()

for i in mlst:
    left,right = 0,n-1
    f = False

    while left<=right:
        mid = (left+right) //2
        if i == a[mid]:
            f=True       
            print(1)
            break
        elif i > a[mid]:
            left = mid+1
        else:
            right = mid-1
    if not f:
        print(0)