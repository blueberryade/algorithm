import sys
input = sys.stdin.readline

n = int(input())
data1 = [int(input()) for _ in range(n)]
data1.sort()

data2 = []
for i in range(n):
    for j in range(i,n):
        data2.append(data1[i]+data1[j])
data2.sort()

result = 0

for i in range(n):
    for j in range(i,n):
        a = data1[j]-data1[i]
        left = 0
        right = len(data2) - 1
        while left<=right:
            mid = (left+right) // 2
            b = data2[mid]
            if a > b:
                left = mid + 1
            elif a < b:
                right = mid - 1
            else:
                result = max(result,data1[j])
                break

print(result)