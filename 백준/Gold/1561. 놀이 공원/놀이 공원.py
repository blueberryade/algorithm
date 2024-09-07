n,m = map(int,input().split())
times = list(map(int,input().split()))

left,right = 0,2000000000000
total_time = 0

while left <= right:
    mid = (left+right) // 2

    total = m
    for time in times:
        total+= mid // time
    
    if total >=n:
        total_time = mid
        right = mid-1
    else:
        left = mid+1
person = m
for time in times:
    person += (total_time -1) // time


for i in range(m):
    if total_time % times[i] == 0:
        person+=1
    if person == n:
        print(i+1)
        break