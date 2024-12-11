import sys
input = sys.stdin.readline

N = int(input())
calender = [0]*366

for _ in range(N):
    s,e = map(int,input().split())
    for i in range(s,e+1):
        calender[i]+=1

row,col,result = 0,0,0

for i in calender:
    if i !=0:
        col = max(col,i)
        row+=1
    else:
        result+= row*col
        row = 0
        col = 0

result+=row*col
print(result)
