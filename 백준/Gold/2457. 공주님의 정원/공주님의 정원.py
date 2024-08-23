n = int(input())
flowers = []

for _ in range(n):
    sm,sd,em,ed = map(int,input().split())
    flowers.append((sm*100+sd,em*100+ed))

flowers.sort()

idx = 0
result = 0
end = 301

while idx < n:
    s,e = flowers[idx]
    if s <= end < e:
        max_end = e 
        while idx < n-1: 
            ns,ne = flowers[idx+1]
            if end < ns: 
                break
            if max_end < ne:
                max_end = ne
            idx += 1
            
        result += 1
        end = max_end
        

        if 1130 < end:
            print(result)
            exit(0)
    idx += 1

print(0)