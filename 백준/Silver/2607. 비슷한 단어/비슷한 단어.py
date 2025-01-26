N = int(input())

result = 0
first = list(input())

for _ in range(N-1):
    word = list(input())
    compare = first[:]
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt+=1
    
    if cnt < 2 and len(compare) < 2:
        result+=1
        
print(result)

    
    