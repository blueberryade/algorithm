import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int,input().split()))

result = 0
sumLst = []

if n == 1:
    dice = sorted(dice)
    for i in range(5):
        result+=dice[i]
else:
    sumLst.append(min(dice[0],dice[5]))
    sumLst.append(min(dice[1],dice[4]))
    sumLst.append(min(dice[2],dice[3]))
    sumLst = sorted(sumLst)

    min1 = sumLst[0]
    min2 = sumLst[0]+sumLst[1]
    min3 = sumLst[0]+sumLst[1]+sumLst[2]

    n1 = (n-2)*(n-2) + (n-2)*(n-1)*4
    n2 = (n-2)*4 + (n-1)*4
    n3 = 4

    result += min1*n1 + min2*n2 + min3*n3

print(result)    
    
