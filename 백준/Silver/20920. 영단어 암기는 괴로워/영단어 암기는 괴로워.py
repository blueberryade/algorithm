import sys
input = sys.stdin.readline

words = {}
N,M = map(int,input().split())
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    else:
        if word not in words:
            words[word] = 1
        else:
            words[word]+=1

result = sorted(words.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))


for i in result:
    print(i[0])