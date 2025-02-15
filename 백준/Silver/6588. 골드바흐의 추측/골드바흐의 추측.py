import math
import sys
input = sys.stdin.readline

arr = [True]*1000001
for i in range(2,int(math.sqrt(len(arr))+1)):
    if arr[i]:
        for j in range(2*i,1000001,i):
            arr[j] = False


while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3,int(n/2)+1,2):
        if arr[i] and arr[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')