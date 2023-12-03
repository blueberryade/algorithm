import sys
input = sys.stdin.readline

s = input().strip()
result = set()

for i in range(0,len(s)):
    for j in range(1,len(s)-i+1):
        result.add(s[i:i+j])
print(len(result))