from bisect import bisect_left
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        data = list(map(int,input().split()))
        lst = []

        for i in range(n):
            idx = bisect_left(lst,data[i])
            if idx == len(lst):
                lst.append(data[i])
            else:
                lst[idx] = data[i]
        print(len(lst))
    except:
        break