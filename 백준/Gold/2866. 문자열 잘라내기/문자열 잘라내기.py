r,c = map(int,input().split())
graph = [input() for _ in range(r)]

start = 0
end  = r-1
result  = 0

while start<=end:
    flag = True
    mid = (start+end) // 2
    tmp = set()
    
    for j in range(c):
        word = ""
        for i in range(mid,r):
            word += graph[i][j]
        
        if word not in tmp:
            tmp.add(word)
        else:
            flag =False
            break

    if flag:
        result = mid
        start = mid+1
        
    else:
        end= mid-1
print(result)
