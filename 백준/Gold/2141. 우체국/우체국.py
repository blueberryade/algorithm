import sys
input = sys.stdin.readline

N = int(input())
data = []
people = 0
for _ in range(N):
    a,b = map(int,input().split())
    data.append((a,b))
    people+=b

data.sort()

count = 0

for i in range(N):
    count+=data[i][1]
    if count >= people/2:
        print(data[i][0])
        break
