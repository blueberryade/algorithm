from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

data.sort()
result = 0

for i in range(N-2):
    start = i+1
    end = N-1

    while start < end:
        total = data[i]+data[start]+data[end]
        if total > 0:
            end-=1
        else:
            if total == 0:
                if data[start] == data[end]:
                    result+=end-start
                else:
                    idx = bisect_left(data,data[end])
                    result+= end-idx+1

            start+=1

print(result)