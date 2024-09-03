from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
freq = Counter(arr)
result = [-1]* n
stack = []

for i in range(n):
    while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)