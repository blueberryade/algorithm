import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    c,s = map(int,input().split())
    data.append((s,c,i))
data.sort()

result = [0]*n
color_size = [0]*(n+1)
total_size = 0
j = 0

for i in range(n):
    while data[j][0] < data[i][0]:
        color_size[data[j][1]]+=data[j][0]
        total_size+=data[j][0]
        j+=1

    result[data[i][2]] = total_size - color_size[data[i][1]]

for i in range(n):
    print(result[i])
    