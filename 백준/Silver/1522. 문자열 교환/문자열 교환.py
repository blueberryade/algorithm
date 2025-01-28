import sys
input = sys.stdin.readline

s = input().rstrip()

cnt = s.count('a')
s= s+s
result = sys.maxsize

for i in range(len(s)-cnt):
    result = min(result,s[i:i+cnt].count('b'))
print(result)