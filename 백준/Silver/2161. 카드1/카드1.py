N = int(input())
q = [i for i in range(1,N+1)]
result = []
while len(q)!=1:
    result.append(q.pop(0))
    q.append(q.pop(0))

for i in result:
    print(i,end=' ')

print(q[0])