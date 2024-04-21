import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
dic = {}

for word in words:
    x = len(word)-1
    for w in word:
        if w in dic:
            dic[w]+=10**x
        else:
            dic[w] = 10**x
        x-=1

s = sorted(dic.values(),reverse=True)
result = 0
num = 9
for i in s:
    result+=i*num
    num-=1
print(result)    

