import sys
input = sys.stdin.readline

n = int(input())
graph = {}
times = [0]*(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    times[i] = data[0]
    if data[1] !=0:
       for j in data[2:]:
           if i in graph:
                graph[i].append(j)
           else:
               graph[i] = [j]
				
for i in range(1,n+1):
	if i in graph:
		time = 0
		for j in graph[i]:
			time = max(time,times[j])
		times[i]+=time
print(max(times))						  